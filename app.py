import flet as ft
from controllers._controller import Controller
from models._model import Model

from views._layout import LayoutView

from views.auth.login_screen import LoginScreen
from views.auth.register_screen import RegisterScreen

from views.pdf_management._pdf_management import PdfManagementView
from views.pdf_management.image_to_pdf_screen import ImageToPdfScreen
from views.pdf_management.merge_screen import MergeScreen
from views.pdf_management.part_screen import PartScreen
from views.pdf_management.pdf_to_image_screen import PdfToImageScreen


def main(page: ft.Page):
    model = Model()
    controller = Controller(page, model)

    layout_view = LayoutView(controller)

    login_view = LoginScreen(controller)
    register_view = RegisterScreen(controller)

    pdf_management_view = PdfManagementView(controller)
    merge_screen = MergeScreen(controller)
    part_screen = PartScreen(controller)
    image_to_pdf_screen = ImageToPdfScreen(controller)
    pdf_to_image_screen = PdfToImageScreen(controller)

    controller.set_views(
        layout_view,
        login_view,
        register_view,
        pdf_management_view,
        merge_screen,
        part_screen,
        image_to_pdf_screen,
        pdf_to_image_screen,
    )

    page.title = "FLET PDF"
    page.theme_mode = ft.ThemeMode.DARK

    page.add(layout_view.main_layout)
    controller.navigation_rail(0, False)
    controller.navigation_route("/login")


ft.app(target=main, assets_dir="assets")
