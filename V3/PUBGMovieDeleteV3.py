# IMPORTS

import os
import winreg
import vdf
import configparser

# DETECT OS VERSION

def Is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ

def GetProgramFiles32():
    if Is64Windows():
        return os.environ['PROGRAMFILES(X86)']
    else:
        return os.environ['PROGRAMFILES']

def GetProgramFiles64():
    if Is64Windows():
        return os.environ['PROGRAMW6432']
    else:
        return None

# OPTIONS

def menu():
    print("Choose an option from the following:")
    print("[a] Use the location from path.txt.")
    print("[b] Auto-detect game files.")
    
# CONFIG FILE CHECK/CREATION

def custom():

    global folderpath
    config = configparser.RawConfigParser()
    configFilePath = r'path.txt'

    if not os.path.isfile(configFilePath):
        config['Settings'] = {'path' : 'C:\\Steam\\SteamApps\\common\\PUBG\\TslGame\\Content\\Movies'}
        config.write(open('path.txt', 'w'))
        print("Path.txt NOT found. The file was created with default path. If PUBG is installed in a different location, edit path.txt and run the program again")

    if os.path.isfile(configFilePath):
        config.read(configFilePath)
        folderpath = config.get('Settings', 'path')
        print("Path.txt found. Path: " + folderpath)

# AUTODETECT GAME LOCATION

def auto():

    # READ REGISTRY TO LOCATE STEAM INSTALLATION

    if Is64Windows() is True:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Valve\\Steam")
    else:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Valve\\Steam")
        
    steampath =  winreg.QueryValueEx(key, "InstallPath")[0]

    # LOCATE THE ACTUAL PUBG INSTALLATION FILES
    
    global folderpath
    acfpath = steampath + "\\SteamApps\\appmanifest_578080.acf"

    if os.path.isfile(acfpath):
        folderpath = steampath + "\\SteamApps\\common\\PUBG\\TslGame\\Content\\Movies"
        print("Game location detected")
    else:
        vdffile = vdf.parse(open(steampath + "\\SteamApps\\LibraryFolders.vdf"))
        vdflocations = len(vdffile['LibraryFolders'])-2
        for a in range(vdflocations):
            b = a + 1
            steampath2 = vdffile['LibraryFolders'][str(b)]
            acfpath2 = steampath2 + "\\SteamApps\\appmanifest_578080.acf"
            if os.path.isfile(acfpath2):
                folderpath = steampath2 + "\\SteamApps\\common\\PUBG\\TslGame\\Content\\Movies"
                print("Game location detected at " + folderpath)
                break
        
# MOVIE FILENAMES

i=0
filename = ["LicenseScreen.mp4", "LoadingScreen.mp4", "LoadingScreen_Xbox.mp4"]

# DELETE MOVIE FILES

def delete():

    for i in range(3):
        filepath = folderpath + "\\" + filename[i]
        if os.path.isfile(filepath):
            os.remove(filepath)
            print("Deleted " + filepath)
        else:
            print("File not found " + filepath)
            print("Maybe the file was already deleted")

    # PRESS KEY TO EXIT

    input("Press ENTER to terminate this program")
    raise SystemExit(0)

# WHILE LOOP

option = "0"
while option!= "a" and option!= "b":
    menu()
    option = input()

if option == "a":
    custom()
    delete()
    
elif option == "b":
    auto()
    delete()
