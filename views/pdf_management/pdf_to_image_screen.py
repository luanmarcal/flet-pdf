import flet as ft


class PdfToImageScreen:
    def __init__(self, controller):
        self.controller = controller
        self.content_list = self.build()

    def build(self):
        self.header_content_row = ft.Row(
            controls=[],
        )

        self.central_content_row = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            wrap=True,
            spacing=30,
            run_spacing=30,
            controls=[],
        )

        return [self.header_content_row, self.central_content_row]
