import flet as ft


class PdfManagementView:
    def __init__(self, controller):
        self.controller = controller
        self.main_layout = self.build()

    def build(self):
        self.navigation_rail = ft.NavigationRail(
            bgcolor="#1A1C1E",
            selected_index=0,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.LAYERS_OUTLINED,
                    selected_icon=ft.icons.LAYERS,
                    label="Juntar PDF",
                    padding=ft.padding.symmetric(horizontal=0, vertical=30),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.PIE_CHART_OUTLINE,
                    selected_icon=ft.icons.PIE_CHART,
                    label="Dividir PDF",
                    padding=ft.padding.symmetric(horizontal=0, vertical=30),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.IMAGE_OUTLINED,
                    selected_icon=ft.icons.IMAGE,
                    label="JPG para PDF",
                    padding=ft.padding.symmetric(horizontal=0, vertical=30),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.PICTURE_AS_PDF_OUTLINED,
                    selected_icon=ft.icons.PICTURE_AS_PDF,
                    label="PDF para JPG",
                    padding=ft.padding.symmetric(horizontal=0, vertical=30),
                ),
            ],
            on_change=lambda e: self.controller.navigation_rail(
                e.control.selected_index
            ),
        )

        self.user = ft.FilledButton(
            disabled=True,
            text="Convidado",
            icon=ft.icons.PERSON,
            width=300,
            style=ft.ButtonStyle(
                bgcolor="#1A1C1E",
                color="#B7BBC2",
                padding=ft.padding.all(20),
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                # alignment=ft.alignment.center_left,
            ),
        )

        self.button_logout = ft.FilledButton(
            text="Sair",
            icon=ft.icons.LOGOUT,
            on_click=lambda _: self.controller.logout(),
            width=300,
            style=ft.ButtonStyle(
                bgcolor="#1A1C1E",
                color="#B7BBC2",
                padding=ft.padding.all(20),
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                # alignment=ft.alignment.center_left,
            ),
        )

        self.column_rail = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=self.navigation_rail,
                    width=180,
                    height=550,
                ),
                ft.Container(
                    height=150,
                    width=180,
                    padding=ft.padding.all(10),
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            self.user,
                            self.button_logout,
                        ],
                    ),
                ),
            ],
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

        self.vertical_divider = ft.VerticalDivider(width=1, color="#2E3136")

        self.main_container = ft.Container(
            content=self.content_column,
            padding=10,
            expand=True,
        )

        return [self.column_rail, self.vertical_divider, self.main_container]
