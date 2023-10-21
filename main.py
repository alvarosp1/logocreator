from fastapi import FastAPI, Response
from pydantic import BaseModel
import requests
import io
from PIL import Image
from starlette.responses import StreamingResponse

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/artificialguybr/LogoRedmond-LogoLoraForSDXL"
headers = {"Authorization": "Bearer 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"}

class Item(BaseModel):
    inputs: str

@app.post("/query/", response_class=Response)
async def create_query(item: Item):
    response = requests.post(API_URL, headers=headers, json=item.dict())
    image_bytes = response.content

    image = Image.open(io.BytesIO(image_bytes))
    
    # Convierte la imagen en un objeto de archivo en memoria
    file_like = io.BytesIO()
    image.save(file_like, format='PNG')
    file_like.seek(0)

    return StreamingResponse(file_like, media_type="image/png")
