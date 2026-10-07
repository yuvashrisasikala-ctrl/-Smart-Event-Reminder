import pytesseract
import os


if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
else:
    pytesseract.pytesseract.tesseract_cmd = "tesseract"


def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text