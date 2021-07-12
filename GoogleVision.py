from __future__ import print_function
from google.cloud import vision
import io
import os
from pdf2image import convert_from_path

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/surface/Desktop/YouWe/OCR Project/fine-sublime-319610-dc80d5c6f639.json"


PATH = 'C:/Users/surface/Desktop/YouWe/OCR Project/Images/13370636.pdf'

pages = convert_from_path(PATH, 501)
client = vision.ImageAnnotatorClient()

for page in pages:
    page.save('tmp.jpg')
    with io.open('tmp.jpg', 'rb') as image_file:
        content = image_file.read()
    os.system('rm tmp.jgp')
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    print(response.text_annotations[0].description)

