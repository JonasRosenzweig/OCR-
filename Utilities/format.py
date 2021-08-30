import io

import pandas as pd
import os, csv

OCR_PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Google Vision\Responses'
CSV_PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Oumar\csv'
Output = r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output\Training Data'
OCR_files = os.listdir(OCR_PATH)
CSV_files = os.listdir(CSV_PATH)

df = pd.read_csv(r'C:\Users\surface\Desktop\YouWe\OCR\Google Vision\Responses\Invoice.13370636.pdf.txt',
                 delimiter='\t', header=None)
df.columns = ['Data']
data = ''.join(df['Data'])
print(data)
df1 = pd.DataFrame()
df1.at[0,0]=data
df1.columns=['OCR Output']
df1.to_csv('out.csv', index=False, encoding='utf-16')
