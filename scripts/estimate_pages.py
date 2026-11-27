import sys, math
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table

LINE_PT = 9.5
CPL = 92
AFTER = 3
TCELL_CPL = 82.5
TCELL_LN = 8
TPAD = 5
PAGE = 752

doc = Document(sys.argv[1])
body = doc.element.body
sections = [0.0]

def para_h(p):
    txt = p.text
    if not txt.strip():
        return LINE_PT
    lines = max(1, -(-len(txt) // CPL))
    pf = p.paragraph_format
    after = pf.space_after.pt if pf.space_after else AFTER
    lh = pf.line_spacing if isinstance(pf.line_spacing, float) else 1.0
    return lines * LINE_PT * lh + after

def tbl_h(t):
    h = 0.0
    for row in t.rows:
        maxl = 1
        for c in row.cells:
            clen = sum(len(p.text) for p in c.paragraphs)
            maxl = max(maxl, -(-clen // TCELL_CPL))
        h += maxl * TCELL_LN + TPAD
    return h

for child in body:
    if child.tag == qn('w:p'):
        has_break = bool(child.findall('.//' + qn('w:br') + '[@' + qn('w:type') + '="page"]'))
        p = Paragraph(child, doc)
        if has_break and sections[-1] > 0:
            sections.append(0.0)
            continue
        sections[-1] += para_h(p)
    elif child.tag == qn('w:tbl'):
        sections[-1] += tbl_h(Table(child, doc))

total = 0
for i, f in enumerate(sections, 1):
    print('side %d: %.2f' % (i, f / PAGE))
    total += math.ceil(f / PAGE)
print('sider i alt: %d' % total)
