import requests
import urllib
from bs4 import BeautifulSoup
import os 
import csv

vendorList = list()
csvRows = list()
if "USB_DATABASE.csv" in os.listdir(os.getcwd()):
    if os.path.getsize("USB_DATABASE.csv")<100:
        inputKeys = 'y'
    else:
        inputKeys = input("USB_DATABASE.csv file already exists...\nDo you really want to regenerate the file?\n[yes(y)/no(n)]")
    if inputKeys == 'y' or inputKeys == 'Y' or inputKeys == "YES" or inputKeys == "yes":
        os.remove("USB_DATABASE.csv")
    elif inputKeys == 'n' or inputKeys == 'N' or inputKeys == 'NO' or inputKeys == 'no':
        print("quitting...")
        exit(0)

vendorID = None 
deViceIDStringPortal = "https://devicehunt.com/view/type/usb/vendor/"
vendorIDStringPortal = "https://devicehunt.com/all-usb-vendors"
try:
    response = requests.get(vendorIDStringPortal)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find_all('tr')
    for row in table:
        vendor = row.find('a')
        if vendor == None:
            continue 
        vendorList.append(vendor.text.strip())
    for VID in vendorList:
        response2 = requests.get(deViceIDStringPortal + VID)
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        finalTable = soup2.find('div', class_="search-results").find_next('table')
        if finalTable == None:
            continue
        finalTable = finalTable.findAllNext('tr')
        for _ in range(len(finalTable)):
            if _ == 0:
                continue
            tdElement = finalTable[_].find_all('td')
            tempList = list()
            for i in range(len(tdElement)):
                if i == 0:
                    continue
                if i == 1:
                    tempList.append(tdElement[i].find('a').text.strip())    #Vendor ID
                if i == 2:
                    tempList.append(tdElement[i].text.strip())              #Vendor name
                if i == 3:
                    tempList.append(tdElement[i].find('a').text.strip())    #Device ID
                if i == 4:
                    tempList.append(tdElement[i].text.strip())              #device name
            print(tempList)
            csvRows.append(tempList)
            input("SUCCESS!\nPress ENTER to exit the program...")
except requests.exceptions.ConnectionError:
    print("Connection Timed Out :(")
    exit(0)

usbDB = open("USB_DATABASE.csv", "a+", newline='')
csvWriter = csv.writer(usbDB)
csvWriter.writerow(["VENDOR_ID", "VENDOR_NAME", "DEVICE_ID", "DEVICE_NAME"])
csvWriter.writerows(csvRows)

