import pandas as pd
import os, csv

import pandas.errors

OCR_PATH = r'C:\Users\surface\Desktop\YouWe\OCR\Google Vision\Responses'
Output = r'C:\Users\surface\Desktop\YouWe\OCR\Utilities\output\Training Data'
OCR_files = os.listdir(OCR_PATH)

for i in range(len(OCR_files)):
    try:
        os.chdir(OCR_PATH)
        file = OCR_files[i]
        print(file)
        df = pd.read_csv(file, delimiter='\t', header=None)
        df.columns = ['Data']
        data = ' '.join(df['Data'])
        df1 = pd.DataFrame()
        df1.at[0, 0] = data
        df1.columns = ['OCR Output']
        os.chdir(Output)
        df1.to_csv('{}.csv'.format(os.path.splitext(file)[0]), index=False, encoding='utf-16')
    except pandas.errors.EmptyDataError:
        pass
    except TypeError:
        pass


# df = pd.read_csv(r'C:\Users\surface\Desktop\YouWe\OCR\Google Vision\Responses\Invoice.13370636.pdf.txt',
#                  delimiter='\t', header=None)
# df.columns = ['Data']
# data = ''.join(df['Data'])
# print(data)
# df1 = pd.DataFrame()
# df1.at[0, 0] = data
# df1.columns = ['OCR Output']
# df1.to_csv('out.csv', index=False, encoding='utf-16')
