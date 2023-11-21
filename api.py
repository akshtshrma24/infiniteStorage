from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Serve static files (like stylesheets) from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Use Jinja2 for HTML templates
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

# Directory to store uploaded files
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Save the file to the uploads directory
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as f:
        f.write(file.file.read())

    return {"filename": file.filename, "file_path": str(file_path)}
