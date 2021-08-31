import pandas as pd
import os, csv

CSV_PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Oumar\csv'
Output = r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output\Training Data\Reformated csv'
CSV_files = os.listdir(CSV_PATH)

for i in range(len(CSV_files)):
    os.chdir(CSV_PATH)
    file = CSV_files[i]
    print(file)
    df = pd.read_csv(file, index_col=0, skiprows=[0])
    df = df.transpose()
    os.chdir(Output)
    df.to_csv('{}'.format(file), index=None, encoding='utf-8')

# os.chdir(CSV_PATH)
# file = r'C:\Users\surface\Desktop\YouWe\OCR\Oumar\csv\Invoice.13370636.csv'
# df = pd.read_csv(file, index_col=0, skiprows=[0])
# print(df)
# df = df.transpose()
# print(df)
# os.chdir(Output)
# df.to_csv('test.csv', index=None, encoding='utf-16')
