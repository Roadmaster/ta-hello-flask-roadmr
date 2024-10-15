from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas

stylesheet = getSampleStyleSheet()
normalStyle = stylesheet["Normal"]

sample = """You are hereby charged that on the 28th day of May, 1970, you did
willfully, unlawfully, and with malice of forethought, publish an
alleged English-Hungarian phrase book with intent to cause a breach
of the peace.  How do you plead?"""

def hello(c):
    c.drawString(100,100,"Hello World" )
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()
