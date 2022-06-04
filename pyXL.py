#pip install pillow
#pip install openpyxl

from openpyxl import load_workbook


wb = load_workbook(filename="PM Books.xlsm")
ws = wb.active
cellCheck = ws["B4"].value

print(ws.title)
print(cellCheck)