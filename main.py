from fastapi import FastAPI, Response
from pydantic import BaseModel
import requests
import io
from PIL import Image
import matplotlib.pyplot as plt
from starlette.responses import StreamingResponse
from datetime import datetime

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
    
    # Genera un nombre de archivo único utilizando la hora actual
    filename = "output_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    image.save(filename)  # Guarda la imagen en el servidor local

    file_like = open(filename, mode="rb")
    return StreamingResponse(file_like, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
