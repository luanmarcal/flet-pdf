import flet as ft


class MergeScreen:
    def __init__(self, controller):
        self.controller = controller
        self.content_list = self.build()

    def update_central_content_row(self, content_list: list):
        self.central_content_row.controls = content_list
        self.central_content_row.update()

    def build(self):
        self.header_content_row = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ADD_ROUNDED,
                    icon_color="#B7BBC2",
                    icon_size=35,
                    tooltip="Adicionar",
                    on_click=lambda _: self.controller.pick_files(),
                ),
                ft.IconButton(
                    icon=ft.icons.CHECK_ROUNDED,
                    icon_color="#2E3136",
                    icon_size=30,
                    tooltip="Confirmar",
                    on_click=lambda _: self.controller.save_file(),
                ),
                ft.IconButton(
                    icon=ft.icons.REMOVE_RED_EYE_OUTLINED,
                    icon_color="#2E3136",
                    icon_size=30,
                    tooltip="Visualizar",
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
