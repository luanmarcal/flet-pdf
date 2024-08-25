from flet_mvc import FletController
import flet as ft
import uuid
from pdf2image import convert_from_path
import os


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
                idFile = str(uuid.uuid4())
                preview_image_path = self.generate_pdf_preview(file.path, idFile)

                title = ft.Text(
                    value=file.name,
                    width=150,
                    height=50,
                    text_align=ft.TextAlign.CENTER,
                    color="#B7BBC2",
                    max_lines=2,
                )

                inner_column = ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    spacing=5,
                    controls=[
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.icons.CLOSE,
                                icon_color="#B7BBC2",
                                icon_size=20,
                                tooltip="Remover",
                                visual_density=ft.ThemeVisualDensity.COMPACT,
                                on_click=lambda e: self.remove_file(e),
                                key=idFile,
                            ),
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Image(src=preview_image_path, border_radius=5),
                            padding=ft.padding.only(left=18, right=18),
                            alignment=ft.alignment.top_center,
                        ),
                    ],
                )

                column = ft.Column(
                    width=150,
                    controls=[
                        ft.Container(
                            content=inner_column,
                            bgcolor="#252728",
                            padding=5,
                            border_radius=5,
                            height=200,
                            width=150,
                            alignment=ft.alignment.top_center,
                        ),
                        title,
                    ],
                    key=idFile,
                )

                self.model.SelectedPdfFiles().append(column)

            self.update()

    def generate_pdf_preview(self, pdf_path, idFile):
        images = convert_from_path(pdf_path, first_page=0, last_page=1, size=(150, 200))
        preview_image_path = f"./assets/temp/preview_{idFile}.png"
        images[0].save(preview_image_path, "PNG")
        return preview_image_path

    def remove_file(self, e):
        for file in self.model.SelectedPdfFiles():
            if file.key == e.control.key:
                print(f"Arquivo removido: {e.control.key}")
                self.model.SelectedPdfFiles().remove(file)
                os.remove(f"./assets/temp/preview_{e.control.key}.png")
                break

        self.update()

    def show_pdf_files(self, e):
        for file in self.model.SelectedPdfFiles():
            print(file.controls[1].value)
