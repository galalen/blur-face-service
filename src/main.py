import os
import cv2
import base64
import numpy as np
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .processing import blur_face

DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

@app.get("/")
async def index(request: Request):
    template = os.path.join(DIR, 'templates/index.html')
    with open(template, 'r') as file:
        html = file.read()
    return HTMLResponse(html)


@app.post("/api/blur")
async def handle_blur(image: UploadFile = File(...)):
    if not image.filename:
        return {"error": "image not provided"}
        
    content = await image.read()
    
    np_arr = np.fromstring(content, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    output = blur_face(img)
    res, im_jpeg = cv2.imencode(".jpeg", output)

    encoded_img = base64.b64encode(im_jpeg.tobytes())
    return {"data": encoded_img}


# Post an encoded image (base64)
class Item(BaseModel):
    image: str

@app.post("/api/blur/encoded")
async def handle_blur(item: Item):
    if not item.image:
        return {"error": "image not provided"}
    
    image = item.image

    if image.startswith("data:image"):
        image = item.image.split("base64,")[1]

    decode_image = base64.b64decode(image)
    np_arr = np.fromstring(decode_image, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    output = blur_face(img)
    res, im_jpeg = cv2.imencode(".jpeg", output)

    encoded_img = base64.b64encode(im_jpeg.tobytes())
    return {"data": encoded_img}
