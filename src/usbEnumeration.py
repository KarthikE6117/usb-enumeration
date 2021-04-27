import usb.core
import csv
import os
import datetime

def getIDs(Vid, Pid):
    vendorID = hex(Vid)[2:]
    productID = hex(Pid)[2:]
    if len(vendorID) == 3:
        vendorID = '0'+vendorID
    if len(productID) == 3:
        productID = '0'+productID
    return vendorID, productID

def getDeviceNames(Vid, Pid, swArg):
    usbFile = open("USB_DATABASE.csv", 'r')
    usbTable = csv.reader(usbFile)
    for record in usbTable:
        if Vid in record and Pid in record:
            if swArg == 1:
                vendors.append(record[1])
                devices.append(record[3])
            elif swArg == 0:
                dVendorName.append(record[1])
                dDeviceName.append(record[3])

def checkIfDBExists():
    if "USB_DATABASE.csv" in os.listdir('.'):
        return True
    else:
        return False

def checkIfDefaultExists():
    if "default.csv" in os.listdir('.'):
        return True
    else:
        return False

def createDefault():
    print(
        "To create default.csv please disconnect all the removable media from the system\n[Type \"exit\" or \"EXIT\" to terminate the program]\nor press ENTER to continue...")
    inputKeys = input()
    if inputKeys == "exit" or inputKeys == "EXIT":
        exit(0)
    
    defaultFile = open("default.csv", "a+", newline='')
    defaultFileWriter = csv.writer(defaultFile)
    dev = usb.core.find(find_all=True)
    for device in dev:
        li.append(device)
    for d in li:
        vendorID, productID = getIDs(d.idVendor, d.idProduct)
        vendors.append(vendorID)
        devices.append(productID)
    defaultFileWriter.writerow(vendors)
    defaultFileWriter.writerow(devices)

def listDifference():
    for _ in set(vendors)-set(dVendorsList):
        detectedVID.append(_)
    for _ in set(devices)-set(dDevicesList):
        detectedPID.append(_)

def listDefaultDevices():
    dVendorName.clear()
    dDeviceName.clear()
    for i in range(len(vendors)):
        getDeviceNames(vendors[i], devices[i], 0)
        print(dVendorName[i], dDeviceName[i])

############## for future purposes #################

def writeLogs():
    logFile = open("./logs/DETECTION_LOG.log", "a+")
    logFile.write(8*"*"+" "+str(datetime.datetime.now())+" "+8*"*"+"\n")
    for i in range(len(dVendorName)):
        logFile.write("DEVICE_"+str(i+1)+" : "+dVendorName[i]+" "+dDeviceName[i]+"\n")
    logFile.write("\n"+48*"*"+"\n\n")
    logFile.close()

#####################################################

li = list()
vendors = list()
devices = list()
dVendorsList = list()
dDevicesList = list()
detectedVID = list()
detectedPID = list()
dDeviceName = list()
dVendorName = list()

def main():
    if checkIfDBExists() == True:
        if checkIfDefaultExists() == True:
            try:
                dev = usb.core.find(find_all = True)
                for device in dev:
                    li.append(device)
                for d in li:
                    vendorID, productID = getIDs(d.idVendor, d.idProduct)
                    vendors.append(vendorID)
                    devices.append(productID)
                defaultFile = open("default.csv", "r")
                defaultFileReader = csv.reader(defaultFile)
                c=0
                for row in defaultFileReader:
                    if c == 0:
                        for i in range(len(row)):
                            dVendorsList.append(row[i])
                    if c == 1:
                        for i in range(len(row)):
                            dDevicesList.append(row[i])
                    c+=1
                listDifference()
                for i in range(len(detectedVID)):
                    getDeviceNames(detectedVID[i], detectedPID[i], 0)
                print("CONNECTED DEVICES\n********************")
                for i in range(len(dVendorName)):
                    print(str(i+1)+'.',dVendorName[i], dDeviceName[i])
                writeLogs()
                input("\nPress ENTER to exit the program")
            except usb.core.NoBackendError:
                print("libusb backend library not found!\nRun the BugFix.py first to fix this bug\nIMOPRTANT: Open the command prompt with \"run as administrator\" and execute the BugFix.py file through that command prompt!!")
        else:
            createDefault()
            print("default.csv has been generated. You are good to go!\nPress any key to exit the program...")
            input()
            exit(0)
    else:
        print("DATABASE DOES NOT EXIST...")
        print("Run the getIds.py first with an active Internet connection to generate the database csv file...")

if __name__ == "__main__":
    main()



