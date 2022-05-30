#INTEGRATES with ApiPython002.py AND ApiPython003-1.py
import time
import http.client
import json
from http.client import HTTPSConnection
from base64 import b64encode
from json import dumps, loads
from pprint import pprint
import numpy as np

def FCA2Priorites(taskArr, fcArr):
    ratioVariable = 10  #This number determines the distribution of priority levels
                        #[length of list of tasks] // ratioVariable => 
                        #IF ratiovariable = 20 AND len(taskList) = 100,
                        #THEN the 5 priority levels will be divided into...
                        #rtnartnsxfgnxertnsfxgntxfgns
    prioArr = []
    pcSync = []
    nzFcArr = []
    finPrioArr = []
    nzFcArri = np.array(nzFcArr)
    fcArri = np.array(fcArr)

    #print(fcArri)

    for n in fcArri:
        if n != 0:  # START IF--1
            nzFcArr.append(n)
            #END IF--1
        #END for-n

    nzFcArri = np.unique(np.sort(fcArr)) #every task's Filter Code, in ascending order
    print(nzFcArri)

    nzL = len(fcArr)    #####  len(nzFcArri)  THIS WILL NOT continue to work. There will eventually be 
                        #####hundreds of tasks(=> filter codes). Dividing them into 5 equal Priority categories will not be effective
                        #####nzFcArri is an ascending list of Filter Codes. Take the top 50 or top 10% and divide those into 5 Priorities
    """ 
    if (0 in fcArri) == False:### if len(fcArri) == nzL:  # START IF--2  #No Zeros; 5 Priority Levels
        #print("No Zeros")
        nzChops = nzL // ratioVariable
        #print(nzChops)
        b = 0
        # builds an array of equal length to nzFcArri(the non-zero filter codes), assigning priority numbers to the filtercodes
        while b < nzL:
            if b <= nzChops:
                prioArr.append(1)
            elif nzChops <= b < (nzChops * 2):
                prioArr.append(2)
            elif (nzChops * 2) <= b < (nzChops * 3):
                prioArr.append(3)
            elif (nzChops * 3) <= b < (nzChops * 4):
                prioArr.append(4)
            else:
                prioArr.append(5)
            #END while-b 1

        #prioArri = np.array(prioArr)

        #for through fcArr, if fcArr(w) = 0 then finPrioArr.append(5)
        for unorderedFc in fcArr:  # START for-unorderedFc
            w = 0
            while w != -9:  # START Priority Seeker 1
                prSeek = nzFcArri[w]
                prMatch = prioArr[w]
                if prSeek == unorderedFc:  # START if/else-prSeek
                    finPrioArr.append(prMatch)
                    w = -9
                else:
                    w += 1
                    #END if/else-prSeek
                #END Priority Seeker 1

    else:  # ZEROs are present in fcArri; 4 Priority Levels (+ Zero = Level 5)
        #print("Zeros Exist")
        nzChops = nzL // ratioVariable
        print(nzChops)
        b = 0
        # builds an array of equal length to nzFcArri(the non-zero filter codes), assigning priority numbers to the filtercodes
        while b < nzL:
            if b <= nzChops:
                prioArr.append(2)
            elif nzChops <= b < (nzChops * 2):
                prioArr.append(3)
            elif (nzChops * 2) <= b < (nzChops * 3):
                prioArr.append(4)
            else:
                prioArr.append(5)

                #END IF--b<nzChops
            b += 1
            #END while-b 2
        prioArri = np.array(prioArr)

        #for through fcArr, if fcArr(w) = 0 then finPrioArr.append(5)
        for unorderedFc in fcArr:  # START for-unorderedFc
            if unorderedFc == 0:  # START if-zero check2
                finPrioArr.append(1)
            else:  # START else-zero check 2
                w = 0
                while w != -9:  # START Priority Seeker 2  ###### -9 is arbitrary, wanted to use a while loop for no particular reason, don't judge.
                    prSeek = nzFcArri[w]
                    prMatch = prioArr[w]
                    if prSeek == unorderedFc:  # START if/else-prSeek
                        finPrioArr.append(prMatch)
                        w = -9 #arbitrary
                    else:
                        w += 1
                        #END if/else-prSeek
                    #END Priority Seeker 2
                #END else-zero check 2
                #END if-zero check 2
            #END for-unorderedFc

        #else, forloop nzFcArri looking to match value of fcArr(w)
        #if matched, get the position of nzFcArri, apply same position to prioArri, finPrioArr.append(prioArr(whatev position))

        #END IF--2 """
        ###THIS is trash
    """ #THIS needs to work for a task list that can be up to 1000 tasks long.
    # filter codes can range rom 0-125
    #

    if len(nzFcArri) < 20:
        x = 6
    else:
        x = len(nzFcArri) // 10
    #END IF len(nz...)
    i = 1
    while i < x:
        
    #END FOR-i, j """
    #end trash

    ones = 0
    twos = 15
    threes = 30
    fours = 50

    for i in fcArr:
        fcChecking = i
        if fcChecking == 0:
            finPrioArr.append("1")
        elif fcChecking < twos:
            finPrioArr.append("2")
        elif fcChecking < threes:
            finPrioArr.append("3")    
        elif fcChecking < fours:
            finPrioArr.append("4")
        else:
            finPrioArr.append("5")
        #END if-fcChecking
    #END for-i        

    fourKey = np.stack((fcArr, finPrioArr, taskArr), axis=1)  # DONT NEED?
    #print(fourKey)

    update_FC(taskArr, finPrioArr)

    return(print(fourKey))

def update_FC(taskArr, finPrioArr): #THIS SHOULD BE THE LAST STEP - sending the API/Update with new Priority Levels
    #PRIid = 2   #temp trash
    #taskID = 59 #temp trash

    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    userAndPass = b64encode(b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")
    headers = {
        'Authorization': 'Basic %s' % userAndPass,
        'Content-Type': 'application/json'
        }

    for i, taskID in enumerate(taskArr):
        #print("priority - " + str(finPrioArr[i]))
        #print("iD - " + str(taskID))
        PRIid = finPrioArr[i]

        payload = json.dumps({
            "priority": PRIid
        })

        conn.request("PATCH", "/v2/tasks/"+ str(taskID), payload, headers)
        res = conn.getresponse()
        data = res.read()
        #print(data.decode("utf-8"))

    #END FOR-taskID

    return(print("GOODBYE"))

def calc_filterCode(risk, sev, pdc):
    bigFC = int(risk) * int(sev) * int(pdc)
    #bigFC = 777
    return int(bigFC)

def find_risk(etID):
    #print(etID)
    riskOut = 0
    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
        'assetID': ''
    }
    #goJuice = "/v2/assets/fields/?assets=" + str(etID) + "&fields=7&limit=10"

    conn.request(
        "GET", "/v2/assets/fields/?assets=" + str(etID) + "&fields=6&limit=10", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)

    for i in json_output:
        #print(i['field'])
        #print(i['value'])
        riskOut = (i['value'])


    #print(riskOut)
    return riskOut

def find_severity(etID):
    #print(etID)
    sevOut = 0
    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
        'assetID': ''
    }
    #goJuice = "/v2/assets/fields/?assets=" + str(etID) + "&fields=7&limit=10"

    conn.request(
        "GET", "/v2/assets/fields/?assets=" + str(etID) + "&fields=7&limit=10", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)

    for i in json_output:
        #print(i['field'])
        #print(i['value'])
        sevOut = (i['value'])


    #print(sevOut)
    return sevOut

def calc_pdc(dueUni):
    pdc = 5
    nowStamp = int(time.time()) 
    #gap = -1 * (dueUni - nowStamp) / 86400 
    gap =(nowStamp - dueUni) / 86400
    
    if gap > 56:
        pdc = 0
    elif gap > 49:
        pdc = 1
    elif gap > 35:
        pdc = 2
    elif gap > 28:
        pdc = 3
    elif gap > 14:
        pdc = 4
    else:
        pdc = 5

    """ print(gap)
    print(pdc) """


    return pdc

def buildArrayofTasks():
    conn = http.client.HTTPSConnection("api.limblecmms.com", 443)
    payload = ""
    userAndPass = b64encode(
        b"DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z:WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y").decode("ascii")

    headers = {
        'Authorization': 'Basic %s' % userAndPass,
    }
    conn.request("GET", "/v2/tasks", payload, headers) #the LIMITED (limiting the number of results) will need to be removed eventually. NOW::::: ?limit=" + str(limited) + "&status=0

    res = conn.getresponse()
    data = res.read()

    json_output = json.loads(data)

    FCA = []  # "taskID","assetID","severity","risk","pdc","FC"
    taskArr = []
    assetArr = []
    sevArr = []
    riskArr = []
    pdcArr = []
    fcArr = []
    prioArr = []
    keyGuide = "taskID,assetID,severity,risk,pdc,FilterCode,Priority"

    """ with open('APIpy.json') as f:
        data = json.loads(f.read())
        #print(data[0]['taskID'])
    """
    for i in json_output:
        #print(i['taskID'])
        #with taskID
        #print(i['assetID'])
        #with assetID
        #print(" - ")
        #FCA += [i] # & "-"
        if (i['due']) != 0:
            thisRisk = find_risk(i['assetID'])
            thisSev = find_severity(i['assetID'])
            thisPDC = calc_pdc(i['due'])
            thisFC = calc_filterCode(thisRisk, thisSev, thisPDC)

            taskArr += [i['taskID']]
            assetArr += [i['assetID']]
            sevArr += [thisSev]
            riskArr += [thisRisk]
            pdcArr += [thisPDC]
            fcArr += [thisFC]
            #FCA += [("-")]
            #f.close()
        #END if-due 
    #END FOR-i LOOP


    #print(taskArr)
    ##print(keyGuide)
    #print(fcArr)

    FCA2Priorites(taskArr, fcArr)

    return(print("COMPLETE"))



buildArrayofTasks() #LIMITED was removed

""" #MAKE two mulitdimensional array m1[], m2[]
###FIRST lists are ordered: taskArri, fcArri, prioArr(emptyToStart) - unaltered, to be referenced later     
###SECOND lists are ordered: taskArri, fcArri. Which are then sorted np.sort(m2 by second list)

##### FROM @@@HERE@@@
    if (0 in fcArri) == True:
        #new array (prioArr) will generate such that fcArri(0) = 1
        #Divide remaining in fcArri into 4 sections, assign 2-5 for each section into prioArr
        
        for k, j in enumerate(fcArri):
            if j == 0:
                prioArr += [1]
                #print(prioArr)
            else:
                print(k) # - J - Needs to be the index/position of J in the array
                print(len(fcArri))
                print("1 Non-Zero")
                if fLength == 0:
                    fLength = (len(fcArri)) - k
                    print(fLength)
                    fLength = fLength // 4
                    print(fLength)
                    #fcArri len - j / 4 or something idk
                else:
                    print("nothing yet")

            #END IF
        #END FOR-j
    else:
        #np.sort(fcArri) (ascending by default)
        #divide fcArri into FIVE equal parts/sections
        #populate prioArr
        print('nothing here yet.')

###### TO @@@HERE@@@ MIGHT BE USELESS, need to figure out 
# how to bring the 'sorted' list back to original order 
# after the prioArr/PriorityNumbers have been calculated


        fourKey = np.stack((nzFcArri, prioArri), axis=0) #### DONT NEED?
        print(fourKey)
 """