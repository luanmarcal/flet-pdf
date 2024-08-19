from flet_mvc import FletController
import flet as ft


class Controller(FletController):
    def __init__(self, page, model):
        super().__init__(page, model)

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
