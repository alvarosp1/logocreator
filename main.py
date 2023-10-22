from fastapi import FastAPI, Response
from pydantic import BaseModel
import requests
import io
from PIL import Image
from starlette.responses import StreamingResponse
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os
from typing import Dict, Any

load_dotenv() 

cloudinary.config( 
  cloud_name = os.getenv("CLOUD_NAME"), 
  api_key = os.getenv("API_KEY"), 
  api_secret = os.getenv("API_SECRET") 
)

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/artificialguybr/LogoRedmond-LogoLoraForSDXL"
headers = {"Authorization": os.getenv("API_IMAGE") }

class Item(BaseModel):
    inputs: str

@app.post("/query/", response_model=Dict[str, Any])
async def create_query(item: Item):
    response = requests.post(API_URL, headers=headers, json=item.dict())
    image_bytes = response.content

    image = Image.open(io.BytesIO(image_bytes))
    
    # Convierte la imagen en un objeto de archivo en memoria
    file_like = io.BytesIO()
    image.save(file_like, format='PNG')
    file_like.seek(0)
    
    upload_result = cloudinary.uploader.upload(file_like)
    
    # Devuelve la URL de la imagen
    return {"url": upload_result['url']}
