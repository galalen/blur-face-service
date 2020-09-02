import cv2
import base64
import numpy as np
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates

from bluring import blur_face


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/api/blur")
async def handle_blur(image: UploadFile = File(...)):
    if not image.filename:
        return {"error": "image not provided"}
        
    content = await image.read()
    
    np_arr = np.fromstring(content, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    output = await blur_face(img)
    res, im_png = cv2.imencode(".png", output)

    encoded_img = base64.b64encode(im_png.tobytes())
    return {"data": encoded_img}
