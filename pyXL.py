#pip install pillow
#pip install openpyxl

from openpyxl import load_workbook

def fromPMBooks(): #This will strip the PM Books for equipment name/number, task info, and frequence
    wb = load_workbook(filename="PM Books.xlsm")
    ws = wb.active

    exCounter = 0

    for ws in wb.worksheets:

        if "BOOK" in ws.title or "Support 1" in ws.title or "Support 2" in ws.title:

            print(ws.title)
            initialCell = 0
            finCell = 0

            for index, cell in enumerate(ws['C']):
                
                print(cell.value)
                if cell.value == "FREQ":
                    initialCell = index
                    print("1 - initialCell - " % initialCell)

                elif cell.value == "None" and initialCell == 0:
                    initialCell = index
                    print("1 - initialCell - " % initialCell)

                elif cell.value == "None" and initialCell != 0:
                    print("1 - initialCell - " % initialCell)
                    finCell = index

                    #Loop from initialCell to finCell over column B and D
                    #build array as [equipment..., task, freq]

                    #ALL NEEDS TO END WHEN ARRAY has 100 entries (due to the import limitation of LIMBLE)

                    #THIS NEEDS TO END with  initialCell = 0 and finCell = 0



                #END if-cell "FREQ"

            #END for-cells    

        #END if-"BOOK"-ws.title    

    #END for-ws-wb.worksheets
    buildImportSheet(pmbArr)
    #END fromPMBooks()

def buildImportSheet(pmbArr):

    #END buildImportSheets()
