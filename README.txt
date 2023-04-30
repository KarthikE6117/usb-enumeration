MICROCHIP INTERNSHIP-2021
***********************************
DEVELOPED BY KARTHIK
***********************************

=======================================
Directory Structure (for verification):
=======================================

task_2_bundle{
    bugfix
    {
        BugFix(directory)
        BugFix.py
    }
    src
    {
        logs(for future use)
        {
            DETECTION_LOG.log
        }
        default.csv(will be auto-generated)
        getIDs.py 
        USB_DATABASE.csv(database file)
        usbEnumeration.py 
    }
    README.txt(this file)
    requirements.txt
}


=====================================
Installing Python Modules:
=====================================

    - Open the command prompt in the task_2_bundle folder.
    - Run the command "pip install -r requirements.txt" 
    - This will install the dependencies for this bundle.

=====================================
INSTRUCTIONS
=====================================

Generating the USB_DATABASE.csv (THIS STEP SHALL BE SKIPPED!):
---------------------------------------------------------------

    - First of all, we need our database file to get generated. So run the getIDs.py file with an active internet connection.
    - This will fetch all the USB vendor and device information and store it in a csv file.
    - This runtime shall even consume an hour, and also dependes upon the Network response time and Processing speed of the system.
    
    *** WE HAVE ALREADY DONE THIS STEP AND GENERATED THE DATABASE FILE(USB_DATABASE.csv)... ***

usbEnumeration.py 
------------------
    
    - This is our main file which will be performing the USB Enumeration.
    - Executing this file for the very first time will generate default.csv in the src folder.
    - After that, it uses the generated default.csv to detect the removable media.

    *** For the first time execution alone, disconnect all the removable media from the computer and run the program. ***

BugFix.py
----------
    - If you come across any exception for backend unavailability while executing the usbEnumeration.py, then the libusb system library is missing from your computer.
    - To fix this bug, We've written a python patch code to patch the libusb dll file to the system libraries path.
    - This will solve this bug!

    *** IT IS MANDATORY TO RUN THIS FILE IN THE COMMAND PROMPT WHICH SHOULD BE OPENED AS ADMINISTRATOR ***

