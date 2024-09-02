import flet as ft


class MergeScreen:
    def __init__(self, controller):
        self.controller = controller
        self.content_list = self.build()

    def update_central_content_row(self, content_list: list):
        self.central_content_row.controls = content_list
        self.central_content_row.update()

    def create_pdf_card(self, card_id: str, name: str, preview: str):
        title = ft.Text(
            value=name,
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
                        on_click=self.controller.handle_remove_pdf,
                        key=card_id,
                    ),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=ft.Image(src=preview, border_radius=5),
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
            key=card_id,
        )

        return column

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
