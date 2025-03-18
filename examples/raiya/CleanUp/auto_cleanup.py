import os
import shutil
import time
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

path = "/home/user/downloads"
archive_path = "/home/user/downloads/archive"
extensions = {
    "pdf": "pdf_files",
    "txt": "text_files",
    "jpg": "image_files",
    "py": "python_files",
}

def move_files():
    for file in os.listdir(path):
        file_extension = file.split('.')[-1]
        if file_extension in extensions:
            dest_dir = os.path.join(path, extensions[file_extension])
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(os.path.join(path, file), os.path.join(dest_dir, file))

def archive_files():
    current_time = time.time()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if current_time - os.path.getmtime(file_path) > 604800:
            archive_name = os.path.join(archive_path, "archived_" + time.strftime("%Y%m%d"))
            shutil.make_archive(archive_name, "gztar", path, file)
            os.remove(file_path)

def delete_files():
    current_time = time.time()
    for file in os.listdir(archive_path):
        file_path = os.path.join(archive_path, file)
        if current_time - os.path.getmtime(file_path) > 2592000:
            os.remove(file_path)

@app.post('/move_files')
def move_files_endpoint():
    move_files()
    return JSONResponse(content={"message": "Files moved successfully"}, status_code=200)

@app.post('/archive_files')
def archive_files_endpoint():
    archive_files()
    return JSONResponse(content={"message": "Files archived successfully"}, status_code=200)

@app.post('/delete_files')
def delete_files_endpoint():
    delete_files()
    return JSONResponse(content={"message": "Archived files deleted successfully"}, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
