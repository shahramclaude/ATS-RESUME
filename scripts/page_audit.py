#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""page_audit.py — sidelayout-kontrol for masterdesign-dokumenter.

Bruger preview_docx's layoutmotor til at rapportere, hvor fyldt hver side er
og hvilket blokelement der starter på hver side, så indholdet kan trimmes
til præcis det aftalte sideantal.

Brug:
    python3 scripts/page_audit.py <fil.docx> [ud.pdf]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import preview_docx as P  # noqa: E402
from docx import Document  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.text.paragraph import Paragraph  # noqa: E402


def label(el, doc):
    if el is None:
        return ""
    if el.tag.endswith("tbl"):
        tc0 = el.findall(qn("w:tr"))[0].findall(qn("w:tc"))[0]
        return "TABEL: " + "".join(t.text or "" for t in tc0.iter(qn("w:t")))[:58]
    return "TEKST: " + Paragraph(el, doc).text[:58]


def main():
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/audit.pdf"
    d = Document(src)
    s = d.sections[0]
    pv = P.Preview(out, (s.left_margin.pt, s.right_margin.pt, s.top_margin.pt, s.bottom_margin.pt))
    blocks = [c for c in d.element.body.iterchildren() if c.tag.split("}")[1] in ("p", "tbl")]
    start_of_page = {1: "side 1"}
    page = 1

    def keeps(c):
        if c is None:
            return False
        if c.tag.endswith("tbl"):
            return True
        return P.para_info(c)["keep"]

    for bi, child in enumerate(blocks):
        tag = child.tag.split("}")[1]
        if tag == "tbl":
            tbl = child
            rows = tbl.findall(qn("w:tr"))
            tc0 = rows[0].findall(qn("w:tc"))[0]
            shade = P.w(P.w(tc0, "tcPr"), "shd")
            fill = shade.get(qn("w:fill"), "") if shade is not None else ""
            indent = int(P.w(P.w(tbl, "tblPr"), "tblInd").get(qn("w:w"), "0"))
            if fill == "002B5C" and len(tc0.findall(qn("w:p"))) > 1:
                pv.draw_banner_table(tbl, indent, header=True)
            elif len(tbl.findall(qn("w:tblGrid"))[0].findall(qn("w:gridCol"))) == 2:
                pv.draw_models_table(tbl, indent)
            else:
                h = P.measure_banner(pv, tbl, indent)
                for j in range(bi + 1, min(bi + 6, len(blocks))):
                    nb = blocks[j]
                    h += (P.measure_banner(pv, nb, indent) if nb.tag.endswith("tbl")
                          else P.measure_para(pv, nb))
                    if not keeps(nb):
                        break
                pv.need(h)
                pv.draw_banner_table(tbl, indent)
        elif tag == "p":
            p = Paragraph(child, d)
            if child.findall(".//" + qn("w:br")):
                pv.new_page()
                page = pv.page
                start_of_page[page] = "sidebrud"
                continue
            if not p.text.strip():
                pv.y -= 8
                continue
            if P.para_info(child)["keep"]:
                h = P.measure_para(pv, child)
                for j in range(bi + 1, min(bi + 6, len(blocks))):
                    nb = blocks[j]
                    if not nb.tag.endswith("p"):
                        break
                    h += P.measure_para(pv, nb)
                    if not keeps(nb):
                        break
                pv.need(h)
            before = pv.page
            pv.draw_para(child)
            if pv.page != before:
                page = pv.page
                start_of_page.setdefault(page, label(child, d))
    pv.save()
    usable = P.PAGE_H - pv.mt - pv.mb
    print(f"{src} | sider={pv.page}")
    for pg in sorted(start_of_page):
        print(f"  side {pg}: {start_of_page[pg]}")
    print(f"  fyldning sidste side: {round((P.PAGE_H - pv.mt - pv.y) / usable, 2)}")
    print(f"  PDF: {out}")


if __name__ == "__main__":
    main()
