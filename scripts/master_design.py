# -*- coding: utf-8 -*-
"""
master_design.py — genskaber PRÆCIS designet fra de uploadede master-CV'er
(Shahram_Ajloo_*.docx: navy banner-tabeller 002B5C, Calibri 9,5 pt, A4, 1,59 cm
margener, blå 0077C8 punkter, 9x2 kompetencetabel med Area | Tools, sektioner
EDUCATION / CERTIFICATIONS / LANGUAGES / CORE KEYWORDS (ATS)).

Brug:
    from master_design import MasterDoc
    m = MasterDoc(template="Shahram_Ajloo_NNE_DepartmentManagerEI.docx", lang="en-GB")
    m.header_banner(name, title, contact)
    m.letter(...)
    m.page_break()
    m.resume_header(name, title, contact, first_section="LEADERSHIP PROFILE")
    ...
    m.save("ud.docx")

Alle mål er taget direkte fra XML i master-filerne. Ingen gæt.
"""
import copy
import os

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.enum.text import WD_BREAK

NAVY = "002B5C"
BLUE = "0077C8"
INK = "1A1A1A"
GREY = "555555"
WHITE = "FFFFFF"
LIGHT = "EAF3FA"
BULLET = "\u25cf  "


def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn(k), str(v))
    return e


class MasterDoc:
    def __init__(self, template, lang="en-GB"):
        self.lang = lang
        self.doc = Document(template)
        body = self.doc.element.body
        for child in list(body.iterchildren()):
            if child.tag != qn("w:sectPr"):
                body.remove(child)
        # sikkerhed: ingen hængende sektioner
        self.body = body

    # ------------------------------------------------------------------ utils
    def _p(self, spacing_after=None, spacing_before=None, line=None, exact=True,
           left=None, hanging=None, justify=True, keep_next=False):
        p = self.doc.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        for old in list(pPr):
            pPr.remove(old)
        if keep_next:                      # schema-rækkefølge: keepNext først
            pPr.append(_el("w:keepNext"))
        sp = _el("w:spacing")
        if spacing_before is not None:
            sp.set(qn("w:before"), str(spacing_before))
        if spacing_after is not None:
            sp.set(qn("w:after"), str(spacing_after))
        if line is not None:
            sp.set(qn("w:line"), str(line))
            sp.set(qn("w:lineRule"), "exact" if exact else "auto")
        pPr.append(sp)
        if left is not None:
            pPr.append(_el("w:ind", **{"w:left": left, "w:hanging": hanging or 0}))
        if justify:
            pPr.append(_el("w:jc", **{"w:val": "both"}))
        return p

    def _run(self, p, text, bold=False, size=None, color=INK, spacing=None, italic=False):
        r = p.add_run(text)
        rPr = r._r.get_or_add_rPr()
        if bold:
            rPr.append(_el("w:b"))
            rPr.append(_el("w:bCs"))
        if italic:
            rPr.append(_el("w:i"))
        if color:
            rPr.append(_el("w:color", **{"w:val": color}))
        if spacing is not None:
            rPr.append(_el("w:spacing", **{"w:val": spacing}))
        if size is not None:
            rPr.append(_el("w:sz", **{"w:val": size}))
            rPr.append(_el("w:szCs", **{"w:val": size}))
        else:
            rPr.append(_el("w:szCs", **{"w:val": 19}))
        rPr.append(_el("w:lang", **{"w:val": self.lang}))
        return r

    def _rich(self, p, text, size=None):
        """**fed** i teksten."""
        import re
        for part in re.split(r"(\*\*.+?\*\*)", text):
            if not part:
                continue
            if part.startswith("**") and part.endswith("**"):
                self._run(p, part[2:-2], bold=True, size=size)
            else:
                self._run(p, part, size=size)
        return p

    # ------------------------------------------------------------- tabeller
    def _cell(self, cell, fill, margins, span=None):
        tcPr = cell._tc.get_or_add_tcPr()
        for old in list(tcPr):
            if old.tag != qn("w:gridSpan"):
                tcPr.remove(old)
        # schema-rækkefølge: tcW, gridSpan, shd, tcMar
        tcPr.find(qn("w:gridSpan")) is not None or None
        tcW = _el("w:tcW", **{"w:w": 0, "w:type": "auto"})
        gs = tcPr.find(qn("w:gridSpan"))
        if gs is not None:
            gs.addprevious(tcW)
        else:
            tcPr.append(tcW)
        tcPr.append(_el("w:shd", **{"w:val": "clear", "w:color": fill, "w:fill": fill}))
        mar = _el("w:tcMar")
        for side in ("top", "left", "bottom", "right"):
            if side in margins:
                mar.append(_el("w:" + side, **{"w:w": margins[side], "w:type": "dxa"}))
        tcPr.append(mar)

    def _table(self, indent, widths, header_fill=NAVY):
        t = self.doc.add_table(rows=0, cols=len(widths))
        tblPr = t._tbl.tblPr
        for old in list(tblPr):
            tblPr.remove(old)
        # schema-rækkefølge: tblW, tblInd, tblBorders, tblCellMar, tblLook
        tblPr.append(_el("w:tblW", **{"w:w": 5000, "w:type": "pct"}))
        tblPr.append(_el("w:tblInd", **{"w:w": indent, "w:type": "dxa"}))
        borders = _el("w:tblBorders")
        for side in ("insideH", "insideV"):
            borders.append(_el("w:" + side, **{"w:val": "single", "w:sz": 4,
                                               "w:space": 0, "w:color": "auto"}))
        tblPr.append(borders)
        mar = _el("w:tblCellMar")
        mar.append(_el("w:left", **{"w:w": 10, "w:type": "dxa"}))
        mar.append(_el("w:right", **{"w:w": 10, "w:type": "dxa"}))
        tblPr.append(mar)
        tblPr.append(_el("w:tblLook", **{"w:val": "04A0", "w:firstRow": 1, "w:lastRow": 0,
                                         "w:firstColumn": 1, "w:lastColumn": 0,
                                         "w:noHBand": 0, "w:noVBand": 1}))
        grid = t._tbl.find(qn("w:tblGrid"))
        for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
            gc.set(qn("w:w"), str(w))
        return t

    def _banner_row(self, table, text, fill=NAVY, span=None, margins=None):
        row = table.add_row()
        cells = row.cells
        cell = cells[0]
        if span:
            tcPr = cell._tc.get_or_add_tcPr()
            tcPr.append(_el("w:gridSpan", **{"w:val": span}))
            for extra in cells[1:]:
                extra._tc.getparent().remove(extra._tc)
        m = margins or {"top": 0, "left": 120, "bottom": 0, "right": 120}
        self._cell(cell, fill, m)
        p = cell.paragraphs[0]
        pPr = p._p.get_or_add_pPr()
        pPr.append(_el("w:keepNext"))          # banner må ikke stå alene nederst på en side
        pPr.append(_el("w:spacing", **{"w:before": 40, "w:after": 40}))
        self._run(p, text, bold=True, size=17, color=WHITE, spacing=50)
        return row

    # ------------------------------------------------------------- blokke
    def header_banner(self, name, title, contact, extra_table=None):
        t = self._table(indent=200, widths=[10506])
        row = t.add_row()
        cell = row.cells[0]
        self._cell(cell, NAVY, {"top": 140, "left": 200, "bottom": 120, "right": 200})
        p = cell.paragraphs[0]
        p._p.get_or_add_pPr().append(_el("w:spacing", **{"w:after": 20}))
        self._run(p, name, bold=True, size=44, color=WHITE)
        p2 = cell.add_paragraph()
        p2._p.get_or_add_pPr().append(_el("w:spacing", **{"w:after": 60}))
        self._run(p2, title, bold=True, color=BLUE)
        p3 = cell.add_paragraph()
        p3._p.get_or_add_pPr().append(_el("w:spacing", **{"w:after": 0}))
        self._run(p3, contact, size=17, color=WHITE)
        return t

    def section(self, text):
        t = self._table(indent=120, widths=[10346])
        self._banner_row(t, text)
        return t

    def para(self, text, after=80, line=250, before=None, justify=True):
        p = self._p(spacing_after=after, spacing_before=before, line=line, justify=justify)
        return self._rich(p, text)

    def meta(self, text, after=20, line=250):
        p = self._p(spacing_after=after, line=line)
        self._run(p, text, size=18, color=GREY)
        return p

    def bullet(self, label, body, after=30, line=250):
        p = self._p(spacing_after=after, line=line, left=240, hanging=240)
        self._run(p, BULLET, color=BLUE)
        if label:
            self._run(p, label + ("" if label.endswith(":") else ":"), bold=True, color=INK)
            self._run(p, " " + body, color=INK)
        else:
            self._rich(p, body)
        return p

    def job(self, title, meta, scope=None):
        p = self._p(spacing_after=20, spacing_before=60, line=260, justify=False, keep_next=True)
        self._run(p, title, bold=True, color=INK)
        self._run(p, " — " + meta, size=18, color=GREY)
        if scope:
            q = self._p(spacing_after=20, line=240, justify=False, keep_next=True, left=120)
            self._run(q, "Scope: ", bold=True, size=18, color=NAVY)
            self._run(q, scope, size=18, color=GREY)
        return p

    def edu(self, title, meta):
        p = self._p(spacing_after=20, spacing_before=30, line=260, justify=False)
        self._run(p, title, bold=True, color=INK)
        self._run(p, " · " + meta, size=18, color=GREY)
        return p

    def _no_split(self, row):
        trPr = row._tr.get_or_add_trPr()
        if trPr.find(qn("w:cantSplit")) is None:
            trPr.append(_el("w:cantSplit"))
        return row

    def models_table(self, title, header, rows):
        t = self._table(indent=120, widths=[1937, 8409])
        self._no_split(self._banner_row(t, title, span=2))
        # kolonneoverskrift
        row = t.add_row()
        for cell, txt, bold in zip(row.cells, header, (True, False)):
            self._cell(cell, LIGHT, {})
            p = cell.paragraphs[0]
            p._p.get_or_add_pPr().append(_el("w:spacing", **{"w:before": 50, "w:after": 50}))
            if bold:
                self._run(p, txt, bold=True, size=18, color=NAVY)
            else:
                self._run(p, txt, size=18, color=INK)
        for area, tools in rows:
            row = self._no_split(t.add_row())
            for cell, txt, bold in zip(row.cells, (area, tools), (True, False)):
                self._cell(cell, WHITE, {})
                p = cell.paragraphs[0]
                p._p.get_or_add_pPr().append(_el("w:spacing", **{"w:before": 50, "w:after": 50}))
                if bold:
                    self._run(p, txt, bold=True, size=18, color=NAVY)
                else:
                    self._run(p, txt, size=18, color=INK)
        return t

    def page_break(self):
        p = self.doc.add_paragraph()
        p.add_run().add_break(WD_BREAK.PAGE)
        return p

    def resume_header(self, name, title, contact, first_section):
        t = self._table(indent=200, widths=[10506])
        row = t.add_row()
        cell = row.cells[0]
        self._cell(cell, NAVY, {"top": 140, "left": 200, "bottom": 120, "right": 200})
        p = cell.paragraphs[0]
        p._p.get_or_add_pPr().append(_el("w:spacing", **{"w:after": 20}))
        self._run(p, name, bold=True, size=44, color=WHITE)
        p2 = cell.add_paragraph()
        p2._p.get_or_add_pPr().append(_el("w:spacing", **{"w:after": 60}))
        self._run(p2, title, bold=True, color=BLUE)
        p3 = cell.add_paragraph()
        p3._p.get_or_add_pPr().append(_el("w:spacing", **{"w:after": 0}))
        self._run(p3, contact, size=17, color=WHITE)
        self._banner_row(t, first_section)
        return t

    def save(self, path, **meta):
        cp = self.doc.core_properties
        cp.author = "Shahram Ajloo"
        cp.last_modified_by = "Shahram Ajloo"
        for k, v in meta.items():
            if hasattr(cp, k):
                setattr(cp, k, v)
        self.doc.save(path)
        return path
