import flet as ft


class Controller:
    def __init__(self, page: ft.Page, model):
        self.page = page
        self.model = model
        self.settings()

    def settings(self):
        self.file_picker = ft.FilePicker(
            on_result=self.pick_files_result,
        )
        self.save_file_dialog = ft.FilePicker(
            on_result=self.save_file_result,
        )
        self.page.overlay.extend([self.file_picker, self.save_file_dialog])

    def set_views(
        self,
        layout_view,
        login_view,
        register_view,
        pdf_management_view,
        merge_screen,
        part_screen,
        image_to_pdf_screen,
        pdf_to_image_screen,
    ):
        # pylint: disable=attribute-defined-outside-init
        self.layout_view = layout_view

        self.login_view = login_view
        self.register_view = register_view

        self.pdf_management_view = pdf_management_view
        self.merge_screen = merge_screen
        self.part_screen = part_screen
        self.image_to_pdf_screen = image_to_pdf_screen
        self.pdf_to_image_screen = pdf_to_image_screen

    def login(self, username, password):
        print(username, password)
        self.navigation_route("/home")

    def register(self, username, password, confirm_password):
        print(username, password, confirm_password)
        self.navigation_route("/home")

    def logout(self):
        self.navigation_route("/login")

    def navigation_route(self, index):
        route_map = {
            "/login": self.login_view.login_layout,
            "/register": self.register_view.register_layout,
            "/home": self.pdf_management_view.main_layout,
        }

        if index in route_map:
            screen = route_map[index]
            self.layout_view.set_screen(screen)
        else:
            print("Error: Invalid index")

    def navigation_rail(self, index, update_content=True):
        content_map = {
            0: self.merge_screen.content_list,
            1: self.part_screen.content_list,
            2: self.image_to_pdf_screen.content_list,
            3: self.pdf_to_image_screen.content_list,
        }

        content_list = content_map[index]
        self.pdf_management_view.content_column.controls[0].content = content_list[0]
        self.pdf_management_view.content_column.controls[1].content = content_list[1]
        if update_content:
            self.pdf_management_view.content_column.update()

    def save_file(self):
        pdf_files = self.model.list_pdf
        if len(pdf_files) > 1:
            self.save_file_dialog.save_file(
                file_type=ft.FilePickerFileType.CUSTOM,
                allowed_extensions=["pdf"],
                file_name="flet_pdf_merged.pdf",
            )

    def save_file_result(self, event: ft.FilePickerResultEvent):
        if event.path:
            self.model.save_path = event.path
            self.handle_merge_pdf_files()

    def pick_files(self):
        self.file_picker.pick_files(
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["pdf"],
            allow_multiple=True,
        )

    def pick_files_result(self, event: ft.FilePickerResultEvent):
        if event.files:
            for file in event.files:
                pdf_document = self.model.add_pdf(file.name, file.path)

                pdf_document.content = self.merge_screen.create_pdf_card(
                    pdf_document.id, pdf_document.name, pdf_document.preview
                )

                self.model.insert_pdf(pdf_document)

            self.update_pdf_list()

    def handle_remove_pdf(self, event: ft.ControlEvent):
        for file in self.model.list_pdf:
            if file.id == event.control.key:
                self.model.remove_pdf(event.control.key)

        self.update_pdf_list()

    def handle_merge_pdf_files(self):
        self.model.merge_pdf_files()
        self.model.clear_pdf_list()
        self.update_pdf_list()

    def update_pdf_list(self):
        content_list = []
        for file in self.model.list_pdf:
            content_list.append(file.content)

        self.merge_screen.update_central_content_row(content_list)
