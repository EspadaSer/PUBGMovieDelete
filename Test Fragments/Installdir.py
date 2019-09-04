#Imports

import os
import winreg

#detect win os version

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

#read registry

if Is64Windows() is True:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Valve\\Steam")
else:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Valve\\Steam")
    
steampath =  winreg.QueryValueEx(key, "InstallPath")[0]

#create folderpath

acfpath = steampath + "\\SteamApps\\appmanifest_578080.acf"

if os.path.isfile(acfpath):
    folderpath = steampath + "\\SteamApps\\common\\PUBG\\TslGame\\Content\\Movies"
        print("Game location detected")
    else:
        print("file in different location")

# Initialization. Do not modify

i=0
filename = ["LicenseScreen.mp4", "LoadingScreen.mp4", "LoadingScreen_Xbox.mp4"]

# Main

for i in range(3):
    filepath = folderpath + "\\" + filename[i]
    if os.path.isfile(filepath):
        os.remove(filepath)
        print("Deleted " + filepath)
    else:
        print("File not found " + filepath)

