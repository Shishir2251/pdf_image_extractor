from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
import uuid

from extractor.pdf_extractor import extract_text_from_pdf
from extractor.image_extractor import extract_from_image_file
from utils.file_utils import get_file_extension

app = FastAPI(title="PDF & Image OCR API")

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)


@app.post("/extract-text")
async def extract_text_api(file: UploadFile = File(...)):
    ext = get_file_extension(file.filename)

    if ext not in [".pdf", ".jpg", ".jpeg", ".png"]:
        raise HTTPException(status_code=400, detail="Unsupported file format")

    temp_filename = f"{uuid.uuid4()}{ext}"
    temp_path = os.path.join(TEMP_DIR, temp_filename)

    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if ext == ".pdf":
            text = extract_text_from_pdf(temp_path)
        else:
            text = extract_from_image_file(temp_path)

        return {
            "filename": file.filename,
            "text": text.strip()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
