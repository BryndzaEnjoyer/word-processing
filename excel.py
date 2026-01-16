import openpyxl as xl
from config import get_data_file_path
path=get_data_file_path('Výpočty a filtrovanie.xlsx')

wb = xl.load_workbook(path)
print(wb.sheetnames)

def select_sheet(x):

    wb._active_sheet_index = x
    print("Active sheet: ", wb.active)
    sheet_obj = wb.active
    row = sheet_obj.max_row
    column = sheet_obj.max_column

    print("\nValue of first column")
    for i in range(1, row + 1):
        cell_obj = sheet_obj.cell(row=i, column=1)
        print(cell_obj.value)

    print("\nValue of first row")
    for i in range(1, column + 1):
        cell_obj = sheet_obj.cell(row=2, column=i)
        print(cell_obj.value, end=" ")

y=int(input("select a sheet number:"))
select_sheet(y)
