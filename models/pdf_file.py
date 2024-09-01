import uuid
import fitz


class PDFFile:
    def __init__(self, name: str, path: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.path = path
        self.preview = self.generate_preview(self.id, path)
        self.content = None

    def generate_preview(self, preview_id: str, path: str):
        pdf_document = fitz.open(path)
        page = pdf_document.load_page(0)

        zoom_x = 150 / page.rect.width
        zoom_y = 200 / page.rect.height
        matrix = fitz.Matrix(zoom_x, zoom_y)

        pix = page.get_pixmap(matrix=matrix, alpha=False)
        preview_image_path = f"./assets/temp/preview_{preview_id}.png"
        pix.save(preview_image_path)

        pdf_document.close()
        return preview_image_path
