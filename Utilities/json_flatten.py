import os, json
from pathlib import Path


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


file = r'C:\Users\surface\Desktop\YouWe\OCR\BilagsBerier\json\response_60627_1_formatted.json'
path = Path(file)
os.chdir(r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output')

with path.open('r', encoding='utf-8') as file:
    data = json.loads(file.read())
    flattened_data = flattenjson(data, "__")

with open(' response_60627_1_formatted_flattened.json', 'w') as write_file:
    json.dump(flattened_data, write_file, sort_keys=True, indent=4)
