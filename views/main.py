from flet_mvc import FletView
import flet as ft


class MainView(FletView):
    def __init__(self, controller, model):
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
            on_change=lambda e: print(
                "Selected destination:", e.control.selected_index
            ),
        )

        self.header_content_row = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ADD_ROUNDED,
                    icon_color="#B7BBC2",
                    icon_size=35,
                    tooltip="Adicionar",
                    on_click=controller.pick_files,
                ),
                ft.IconButton(
                    icon=ft.icons.CHECK_ROUNDED,
                    icon_color="#2E3136",
                    icon_size=30,
                    tooltip="Confirmar",
                ),
                ft.IconButton(
                    icon=ft.icons.REMOVE_RED_EYE_OUTLINED,
                    icon_color="#2E3136",
                    icon_size=30,
                    tooltip="Visualizar",
                    on_click=controller.show_pdf_files,
                ),
            ],
        )

        self.central_content_row = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            wrap=True,
            spacing=30,
            run_spacing=30,
            controls=model.SelectedPdfFiles(),
        )

        self.content_column = ft.Column(
            controls=[
                ft.Container(
                    content=self.header_content_row,
                    border=ft.border.all(1, "#2E3136"),
                    margin=10,
                    padding=10,
                    border_radius=5,
                    height=100,
                ),
                ft.Container(
                    content=self.central_content_row,
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

        view = [
            self.main_layout,
        ]
        super().__init__(model, view, controller)
