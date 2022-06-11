#pip install pillow
#pip install openpyxl

from openpyxl import load_workbook

def fromPMBooks(): #This will strip the PM Books for equipment name/number, task info, and frequence
    wb = load_workbook(filename="PM Books.xlsm")
    ws = wb.active

    eqArr = []
    taskArr = []
    freqArr = [] #THESE THREE ARRAYS will eventually be stacked into a single array like this: fourKey = np.stack((fcArr, finPrioArr, taskArr), axis=1)

    exCounter = 0   #DITCH this, add a statement to first IF... AND len(eqArr) < 100 
                    #The point of this is to meet limble's PM import maximum of 100 tasks

    for ws in wb.worksheets:

        if "BOOK" in ws.title or "Support 1" in ws.title or "Support 2" in ws.title:

            print(ws.title)
            initialCell = 0
            finCell = 0
###PROBABLY change this to a loop through Range(3(wherever FREQ is) to len(ws['c'])
            for index, cell in enumerate(ws['C']):
                
                print(cell.value)
                if cell.value is None and initialCell == 0:
                    initialCell = index 
                    

                elif cell.value is None and initialCell != 0:
                    initialCell = initialCell + 1
                    finCell = index
                    print(finCell)

                    eqFind = "B" + str(initialCell)
                    eqRaw = ws[eqFind].value
                    print(eqRaw)

                    
                    #initialCell - 1 of B is Equipment RAW, ad
                    #from initialCell to finCell, add to array Bi, Ci, and EqRaw(for every i)
                    initialCell = finCell 

                    #Loop from initialCell to finCell over column B and D
                    #build array as [equipment..., task, freq]

                    #ALL NEEDS TO END WHEN ARRAY has 100 entries (due to the import limitation of LIMBLE)

                    #THIS NEEDS TO END with  initialCell = 0 and finCell = 0
                    """ cell.value == "FREQ":
                    initialCell = index
                    print("1 - initialCell - " ) """



                #END if-cell "FREQ"

            #END for-cells    

        #END if-"BOOK"-ws.title    

    #END for-ws-wb.worksheets
    pmbArr = -9
    buildImportSheet(pmbArr)
    #END fromPMBooks()

def buildImportSheet(pmbArr):
    print("nothing")
    #END buildImportSheets()

fromPMBooks()