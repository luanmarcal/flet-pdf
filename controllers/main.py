import flet as ft


class Controller:
    def __init__(self, page: ft.Page, model):
        self.page = page
        self.model = model
        self.view = None
        self.settings()

    def set_view(self, view):
        self.view = view

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

        self.view.update_central_content_row(content_list)
