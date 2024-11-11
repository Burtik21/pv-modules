from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Vytvoření PDF
pdf = canvas.Canvas("example.pdf", pagesize=letter)
pdf.drawString(100, 750, "Hello World!")
pdf.save()
