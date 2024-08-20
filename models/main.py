from flet_mvc import FletModel, data
import flet as ft


# class PDFFile:
#     def __init__(self, name: str, path: str):
#         self.name = name
#         self.path = path

class Model(FletModel):
    @data
    def SelectedPdfFiles(self):
        return []
