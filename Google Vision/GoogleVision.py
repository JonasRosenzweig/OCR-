from __future__ import print_function
from google.cloud import vision
import io
import os
import pandas as pd
import json
from pdf2image import convert_from_path


# get credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/surface/Desktop/YouWe/OCR Project/fine-sublime-319610-dc80d5c6f639.json"
PATH = r'C:\Users\surface\Desktop\YouWe\OCR\BilagsBerier\pdf'

files = os.listdir(PATH)
client = vision.ImageAnnotatorClient()


for j in range(len(files)):
    print(j+1,  'of', (len(files)), "files OCR'd.")
    file = os.listdir(PATH)[j]
    file_path = os.path.join('..', PATH, file)
    pages = convert_from_path(file_path, 501)
    responses = []

    for page in pages:
        page.save('tmp.jpg')
        with io.open('tmp.jpg', 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)
        i = 0

        for r in response.text_annotations:
            responses.append(response.text_annotations[i].description)
            i += 1

    os.chdir(r'C:\Users\surface\Desktop\YouWe\OCR\Google Vision\Responses')
    output = open('{}.txt'.format(file), 'w', encoding='UTF-8')
    output.writelines(responses)
    output.close()
    j -= 1

print("All files OCR'd.")

