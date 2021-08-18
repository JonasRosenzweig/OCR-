import pandas as pd
import os, json
from pathlib import Path


TagGunJsonDir = r'C:\Users\surface\Desktop\YouWe\OCR\TagGun\Responses'
GCVJsonDir = r'C:\Users\surface\Desktop\YouWe\OCR\Google Vision\Responses'
file = r'C:\Users\surface\Desktop\YouWe\OCR\TagGun\Responses\output13370636.json'
fileBB = r'C:\Users\surface\Desktop\YouWe\OCR\BilagsBerier\json\response_60627_100.json'
fileBB1 = r'C:\Users\surface\Desktop\YouWe\OCR\BilagsBerier\json\response_60627_1_formatted.json'
path = Path(fileBB1)


def flattenjson(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenjson(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]

    return val


with path.open('r', encoding='utf-8') as file:
    data = json.loads(file.read())
    flattenjson(data, "_")

df = pd.json_normalize(data)
os.chdir(r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output')
df.to_csv('testHuge1.csv', index=False, encoding='utf-8')

