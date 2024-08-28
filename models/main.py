import uuid
import fitz
import os


class PDFFile:
    def __init__(self, name, path):
        self.id = str(uuid.uuid4())
        self.name = name
        self.path = path
        self.preview = self.generate_preview(self.id, path)
        self.content = None

    def generate_preview(self, id, path):
        pdf_document = fitz.open(path)
        page = pdf_document.load_page(0)

        zoom_x = 150 / page.rect.width
        zoom_y = 200 / page.rect.height
        matrix = fitz.Matrix(zoom_x, zoom_y)

        pix = page.get_pixmap(matrix=matrix, alpha=False)
        preview_image_path = f"./assets/temp/preview_{id}.png"
        pix.save(preview_image_path)

        pdf_document.close()
        return preview_image_path


class Model:
    def __init__(self):
        self.list_pdf = []

    def add_pdf(self, name, path):
        pdf_file = PDFFile(name, path)
        return pdf_file

    def insert_pdf(self, pdf_file):
        self.list_pdf.append(pdf_file)

    def remove_pdf(self, id):
        for pdf_file in self.list_pdf:
            if pdf_file.id == id:
                self.list_pdf.remove(pdf_file)
                try:
                    os.remove(pdf_file.preview)
                except:
                    pass

    def merge_pdf_files(self):
        pdf_files = self.list_pdf
        if len(pdf_files) > 1:
            pdf_document = fitz.open()
            for pdf_file in pdf_files:
                pdf_document.insert_pdf(fitz.open(pdf_file.path))

            pdf_document.save("./assets/temp/merged.pdf")
            pdf_document.close()
            print("PDFs merged")
        else:
            print("Selecione mais de um arquivo PDF")
