import pandas as pd
import os

PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Oumar\csv'
SAVEPATH = r'C:\Users\surface\Desktop\YouWe\OCR\Oumar\Extracted Data'

list_files = os.listdir(PATH)
print("Extracting Voucher IDs from all files in", PATH)

i = 0
voucher_IDs = []
for j in range(len(list_files)):
    print(i + len(list_files),  'of', (len(list_files)), "files remaining.")
    dataset_filename = os.listdir(PATH)[j]
    dataset_path = os.path.join("../..", PATH, dataset_filename)
    df = pd.read_csv(dataset_path, error_bad_lines=False, engine='c', encoding="ISO-8859-1", low_memory=False)
    data = df['Data']
    voucher_IDs.append(data[0])
    i -= 1

os.chdir(SAVEPATH)
Voucher_IDs_text = open('Voucher_IDs_Full.txt', 'w')
for e in voucher_IDs:
    Voucher_IDs_text.write(e + '\n')
Voucher_IDs_text.close()
