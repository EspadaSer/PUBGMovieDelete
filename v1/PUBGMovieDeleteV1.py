import os

# Initialization. Do not modify
i=0
folder_path = "C:\Steam\SteamApps\common\PUBG\TslGame\Content\Movies"
filename = ["LicenseScreen.mp4", "LoadingScreen.mp4", "LoadingScreen_Xbox.mp4"]

# Main

for i in range(3):
    filepath = folder_path + "\\" + filename[i]
    if os.path.isfile(filepath):
        os.remove(filepath)
        print("Deleted " + filepath)
    else:
        print("File not found " + filepath)
    

