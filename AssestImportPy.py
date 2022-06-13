# - THIS IS WHAT IS NEXT - ##############
""" 
6.13 - Just starting off! Pulling and sorting data from assetsRaw.xlsx into Sample Asset Import.xlsx
 """
#########################################

from tkinter.font import names
import numpy as np
import re
from openpyxl import load_workbook

def eqNameBuild(): #pull info from assetsRaw to build array of equipNum - AssetName, Format Example: "964 - North Elevator"
    #
    namesArr = []
    makeArr = []
    modelArr = []
    serialArr = []
    shortParentArr = []
    parentArr = []

    wb = load_workbook(filename="assetsRaw.xlsx")
    ws = wb["Asset"]

    for i, cell in enumerate(ws["A"]):
        if cell.value != "Asset Name":
            z = i + 1
            eqName = "A" + str(z)
            #print(eqName)
            #print(ws[eqName].value)
            longACode = "B" + str(z)
            longPCode = "H" + str(z)

            x = ws[longACode].value.rsplit("-")
            #print(x)

            parent = (x[((len(x) - 2))])
            eqNum = (x[((len(x) - 1))])
            #print(eqNum)

            if len(x) > 3 and eqName != "A602" and eqNum[3:].isalpha():
                eqNum = eqNum[:3]
            elif len(x) > 3 and eqName != "A602" and eqNum[:1].isalpha():
                parent = (x[((len(x) - 3))])
                eqNum = (x[((len(x) - 2))])
                eqNum = eqNum[:3]
            #END EQNUM    

            finName = eqNum + " - " + ws[eqName].value
            #print(finName)

            namesArr.append(finName)
            parentArr.append(parent)
            make = "D" + str(z)
            makeArr.append(ws[make].value)
            model = "E" + str(z)
            modelArr.append(ws[model].value)
            serial = "F" + str(z)
            serialArr.append(ws[serial].value)

            #
        #END IF CELL.VALUE
    #END FOR-Z

    for j, eqNom in enumerate(namesArr): #get fpn (full parent name) from parent by matching to namesArr[:3]
        print(eqNom)
        for k, parr in enumerate(parentArr):
            if eqNom[:(len(parr))] == parr:
                parentArr[k] = (eqNom)
                print(eqNom)
            #END IF-EQNOM
        #END FOR-K
    #END FOR-J

    print(parentArr)
    #print(len(namesArr))
#END eqNameBuild()

eqNameBuild()