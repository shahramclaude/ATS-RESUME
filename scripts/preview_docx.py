# -*- coding: utf-8 -*-
"""
preview_docx.py — paginerings- og layoutkontrol af et master-design-docx.

Render en tro kopi (Carlito = metrisk identisk med Calibri) til PDF/PNG ud fra
den FAKTISKE docx, så sidetal, sidebrydninger og banner-højder kan kontrolleres
uden Word/LibreOffice.

Brug:
    python3 scripts/preview_docx.py fil.docx [ud.pdf]
"""
import sys

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = "/tmp/car/carlito-main/fonts/ttf"
for name, f in (("Carlito", "Carlito-Regular.ttf"), ("Carlito-Bold", "Carlito-Bold.ttf"),
                ("Carlito-Italic", "Carlito-Italic.ttf")):
    pdfmetrics.registerFont(TTFont(name, f"{FONT_DIR}/{f}"))

TW = 1.0 / 20.0          # twips -> points
PAGE_W, PAGE_H = A4

# sekvens-navne fra Word
RPR_ORDER = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike",
             "dstrike", "outline", "shadow", "emboss", "imprint", "noProof", "snapToGrid",
             "vanish", "webHidden", "color", "spacing", "w", "kern", "position", "sz",
             "szCs", "highlight", "u", "effect", "bdr", "shd", "fitText", "vertAlign",
             "rtl", "cs", "em", "lang"]


def w(el, tag):
    return el.find(qn("w:" + tag))


def val(el, tag, default=None, attr="w:val"):
    e = w(el, tag)
    if e is None:
        return default
    return e.get(qn(attr), default)


def run_info(r):
    rPr = w(r, "rPr")
    info = {"text": "".join(t.text or "" for t in r.iter(qn("w:t"))),
            "bold": False, "italic": False, "color": "1A1A1A", "size": 9.5, "spacing": 0.0}
    if rPr is not None:
        if w(rPr, "b") is not None:
            info["bold"] = True
        if w(rPr, "i") is not None:
            info["italic"] = True
        c = val(rPr, "color")
        if c:
            info["color"] = c
        sz = val(rPr, "sz")
        if sz:
            info["size"] = int(sz) / 2.0
        sp = val(rPr, "spacing")
        if sp:
            info["spacing"] = int(sp) * TW
    return info


def para_info(p):
    pPr = w(p, "pPr")
    d = {"after": 0.0, "before": 0.0, "line": None, "left": 0.0, "hanging": 0.0,
         "justify": False, "keep": False, "runs": [run_info(r) for r in p.findall(qn("w:r"))]}
    if pPr is not None:
        sp = w(pPr, "spacing")
        if sp is not None:
            d["after"] = int(sp.get(qn("w:after"), 0)) * TW
            d["before"] = int(sp.get(qn("w:before"), 0)) * TW
            if sp.get(qn("w:line")):
                d["line"] = int(sp.get(qn("w:line"))) * TW
        ind = w(pPr, "ind")
        if ind is not None:
            d["left"] = int(ind.get(qn("w:left"), 0)) * TW
            d["hanging"] = int(ind.get(qn("w:hanging"), 0)) * TW
        jc = w(pPr, "jc")
        d["justify"] = jc is not None and jc.get(qn("w:val")) == "both"
        d["keep"] = w(pPr, "keepNext") is not None
    return d


def tokenize(runs, base_size=9.5):
    """-> liste af (tekst, font, size, color, charspace) uden at miste mellemrum."""
    out = []
    for r in runs:
        if not r["text"]:
            continue
        font = "Carlito-Bold" if r["bold"] else ("Carlito-Italic" if r["italic"] else "Carlito")
        out.append((r["text"], font, r["size"] or base_size, r["color"], r["spacing"]))
    return out


def wrap(tokens, width):
    """Returnerer linjer som lister af (tekst,font,size,color,spacing, er_mellemrum)."""
    words = []          # (tekst, font, size, color, spacing)
    for text, font, size, color, cs in tokens:
        parts = text.split(" ")
        for i, part in enumerate(parts):
            if part:
                words.append((part, font, size, color, cs))
            if i < len(parts) - 1:
                words.append((" ", font, size, color, cs))
    lines, cur, cur_w = [], [], 0.0
    for word in words:
        wd = pdfmetrics.stringWidth(word[0], word[1], word[2]) + word[4] * len(word[0])
        if cur and cur_w + wd > width and word[0] != " ":
            while cur and cur[-1][0] == " ":
                cur.pop()
            lines.append(cur)
            cur, cur_w = [], 0.0
        if word[0] == " " and not cur:
            continue
        cur.append(word)
        cur_w += wd
    if cur:
        lines.append(cur)
    return lines


def line_width(line):
    return sum(pdfmetrics.stringWidth(t, f, s) + cs * len(t) for t, f, s, c, cs in line)


class Preview:
    def __init__(self, path, margins):
        self.c = canvas.Canvas(path, pagesize=A4)
        self.ml, self.mr, self.mt, self.mb = margins
        self.left = self.ml
        self.width = PAGE_W - self.ml - self.mr
        self.y = PAGE_H - self.mt
        self.page = 1
        self.breaks = []

    def new_page(self):
        self.c.showPage()
        self.page += 1
        self.y = PAGE_H - self.mt
        self.breaks.append(self.page)

    def need(self, h):
        if self.y - h < self.mb:
            self.new_page()

    # ---------------------------------------------------------------- tekst
    def draw_para(self, p, x_offset=0.0, width=None, base_size=9.5, fill_bg=None):
        info = para_info(p)
        width = width or (self.width - info["left"] - x_offset)
        self.y -= info["before"]
        tokens = tokenize(info["runs"], base_size)
        if not tokens:
            self.y -= (info["line"] or 12.0) + info["after"]
            return 0.0
        lines = wrap(tokens, width)
        lh = info["line"] or (max(t[2] for t in tokens) * 1.22)
        for ln in lines:
            self.need(lh)
            x = self.left + x_offset + info["left"] - (info["hanging"] if info["hanging"] else 0)
            if info["hanging"]:
                x = self.left + x_offset + info["left"] - info["hanging"]
            lw = line_width(ln)
            extra = 0.0   # Word justificerer; preview viser venstrekant (samme linjebrydning)
            cx = x
            for i, (text, font, size, color, cs) in enumerate(ln):
                self.c.setFont(font, size)
                self.c.setFillColor(HexColor("#" + color))
                self.c.drawString(cx, self.y - size * 0.80, text)
                cx += pdfmetrics.stringWidth(text, font, size) + cs * len(text)
                if extra and i < len(ln) - 1 and text != " ":
                    cx += extra
            self.y -= lh
        self.y -= info["after"]
        return lh

    # -------------------------------------------------------------- tabeller
    def draw_banner_table(self, tbl, indent_tw, header=False):
        """1x1 banner (valgfrit 2 rækker: header-blok + sektionsbanner)."""
        rows = tbl.findall(qn("w:tr"))
        for ri, tr in enumerate(rows):
            cells = tr.findall(qn("w:tc"))
            tc = cells[0]
            tcPr = w(tc, "tcPr")
            margins = {"top": 0.0, "left": 0.0, "bottom": 0.0, "right": 0.0}
            if tcPr is not None:
                mar = w(tcPr, "tcMar")
                if mar is not None:
                    for side in margins:
                        e = w(mar, side)
                        if e is not None:
                            margins[side] = int(e.get(qn("w:w"), 0)) * TW
            paras = tc.findall(qn("w:p"))
            x = self.left + indent_tw * TW
            width = self.width - indent_tw * TW
            inner = width - margins["left"] - margins["right"]
            # højde først
            total = margins["top"] + margins["bottom"]
            for p in paras:
                info = para_info(p)
                total += info["before"] + info["after"]
                toks = tokenize(info["runs"])
                if toks:
                    lh = info["line"] or (max(t[2] for t in toks) * 1.22)
                    total += lh * len(wrap(toks, inner))
                else:
                    total += 10.0
            self.need(total)
            self.c.setFillColor(HexColor("#002B5C"))
            self.c.rect(x, self.y - total, width, total, stroke=0, fill=1)
            self.y -= margins["top"]
            for p in paras:
                info = para_info(p)
                self.y -= info["before"]
                toks = tokenize(info["runs"])
                if not toks:
                    self.y -= 10.0
                    continue
                lh = info["line"] or (max(t[2] for t in toks) * 1.22)
                for ln in wrap(toks, inner):
                    cx = x + margins["left"]
                    for (text, font, size, color, cs) in ln:
                        self.c.setFont(font, size)
                        self.c.setFillColor(HexColor("#" + color))
                        self.c.drawString(cx, self.y - size * 0.80, text)
                        cx += pdfmetrics.stringWidth(text, font, size) + cs * len(text)
                    self.y -= lh
                self.y -= info["after"]
            self.y -= margins["bottom"]

    def draw_models_table(self, tbl, indent_tw):
        grid = [int(g.get(qn("w:w"))) * TW for g in tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
        x0 = self.left + indent_tw * TW
        for tr in tbl.findall(qn("w:tr")):
            cells = tr.findall(qn("w:tc"))
            span = 2 if len(cells) == 1 else 1
            # rækkehøjde
            heights, contents = [], []
            for ci, tc in enumerate(cells):
                tcPr = w(tc, "tcPr")
                fill = "FFFFFF"
                if tcPr is not None:
                    shd = w(tcPr, "shd")
                    if shd is not None:
                        fill = shd.get(qn("w:fill"), "FFFFFF")
                cw = sum(grid[:span]) if span == 2 else grid[ci]
                inner = cw - 10.0
                h_row, lines_all = 0.0, []
                for p in tc.findall(qn("w:p")):
                    info = para_info(p)
                    toks = tokenize(info["runs"])
                    lines = wrap(toks, inner) if toks else [[]]
                    h_row += info["before"] + info["after"] + len(lines) * (info["line"] or 11.0)
                    lines_all.append((info, lines))
                heights.append(h_row)
                contents.append((cw, inner, fill, lines_all))
            h_total = max(heights)
            self.need(h_total)
            x = x0
            for ci, (cw, inner, fill, lines_all) in enumerate(contents):
                self.c.setFillColor(HexColor("#" + fill))
                self.c.rect(x, self.y - h_total, cw, h_total, stroke=0, fill=1)
                yy = self.y
                for info, lines in lines_all:
                    yy -= info["before"]
                    for ln in lines:
                        cx = x + 5.0
                        for (text, font, size, color, cs) in ln:
                            self.c.setFont(font, size)
                            self.c.setFillColor(HexColor("#" + color))
                            self.c.drawString(cx, yy - size * 0.80, text)
                            cx += pdfmetrics.stringWidth(text, font, size) + cs * len(text)
                        yy -= info["line"] or 11.0
                    yy -= info["after"]
                x += cw
            # gitterlinjer
            self.c.setStrokeColor(HexColor("#8C8C8C"))
            self.c.setLineWidth(0.5)
            self.c.line(x0, self.y - h_total, x0 + sum(grid[:span]), self.y - h_total)
            self.y -= h_total

    def save(self):
        self.c.save()


def main():
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else src.rsplit(".", 1)[0] + "_preview.pdf"
    d = Document(src)
    s = d.sections[0]
    margins = (s.left_margin.pt, s.right_margin.pt, s.top_margin.pt, s.bottom_margin.pt)
    pv = Preview(out, margins)

    for child in d.element.body.iterchildren():
        tag = child.tag.split("}")[1]
        if tag == "tbl":
            tbl = child
            rows = tbl.findall(qn("w:tr"))
            tr0 = rows[0]
            tc0 = tr0.findall(qn("w:tc"))[0]
            shade = w(w(tc0, "tcPr"), "shd")
            fill = shade.get(qn("w:fill"), "") if shade is not None else ""
            indent = int(w(w(tbl, "tblPr"), "tblInd").get(qn("w:w"), "0"))
            if fill == "002B5C" and len(tc0.findall(qn("w:p"))) > 1:
                pv.draw_banner_table(tbl, indent, header=True)
            elif len(tbl.findall(qn("w:tblGrid"))[0].findall(qn("w:gridCol"))) == 2:
                pv.draw_models_table(tbl, indent)
            else:
                pv.draw_banner_table(tbl, indent)
        elif tag == "p":
            p = Paragraph(child, d)
            if child.findall(".//" + qn("w:br")):
                pv.new_page()
                continue
            if not p.text.strip():
                pv.y -= 8
                continue
            pv.draw_para(child)
    pv.save()
    print(f"{out} | pages={pv.page} | breaks at {pv.breaks} | last fill={round((PAGE_H - pv.mt - pv.y) / (PAGE_H - pv.mt - pv.mb), 2)}")


if __name__ == "__main__":
    main()
