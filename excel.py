import openpyxl as xl
from config import get_data_file_path
import data_frame_functions as dff
import excel as ex
import pandas as pd

path=get_data_file_path('Výpočty a filtrovanie.xlsx')

wb = xl.load_workbook(path)
print(wb.sheetnames)


def select_sheet(x):
    wb._active_sheet_index = x
    print("Active sheet: ", wb.active)
    sheet_obj = wb.active
    row = sheet_obj.max_row
    column = sheet_obj.max_column
  
    all_values = []
    for i in range(1, row + 1):
        row_values = []
        for j in range(1, column + 1):
            cell_obj = sheet_obj.cell(row=i, column=j)
            row_values.append(cell_obj.value)
        all_values.append(row_values)

    return all_values

y=int(input("select a sheet number:"))

table = pd.DataFrame(select_sheet(y))
print(table)
A=dff.read_collumn("A")
B=dff.read_collumn("B")
collumn2=dff.summation(A,B)
print(collumn2)