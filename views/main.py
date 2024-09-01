import flet as ft


class MainView:
    def __init__(self, controller):
        self.controller = controller
        self.main_layout = self.build()

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
        self.navigation_rail = ft.NavigationRail(
            selected_index=0,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.LAYERS_OUTLINED,
                    selected_icon=ft.icons.LAYERS,
                    label="Juntar PDF",
                    padding=30,
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.PIE_CHART_OUTLINE,
                    selected_icon=ft.icons.PIE_CHART,
                    label="Dividir PDF",
                    padding=30,
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.IMAGE_OUTLINED,
                    selected_icon=ft.icons.IMAGE,
                    label="JPG para PDF",
                    padding=30,
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.PICTURE_AS_PDF_OUTLINED,
                    selected_icon=ft.icons.PICTURE_AS_PDF,
                    label="PDF para JPG",
                    padding=30,
                ),
            ],
            on_change=lambda e: self.controller.navigation_rail(
                e.control.selected_index
            ),
        )

        self.content_column = ft.Column(
            controls=[
                ft.Container(
                    border=ft.border.all(1, "#2E3136"),
                    margin=10,
                    padding=10,
                    border_radius=5,
                    height=100,
                ),
                ft.Container(
                    border=ft.border.all(1, "#2E3136"),
                    padding=30,
                    margin=10,
                    border_radius=5,
                    expand=True,
                    alignment=ft.alignment.top_center,
                ),
            ],
        )

        self.main_row = ft.Row(
            [
                self.navigation_rail,
                ft.VerticalDivider(width=1, color="#2E3136"),
                ft.Container(
                    content=self.content_column,
                    padding=10,
                    expand=True,
                ),
            ],
        )

        self.main_layout = ft.Container(
            content=self.main_row,
            expand=True,
            padding=10,
        )

        return self.main_layout
