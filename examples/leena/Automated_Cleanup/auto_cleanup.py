#Automated Cleanup and Archival Script
import os
import shutil
import time
import tarfile
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

directory = '/home/user/downloads'
archives_directory = '/home/user/downloads/Archives'

subdirectories = ['Documents', 'Images', 'Script', 'Text', 'Others']

def organize_files(): 
    # Create subdirectories if they don't exist
    for subdirectory in subdirectories:
        if not os.path.exists(directory + '/' + subdirectory):
            os.makedirs(directory + '/' + subdirectory)

    for file in os.listdir(directory):
        if file.endswith('.pdf') or file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt'):
            shutil.move(directory + '/' + file, directory + '/Documents')
        elif file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            shutil.move(directory + '/' + file, directory + '/Images')
        elif file.endswith('.py') or file.endswith('.sh') or file.endswith('.js'):
            shutil.move(directory + '/' + file, directory + '/Script')
        elif file.endswith('.txt'):
            shutil.move(directory + '/' + file, directory + '/Text')
        else:
            shutil.move(directory + '/' + file, directory + '/Others')

#Automatically archives old files older than 7 days
def Automatically_archives_old_files():
    archive_name = f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz"
    archive_path = os.path.join(archives_directory, archive_name)
    cutoff_time = time.time() - 7 * 86400  
    tar = tarfile.open(archive_path, "w:gz")
    for subdir, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(subdir, file)
            if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff_time:
                tar.add(file_path, arcname=os.path.relpath(file_path, directory))
                os.remove(file_path)
    tar.close()

#Automatically deletes archives older than 30 days
def Automatically_deletes_old_archives():
    cutoff_time = time.time() - 30 * 86400  # 30 days in seconds
    for file in os.listdir(archives_directory):
        if file.endswith('.tar.gz') and os.path.getmtime(archives_directory + '/' + file) < cutoff_time:
            os.remove(archives_directory + '/' + file)
    


#Automated Cleanup and Archival Script
@app.post("/organize")
def organize():
    organize_files()
    return JSONResponse(content={"message": "Files organized successfully"}, status_code=200)

@app.post("/archive")
def archive():
    automatically_archives_old_files()
    return JSONResponse(content={"message": "Old files archived successfully"}, status_code=200)

@app.post("/cleanup")
def cleanup():
    delete_old_archives()
    return JSONResponse(content={"message": "Old archives deleted successfully"}, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    