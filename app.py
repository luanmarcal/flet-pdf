import flet as ft
from controllers.main import Controller
from models.main import Model

from views.main import MainView
from views.image_to_pdf_screen import ImageToPdfScreen
from views.pdf_to_image_screen import PdfToImageScreen
from views.part_screen import PartScreen
from views.merge_screen import MergeScreen


def main(page: ft.Page):
    model = Model()
    controller = Controller(page, model)

    view = MainView(controller)
    merge_screen = MergeScreen(controller)
    part_screen = PartScreen(controller)
    image_to_pdf_screen = ImageToPdfScreen(controller)
    pdf_to_image_screen = PdfToImageScreen(controller)

    controller.set_views(
        view, merge_screen, part_screen, image_to_pdf_screen, pdf_to_image_screen
    )

    page.title = "Flet PDF"
    page.theme_mode = ft.ThemeMode.DARK

    page.add(view.main_layout)
    controller.navigation_rail(0)


ft.app(target=main)
