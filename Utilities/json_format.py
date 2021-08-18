import json, os
from pathlib import Path

# format Json for nice formatting

file = r'C:\Users\surface\Desktop\YouWe\OCR\BilagsBerier\json\response_60627_100.json'
path = Path(file)

with path.open('r', encoding='utf-8') as file:
    data = json.loads(file.read())

os.chdir(r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output')

with open(' response_60627_100_formatted_2.json', 'w') as write_file:
    json.dump(data, write_file, sort_keys=True, indent=3)

