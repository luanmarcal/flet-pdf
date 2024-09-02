import flet as ft


class PdfManagementView:
    def __init__(self, controller):
        self.controller = controller
        self.main_layout = self.build()

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

        self.vertical_divider = ft.VerticalDivider(width=1, color="#2E3136")

        self.main_container = ft.Container(
            content=self.content_column,
            padding=10,
            expand=True,
        )

        return [self.navigation_rail, self.vertical_divider, self.main_container]
