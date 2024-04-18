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

    test2 = ft.ResponsiveRow(
        controls=[
            ft.Text("Container with background vdsadasdasdasdasdsaddasdasdasd"),
            ft.Text("Container with background vdsadasdasdasdasdsaddasdasdasd"),
            # ft.TextButton(text="Text button"),
        ],
        # bgcolor=ft.colors.BLUE,
        # padding=10,
        # expand=True,
    )

    test3 = ft.ResponsiveRow(
        controls=[
            ft.Text("Container with background vdsadasdasdasdasdsaddasdasdasd"),
            ft.Text("Container with background vdsadasdasdasdasdsaddasdasdasd"),
        ],
    )

    test = ft.Column(
        [
            ft.Container(
                content=test2,
                bgcolor=ft.colors.BLUE,
                padding=10,
                height=100,
                width="100%",
            ),
            ft.Container(
                content=test3,
                bgcolor=ft.colors.RED,
                padding=10,
                expand=True,
                width="100%",
            ),
        ],
    )

    page.layout = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Container(
                content=test,
                bgcolor=ft.colors.GREEN,
                padding=10,
                expand=True,
                # border=ft.border.all(1, ft.colors.OUTLINE),
            ),
        ],
        expand=True,
    )

    page.add(page.layout)
    page.update()


ft.app(target=main)
