"""
ats_builder.py — genbrugelig ATS-optimeret dokumentbygger (dansk arbejdsmarked).

Bruges af hver ny ansøgning:
    from ats_builder import Application
    a = Application()
    a.cover_letter(...)
    a.resume(...)
    a.save("Shahram_Ajloo_FIRMA_Stilling.docx")

Designkrav (ATS + menneske):
  * A4, smalle marginer, Calibri 9,5 pt — samme visuelle sprog som de tidligere ansøgninger.
  * Ingen tabeller, tekstbokse, spalter, ikoner i tekstlaget, header/footer-tekst.
  * Kontaktinfo i selve brødteksten (ikke i sidehoved) — ATS læser brødteksten.
  * Overskrifter er rigtige ord med tegnafstand (w:spacing) — IKKE "L E D E R" med mellemrum,
    som ødelægger ATS-tokenisering.
  * Sammenhængende læserækkefølge: ansøgning → sideskift → CV.
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re

INK = RGBColor(0x1A, 0x1A, 0x1A)
META = RGBColor(0x55, 0x55, 0x55)
ACCENT = RGBColor(0x00, 0x77, 0xC8)
BULLET = "\u25cf  "


# Schema-rækkefølge for w:rPr og w:pPr — Word er streng, så elementer indsættes på plads.
_RPR_AFTER_SPACING = ("w:w", "w:kern", "w:position", "w:sz", "w:szCs", "w:highlight", "w:u",
                      "w:effect", "w:bdr", "w:shd", "w:fitText", "w:vertAlign", "w:rtl",
                      "w:cs", "w:em", "w:lang", "w:eastAsianLayout", "w:specVanish",
                      "w:oMath")
_PPR_AFTER_PBDR = ("w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap",
                   "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN",
                   "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing", "w:ind",
                   "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
                   "w:textDirection", "w:textAlignment", "w:textboxTightWrap",
                   "w:outlineLvl", "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr",
                   "w:pPrChange")


def _insert_ordered(parent, child, successors):
    for tag in successors:
        found = parent.find(qn(tag))
        if found is not None:
            found.addprevious(child)
            return child
    parent.append(child)
    return child


def _set_spacing(run, twips):
    """Tegnafstand i 1/20 pt — giver 'spaced caps' uden at bryde ordene."""
    rPr = run._r.get_or_add_rPr()
    for old in rPr.findall(qn("w:spacing")):
        rPr.remove(old)
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:val"), str(twips))
    _insert_ordered(rPr, sp, _RPR_AFTER_SPACING)


class Application:
    def __init__(self, font="Calibri", size=9.5):
        self.doc = Document()
        self.size = size

        st = self.doc.styles["Normal"]
        st.font.name = font
        st.font.size = Pt(size)
        st.font.color.rgb = INK
        st.element.rPr.rFonts.set(qn("w:eastAsia"), font)
        st.paragraph_format.space_before = Pt(0)
        st.paragraph_format.space_after = Pt(0)

        s = self.doc.sections[0]
        s.page_width = Cm(21.0)
        s.page_height = Cm(29.7)
        for attr in ("left_margin", "right_margin"):
            setattr(s, attr, Cm(1.6))
        s.top_margin = Cm(1.3)
        s.bottom_margin = Cm(1.1)

    # ---------- primitiver ----------
    def _p(self, after=1.0, line=None, before=0.0, left=None, hang=None,
           align=WD_ALIGN_PARAGRAPH.LEFT, keep=False):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_after = Pt(after)
        pf.space_before = Pt(before)
        if line:
            pf.line_spacing = Pt(line)
        if left is not None:
            pf.left_indent = Cm(left)
        if hang is not None:
            pf.first_line_indent = Cm(-hang)
        pf.alignment = align
        pf.widow_control = True
        if keep:
            pf.keep_with_next = True
        return p

    def _rich(self, p, text, size=None, color=INK, base_bold=False):
        """**fed** markering i teksten."""
        for part in re.split(r"(\*\*.+?\*\*)", text):
            if not part:
                continue
            bold = base_bold
            if part.startswith("**") and part.endswith("**"):
                part = part[2:-2]
                bold = True
            r = p.add_run(part)
            r.font.size = Pt(size or self.size)
            r.font.color.rgb = color
            r.font.bold = bold
        return p

    # ---------- byggeklodser ----------
    def meta(self, text, after=0.5):
        p = self._p(after=after, line=10.5)
        r = p.add_run(text)
        r.font.size = Pt(8.5)
        r.font.color.rgb = META
        return p

    def subject(self, text, before=3, after=5):
        p = self._p(before=before, after=after, line=12, keep=True)
        r = p.add_run(text)
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = INK
        return p

    def para(self, text, before=0, after=3.2, line=11.75):
        p = self._p(before=before, after=after, line=line, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        return self._rich(p, text)

    def bullet(self, label, body, after=2.1, line=11.4):
        p = self._p(after=after, line=line, left=0.42, hang=0.42,
                    align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        r = p.add_run(BULLET)
        r.font.size = Pt(8.5)
        r.font.color.rgb = ACCENT
        if label:
            self._rich(p, f"**{label}:** " if not label.endswith(":") else f"**{label}** ")
        self._rich(p, body)
        return p

    def heading(self, text, before=7, after=3.0):
        p = self._p(before=before, after=after, line=12, keep=True)
        r = p.add_run(text.upper())
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = INK
        _set_spacing(r, 26)
        # tynd streg under sektionen
        pPr = p._p.get_or_add_pPr()
        bdr = OxmlElement("w:pBdr")
        bottom = OxmlElement("w:bottom")
        bottom.set(qn("w:val"), "single")
        bottom.set(qn("w:sz"), "4")
        bottom.set(qn("w:space"), "1")
        bottom.set(qn("w:color"), "C9C9C9")
        bdr.append(bottom)
        _insert_ordered(pPr, bdr, _PPR_AFTER_PBDR)
        return p

    def name(self, text, page_break=False):
        p = self._p(after=1, line=15, keep=True)
        if page_break:
            p.add_run().add_break(WD_BREAK.PAGE)
        r = p.add_run(text.upper())
        r.font.size = Pt(17)
        r.font.bold = True
        r.font.color.rgb = INK
        _set_spacing(r, 18)
        return p

    def job(self, title_company, meta, before=4):
        p = self._p(before=before, after=0.5, line=11.6, keep=True)
        self._rich(p, f"**{title_company}**")
        r = p.add_run(" — " + meta)
        r.font.size = Pt(8.5)
        r.font.color.rgb = META
        return p

    def page_break(self):
        p = self._p(after=0)
        p.add_run().add_break(WD_BREAK.PAGE)

    def save(self, path, **meta):
        cp = self.doc.core_properties
        cp.author = meta.get("author", "Shahram Ajloo")
        cp.last_modified_by = meta.get("author", "Shahram Ajloo")
        cp.title = meta.get("title", "")
        cp.subject = meta.get("subject", "")
        cp.keywords = meta.get("keywords", "")
        cp.comments = meta.get("comments", "")
        self.doc.save(path)
        return path

    # ---------- sammensat dokument ----------
    def cover_letter(self, date, recipient, subject, opening, points, mirror=None,
                     honest=None, culture=None, offer=None, practical=None,
                     signoff="Med venlig hilsen,", signature=None, contact=None):
        self.meta(date)
        self.meta(recipient, after=2)
        self.subject(subject)
        for t in opening:
            self.para(t)
        for label, body in points:
            self.bullet(label, body)
        for t in (mirror, honest, culture, offer, practical):
            if t:
                self.para(t, before=2.5)
        p = self._p(before=4, after=1.5, line=12.4)
        r = p.add_run(signoff)
        r.font.size = Pt(self.size)
        r.font.color.rgb = INK
        p = self._p(after=1, line=12.4, keep=True)
        r = p.add_run(signature or "")
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = INK
        if contact:
            self.meta(contact)

    def resume(self, name, title, contact, profile, toolbox, toolbox_title,
               experience, education, core, core_title, keywords):
        self.name(name, page_break=True)
        p = self._p(after=0.5, line=11.6)
        r = p.add_run(title)
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = ACCENT
        self.meta(contact)

        self.heading("Lederprofil", before=7)
        self.para(profile, after=2)

        self.heading(toolbox_title)
        for label, body in toolbox:
            self.bullet(label, body)

        self.heading("Erhvervserfaring")
        for item in experience:
            self.job(item["job"], item["meta"])
            for b in item["bullets"]:
                self.bullet(None, b.replace("\u25cf  ", ""))

        self.heading("Uddannelse og certificeringer")
        for line in education:
            self.bullet(None, line)

        self.heading(core_title)
        for line in core:
            self.bullet(None, line)

        self.heading("Nøgleord (ATS)", before=7, after=2)
        p = self._p(after=0, line=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        r = p.add_run(keywords)
        r.font.size = Pt(8)
        r.font.color.rgb = META
