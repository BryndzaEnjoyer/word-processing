import openpyxl as xl
from config import get_data_file_path
import pandas as pd
import numpy as np
from pathlib import Path



path=get_data_file_path('TEST_tabuľkovy kalkulátor_ZDROJE_B - Copy.xlsx')

path2=Path("data/raw") / "ulohy"
print(path2)

wb = pd.read_excel(path)

df = pd.DataFrame(wb)
print(df)



for i in path2.iterdir():
    wb2 = pd.read_excel(i)
    df2 = pd.DataFrame(wb2)
    #compare them
