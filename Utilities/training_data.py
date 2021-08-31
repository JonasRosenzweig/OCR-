import pandas as pd
import os, csv

CSV_PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output\Training Data\Reformated csv'
CSV_files = os.listdir(CSV_PATH)
OCR_PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output\Training Data\Reformated ocr'
OCR_files = os.listdir(OCR_PATH)
OUT_PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output\Training Data'

c = 0
k = 1
for i in range(len(OCR_files)):
    ocr_file = OCR_files[i]
    csv_file = CSV_files[k]
    if ocr_file == csv_file:
        c+=1
        print('match!', c)
        k+=1
        os.chdir(OCR_PATH)
        df_ocr = pd.read_csv(ocr_file, header=None, encoding='ISO-8859-1', sep='/t')
        os.chdir(CSV_PATH)
        df_csv = pd.read_csv(csv_file, header=0, encoding='ISO-8859-1', sep=',')
        df_join = df_ocr.join(df_csv)
        os.chdir(OUT_PATH)
        df_join.to_csv('{}.csv'.format(os.path.splitext(ocr_file)[0]), index=False, encoding='ISO-8859-1')
    elif ocr_file != csv_file:
        print(csv_file, ocr_file)
        k+=2
print(c)
