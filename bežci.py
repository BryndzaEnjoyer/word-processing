import pandas as pd
import numpy as np
import openpyxl as xl

from config import get_data_file_path

path=get_data_file_path('TEST_tabuľkovy kalkulátor_ZDROJE_B - Copy.xlsx')
wb = xl.load_workbook(path, data_only = True)
data= pd.DataFrame(wb.active.values)

katfre={}
kat= data[5]
kats=["A","B","C","D"]
for i in kats:
    a = (kat == i).sum()
    katfre[i]=a
    
def umiestnenie(p,um):
    return kat[kat[p]==um]

women=data[6][data[6]=="Z"]

print(women)
