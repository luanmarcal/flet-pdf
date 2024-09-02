import flet as ft


class LayoutView:
    def __init__(self, controller):
        self.controller = controller
        self.main_layout = self.build()

    def set_screen(self, screen: list):
        self.main_row.controls = screen
        self.main_row.update()

    def build(self):

        self.main_row = ft.Row(
            [],
        )

        self.main_layout = ft.Container(
            content=self.main_row,
            expand=True,
            padding=10,
        )

        return self.main_layout
