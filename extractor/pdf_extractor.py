import fitz  # PyMuPDF
from PIL import Image
from extractor.ocr import extract_text_from_image


def is_scanned_pdf(doc: fitz.Document) -> bool:
    """Check if PDF has no extractable text"""
    for page in doc:
        if page.get_text().strip():
            return False
    return True


def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""

    if not is_scanned_pdf(doc):
        # Text-based PDF
        for page in doc:
            text += page.get_text()
        return text

    # Scanned PDF → OCR
    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text += extract_text_from_image(img)

    return text
