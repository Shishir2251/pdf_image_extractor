import pytesseract
from PIL import Image
import cv2
import numpy as np


def preprocess_image(image: Image.Image) -> Image.Image:
    """Improve image quality for OCR"""
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)[1]
    return Image.fromarray(img)


def extract_text_from_image(image: Image.Image) -> str:
    image = preprocess_image(image)
    return pytesseract.image_to_string(image)
