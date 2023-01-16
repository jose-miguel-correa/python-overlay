from fastapi import APIRouter, Form, UploadFile, File
from azure_blob_functions.blob import get_blob, upload_blob, download_blob, delete_blob

blob_routes = APIRouter()

@blob_routes.post("/upload")
async def upload(container: str = Form(...), file: UploadFile = File(...)):
    data = await file.read()
    filename = file.filename
    return upload_blob(filename, container, data)

@blob_routes.get("/file/{container}/{filename}")
def get_file(container: str, filename: str):
    return get_blob(filename, container)

@blob_routes.get("/download/{container}/{filename}")
def download_file(container: str, filename: str):
    return download_blob(filename, container)

@blob_routes.delete("/delete")
def delete_file(container: str = Form(...), filename: str = Form(...)):
    return delete_blob(filename, container)