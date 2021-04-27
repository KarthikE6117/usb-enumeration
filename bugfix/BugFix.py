import os
import shutil

system = os.listdir("C:/")
dllFile = "libusb-1.0.dll"
refDir = ['Program Files (x86)', 'Program Files']

def findArchitecture():
    if refDir[0] in system and refDir[1] in system:
        return 'x64'
    else:
        return 'x86'

def isBuggy(arch):
    if arch == 'x64':
        if dllFile in os.listdir("C:/Windows/System32"):
            return False 
        else:
            return True 
    if arch == "x86":
        if dllFile in os.listdir("C:/Windows/SysWOW64"):
            return False
        else:
            return True

def main():
    winArch = findArchitecture()
    bugStatus = isBuggy(winArch)
    root = os.getcwd()
    path = ''
    for _ in range(len(root)):
        if root[_] == "\\":
            path += "/"
        else:
            path += root[_]    
    if winArch == 'x64':
        if bugStatus == True:
            shutil.copyfile(path + "/BugFix/libusb-1.0.21/MS64/dll/libusb-1.0.dll", "C:/Windows/System32/libusb-1.0.dll")
            print("Good to Go..!")
            input()
            return 0
        else:
            print("Your machine is already Compatible...Good to Go..!")
            input()
            return 0
    if winArch == 'x86':
        if bugStatus == True:
            shutil.copyfile(path + "/BugFix/libusb-1.0.21/MS32/dll/libusb-1.0.dll", "C:/Windows/SysWOW64/libusb-1.0.dll")
            print("Good to Go...!")
            input()
            return 0
        else:
            print("Your machine is already Compatible...Good to Go..!")
            input()
            return 0


if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        input("Run this program in cmd as administrator...")