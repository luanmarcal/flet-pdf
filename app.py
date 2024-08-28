import flet as ft
from controllers.main import Controller
from views.main import MainView
from models.main import Model


def main(page: ft.Page):
    model = Model()
    controller = Controller(page, model)
    view = MainView(controller)
    controller.set_view(view)

    page.title = "Flet PDF"
    page.theme_mode = ft.ThemeMode.DARK

    page.add(view.build())


ft.app(target=main)
