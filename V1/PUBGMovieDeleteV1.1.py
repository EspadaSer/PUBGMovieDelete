import os
import configparser

# Config file exists

config = configparser.RawConfigParser()
configFilePath = r'path.txt'

if not os.path.isfile(configFilePath):
    config['Settings'] = {'path' : 'C:\\Steam\\SteamApps\\common\\PUBG\\TslGame\\Content\\Movies'}
    config.write(open('path.txt', 'w'))
    print("path.txt NOT found. File created with default path. If PUBG is installed in a different location edit path.txt and run the program again")

if os.path.isfile(configFilePath):
    config.read(configFilePath)
    folder_path = config.get('Settings', 'path')
    print("path.txt found. Path: " + folder_path)
    
# Initialization. Do not modify

i=0
filename = ["LicenseScreen.mp4", "LoadingScreen.mp4", "LoadingScreen_Xbox.mp4"]

# Main

for i in range(3):
    filepath = folder_path + "\\" + filename[i]
    if os.path.isfile(filepath):
        os.remove(filepath)
        print("Deleted " + filepath)
    else:
        print("File not found " + filepath)
    
# PRESS KEY TO EXIT

input("Press ENTER to terminate this program")
raise SystemExit(0)
