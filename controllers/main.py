import flet as ft


class Controller:
    def __init__(self, page: ft.Page, model):
        self.page = page
        self.model = model
        self.view = None
        self.merge_screen = None
        self.part_screen = None
        self.image_to_pdf_screen = None
        self.pdf_to_image_screen = None
        self.settings()

    def set_views(
        self, view, merge_screen, part_screen, image_to_pdf_screen, pdf_to_image_screen
    ):
        self.view = view
        self.merge_screen = merge_screen
        self.part_screen = part_screen
        self.image_to_pdf_screen = image_to_pdf_screen
        self.pdf_to_image_screen = pdf_to_image_screen

    def settings(self):
        self.file_picker = ft.FilePicker(
            on_result=self.pick_files_result,
        )
        self.save_file_dialog = ft.FilePicker(
            on_result=self.save_file_result,
        )
        self.page.overlay.extend([self.file_picker, self.save_file_dialog])

    def save_file_result(self, event: ft.FilePickerResultEvent):
        if event.path:
            self.model.save_path = event.path
            self.handle_merge_pdf_files()
        else:
            print("Cancelled!!")

    def save_file(self):
        pdf_files = self.model.list_pdf
        if len(pdf_files) > 1:
            self.save_file_dialog.save_file(
                file_type=ft.FilePickerFileType.CUSTOM,
                allowed_extensions=["pdf"],
                file_name="flet_pdf_merged.pdf",
            )
        else:
            print("Select more than one file")

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

                pdf_document.content = self.view.create_pdf_card(
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

    def navigation_rail(self, index):
        content_map = {
            0: self.merge_screen.content_list,
            1: self.part_screen.content_list,
            2: self.image_to_pdf_screen.content_list,
            3: self.pdf_to_image_screen.content_list,
        }

        if index in content_map:
            build = content_map[index]
            self.view.content_column.controls[0].content = build[0]
            self.view.content_column.controls[1].content = build[1]
            self.view.content_column.update()
        else:
            print("Error: Invalid index")
