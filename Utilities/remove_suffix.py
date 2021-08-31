from pathlib import Path
import os

DIR = r'C:\Users\surface\Desktop\YouWe\OCR\Google Vision\Responses'
files = os.listdir(DIR)
os.chdir(DIR)

for i in range(len(files)):
    file = files[i]
    new_name = file[:-8]
    os.rename(file, new_name + '.txt')
print('done renaming!')




