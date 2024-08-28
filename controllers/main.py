import flet as ft


class Controller:
    def __init__(self, page, model):
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
        self.page.overlay.append(self.file_picker)

    def pick_files(self, event=None):
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

    def handle_remove_pdf(self, event):
        for file in self.model.list_pdf:
            if file.id == event.control.key:
                self.model.remove_pdf(event.control.key)

        self.update_pdf_list()

    def handle_merge_pdf_files(self, e=None):
        self.model.merge_pdf_files()
        self.update_pdf_list()

    def update_pdf_list(self):
        content_list = []
        for file in self.model.list_pdf:
            content_list.append(file.content)

        self.view.update_central_content_row(content_list)
