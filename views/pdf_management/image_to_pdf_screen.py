import flet as ft


class ImageToPdfScreen:
    def __init__(self, controller):
        self.controller = controller
        self.content_list = self.build()

    def build(self):
        self.header_content_row = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.LAYERS_OUTLINED,
                    icon_color="#B7BBC2",
                    icon_size=35,
                    tooltip="Sair",
                    on_click=lambda _: self.controller.logout(),
                ),
            ],
        )

        self.central_content_row = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            wrap=True,
            spacing=30,
            run_spacing=30,
            controls=[],
        )

        return [self.header_content_row, self.central_content_row]
