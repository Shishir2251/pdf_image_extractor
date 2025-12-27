from PIL import Image
from extractor.ocr import extract_text_from_image


def extract_from_image_file(image_path: str) -> str:
    image = Image.open(image_path)
    return extract_text_from_image(image)
