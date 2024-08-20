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
        if e.files:
            for file in e.files:
                print(f"Arquivo selecionado: {file.name}")

                title = ft.Text(
                    value=file.name,
                    width=150,
                    height=50,
                    text_align=ft.TextAlign.CENTER,
                    color="#B7BBC2",
                    max_lines=2,
                )

                column = ft.Column(
                    width=150,
                    controls=[
                        ft.Container(
                            content=None,
                            bgcolor="#252728",
                            padding=10,
                            border_radius=5,
                            height=200,
                            width=150,
                            alignment=ft.alignment.center,
                        ),
                        title,
                    ],
                )

                self.model.SelectedPdfFiles().append(column)

            self.update()

    def show_pdf_files(self, e):
        for file in self.model.SelectedPdfFiles():
            print(f"Nome: {file['name']}, Path: {file['path']}")
