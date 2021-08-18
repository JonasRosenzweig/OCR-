from __future__ import print_function
from google.cloud import vision
import io
import os
import pandas as pd
import json
from pdf2image import convert_from_path

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/surface/Desktop/YouWe/OCR Project/fine-sublime-319610-dc80d5c6f639.json"


PATH = 'C:/Users/surface/Desktop/YouWe/OCR Project/Images/PDFs/13370636.pdf'

pages = convert_from_path(PATH, 501)
client = vision.ImageAnnotatorClient()
responses = []

for page in pages:
    page.save('tmp.jpg')
    with io.open('tmp.jpg', 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    print(response.text_annotations)
    i = 0
    for r in response.text_annotations:
        responses.append(response.text_annotations[i].description)
        i += 1
    print(responses)

os.chdir('Responses')
output = open('output.json', 'w')
json.dump(response, output, indent = 6)
output.close()
Table = {'Text': responses}
df = pd.DataFrame(Table)
df.to_csv('responses.csv')


