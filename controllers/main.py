from flet_mvc import FletController
import flet as ft


class Controller(FletController):
    def __init__(self, page, model):
        super().__init__(page, model)
        self.settings()

    def settings(self):
        self.file_picker = ft.FilePicker(
            on_result=self.pick_files_result,
        )
        self.page.overlay.append(self.file_picker)

    def pick_files(self, e=None):
        self.file_picker.pick_files(
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["pdf"],
            allow_multiple=True,
        )

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        print("pick_files_result")
        if e.files:
            file_names = ", ".join([f.name for f in e.files])
            print(f"Arquivos selecionados: {file_names}")
        else:
            print("Nenhum arquivo selecionado.")

    def insert_file_example(self, e):
        print("Arquivo exemplo inserido.")
        self.model.pdf_files_selected().append(
            {"name": "Exemplo.pdf", "path": "exemplo.pdf"}
        )

    def show_pdf_files(self, e):
        print("Arquivos PDF:")
        for file in self.model.pdf_files_selected():
            print(f"Nome: {file['name']}, Path: {file['path']}")
