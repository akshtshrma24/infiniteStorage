from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = open("./templates/index.html", "r").read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return {"filename": file.filename, "file_path": file_path}
