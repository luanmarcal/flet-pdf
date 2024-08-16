"""
Este módulo contém a função principal da aplicação
"""

import flet as ft
import test


def main(page: ft.Page):
    """
    Função principal da aplicação

    Args:
        page (ft.Page): Página principal da aplicação
    """
    page.title = "PDF Tools"
    page.theme_mode = ft.ThemeMode.DARK

    navigation_rail = ft.NavigationRail(
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
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    header_content_row = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.icons.ADD_ROUNDED,
                icon_color=ft.colors.WHITE70,
                icon_size=35,
                tooltip="Adicionar",
                on_click=lambda e: test.show_message(),
            ),
            ft.IconButton(
                icon=ft.icons.CHECK_ROUNDED,
                icon_color=ft.colors.GREY_800,
                icon_size=30,
                tooltip="Confirmar",
            ),
            ft.IconButton(
                icon=ft.icons.REMOVE_RED_EYE_OUTLINED,
                icon_color=ft.colors.GREY_800,
                icon_size=30,
                tooltip="Visualizar",
            ),
        ],
    )

    central_content_row = ft.Row()

    content_column = ft.Column(
        [
            ft.Container(
                content=header_content_row,
                border=ft.border.all(1, ft.colors.GREY_800),
                padding=10,
                border_radius=5,
                height=100,
            ),
            ft.Container(
                content=central_content_row,
                border=ft.border.all(1, ft.colors.GREY_800),
                padding=10,
                border_radius=5,
                expand=True,
                alignment=ft.alignment.top_left,
            ),
        ],
    )

    main_row = ft.Row(
        [
            navigation_rail,
            ft.VerticalDivider(width=1, color=ft.colors.GREY_800),
            ft.Container(
                content=content_column,
                padding=10,
                expand=True,
            ),
        ],
    )

    main_layout = ft.Container(
        content=main_row,
        expand=True,
        padding=10,
    )

    page.add(main_layout)
    page.update()


ft.app(target=main)
