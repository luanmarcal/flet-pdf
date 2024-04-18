import flet as ft
from controllers.image_controller import ImageController

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK

    page.update()


ft.app(main)
