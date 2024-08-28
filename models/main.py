import fitz
import os
from models.pdf_file import PDFFile


class Model:
    def __init__(self):
        self.save_path = ""
        self.list_pdf = []

    def add_pdf(self, name: str, path: str):
        pdf_file = PDFFile(name, path)
        return pdf_file

    def insert_pdf(self, pdf_file: PDFFile):
        self.list_pdf.append(pdf_file)

    def remove_pdf(self, id: str):
        for pdf_file in self.list_pdf:
            if pdf_file.id == id:
                self.list_pdf.remove(pdf_file)
                try:
                    os.remove(pdf_file.preview)
                except:
                    pass

    def clear_pdf_list(self):
        for pdf_file in self.list_pdf:
            try:
                os.remove(pdf_file.preview)
            except:
                pass

        self.list_pdf.clear()

    def merge_pdf_files(self):
        pdf_files = self.list_pdf
        pdf_document = fitz.open()
        for pdf_file in pdf_files:
            pdf_document.insert_pdf(fitz.open(pdf_file.path))

        pdf_document.save(self.save_path)
        pdf_document.close()
        print("PDFs merged")
