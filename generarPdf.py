from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Pdf():
    def __init__(self):
        self.nombre_archivo = "documento.pdf"

    def generarPdf(self, historial):
        # Crear un objeto Canvas (lienzo) para el PDF
        c = canvas.Canvas(self.nombre_archivo, pagesize=letter)

        # Agregar contenido al PDF
        c.drawString(
            100, 750, "Historial")
        c.drawString(200, 930, f"{historial}")

        # Guardar el PDF y cerrar el objeto Canvas
        c.save()

        print(f"Se ha generado el archivo PDF: {self.nombre_archivo}")
