from flet_mvc import FletModel, data
import flet as ft
import uuid


class PDFFile:
    def __init__(self, name, path):
        self.id = str(uuid.uuid4())
        self.name = name
        self.path = path
        self.preview = None
        self.content = None


class Model(FletModel):
    def __init__(self):
        self.list_pdf = []

    @data
    def list_pdf_render(self):
        return []

    def add_pdf(self, name, path):
        return PDFFile(name, path)
