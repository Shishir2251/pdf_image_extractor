from extractor.pdf_extractor import extract_text_from_pdf
from extractor.image_extractor import extract_from_image_file
from utils.file_utils import get_file_extension


def extract_text(file_path: str) -> str:
    ext = get_file_extension(file_path)

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)

    if ext in [".jpg", ".jpeg", ".png"]:
        return extract_from_image_file(file_path)

    raise ValueError("Unsupported file format")


if __name__ == "__main__":
    file_path = "C:/Users/shish/OneDrive/Pictures/Task 2 .png"  # change this
    text = extract_text(file_path)
    print(text)
