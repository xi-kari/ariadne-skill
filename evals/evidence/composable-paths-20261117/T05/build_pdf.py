from pathlib import Path
from xml.sax.saxutils import escape
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

root = Path(__file__).resolve().parent
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
body = ParagraphStyle('body',fontName='STSong-Light',fontSize=9.2,leading=13.2,wordWrap='CJK',spaceAfter=6)
title = ParagraphStyle('title',parent=body,fontSize=15,leading=20,spaceAfter=9)
cell = ParagraphStyle('cell',parent=body,fontSize=8.7,leading=12,spaceAfter=0)

def clean(s):
    return escape(re.sub(r'\*\*(.*?)\*\*',r'\1',s))

blocks = (root/'one_page_arrangement.md').read_text().strip().split('\n\n')
story = []
for block in blocks:
    if block.startswith('# '):
        story.append(Paragraph(clean(block[2:]),title))
    elif block.startswith('|'):
        rows=[]
        for line in block.splitlines():
            fields=[x.strip() for x in line.strip('|').split('|')]
            if all(re.fullmatch(r'[-:]+',x) for x in fields):
                continue
            rows.append([Paragraph(clean(x),cell) for x in fields])
        t=Table(rows,colWidths=[187,63,63,202],repeatRows=1)
        t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#c3cdd2')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eef3f5')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
        story.extend([t,Spacer(1,8)])
    else:
        story.append(Paragraph(clean(block),body))
SimpleDocTemplate(str(root/'one_page_arrangement.pdf'),pagesize=A4,rightMargin=40,leftMargin=40,topMargin=34,bottomMargin=34,title='公共服务站下周Q方案安排').build(story)
print(root/'one_page_arrangement.pdf')
