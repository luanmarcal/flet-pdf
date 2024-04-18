"""
Este módulo contém a função principal da aplicação
"""

import flet as ft


def main(page: ft.Page):
    """
    Função principal da aplicação

    Args:
        page (ft.Page): Página principal da aplicação
    """
    page.theme_mode = ft.ThemeMode.DARK

    rail = ft.NavigationRail(
        selected_index=0,
        extended=True,
        min_width=100,
        min_extended_width=300,
        group_alignment=ft.VerticalAlignment.START,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.LAYERS_OUTLINED,
                selected_icon=ft.icons.LAYERS,
                label="Juntar PDF",
                padding=20,
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PIE_CHART_OUTLINE,
                selected_icon=ft.icons.PIE_CHART,
                label="Dividir PDF",
                padding=20,
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.IMAGE_OUTLINED,
                selected_icon=ft.icons.IMAGE,
                label="JPG para PDF",
                padding=20,
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PICTURE_AS_PDF_OUTLINED,
                selected_icon=ft.icons.PICTURE_AS_PDF,
                label="PDF para JPG",
                padding=20,
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.layout = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Container(
                expand=True,
                content=ft.Text("Container 1"),
                bgcolor=ft.colors.GREEN_100,
            ),
            # ft.Column(
            #     # expand=True,
            #     width=500,
            #     alignment=ft.MainAxisAlignment.CENTER,
            #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            #     controls=[
            #         ft.Container(
            #             expand=1,
            #             content=ft.Text("Container 1"),
            #             bgcolor=ft.colors.GREEN_100,
            #         ),
            #         ft.Container(
            #             expand=2,
            #             content=ft.Text("Container 2"),
            #             bgcolor=ft.colors.RED_100,
            #         ),
            #     ],
            # ),
        ],
        expand=True,
    )

    page.add(page.layout)
    page.update()


ft.app(target=main)
