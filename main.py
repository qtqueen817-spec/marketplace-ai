from fastapi import File, UploadFile
import shutil

@app.post("/items/{item_id}/upload-image")
async def upload_item_image(item_id: int, file: UploadFile = File(...)):
    # Define where to save the image
    file_path = f"static/images/{item_id}_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"filename": file.filename, "status": "Image uploaded successfully"}