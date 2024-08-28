from flet_mvc import FletController
import flet as ft
import fitz
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
                pdf_document = self.model.add_pdf(file.name, file.path)
                pdf_document.preview = self.generate_preview(
                    pdf_document.id, pdf_document.path
                )

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
                                on_click=lambda e: self.remove_pdf(e),
                                key=pdf_document.id,
                            ),
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Image(src=pdf_document.preview, border_radius=5),
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
                    key=pdf_document.id,
                )

                pdf_document.content = column
                self.model.list_pdf.append(pdf_document)
                self.model.list_pdf_render().append(pdf_document.content)

            self.update()

    def generate_preview(self, idFile, pdf_path):
        pdf_document = fitz.open(pdf_path)
        page = pdf_document.load_page(0)

        zoom_x = 150 / page.rect.width
        zoom_y = 200 / page.rect.height
        matrix = fitz.Matrix(zoom_x, zoom_y)

        pix = page.get_pixmap(matrix=matrix, alpha=False)
        preview_image_path = f"./assets/temp/preview_{idFile}.png"
        pix.save(preview_image_path)

        pdf_document.close()
        return preview_image_path

    def merge_pdf_files(self, e):
        print("Merge PDF Files")
        pdf_files = self.model.list_pdf
        if len(pdf_files) > 1:
            pdf_document = fitz.open()
            for pdf_file in pdf_files:
                pdf_document.insert_pdf(fitz.open(pdf_file.path))

            pdf_document.save("./assets/temp/merged.pdf")
            pdf_document.close()
            print("PDFs merged")
        else:
            print("Selecione mais de um arquivo PDF")

    def remove_pdf(self, e):
        for file in self.model.list_pdf_render():
            if file.key == e.control.key:
                for file_model in self.model.list_pdf:
                    if file_model.id == e.control.key:
                        self.model.list_pdf.remove(file_model)
                        break
                print(f"Arquivo removido: {e.control.key}")
                self.model.list_pdf_render().remove(file)
                try:
                    os.remove(f"./assets/temp/preview_{e.control.key}.png")
                except:
                    pass
                break

        self.update()
