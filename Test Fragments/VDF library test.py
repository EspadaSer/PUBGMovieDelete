import vdf

d = vdf.parse(open("C:\\Steam\\SteamApps\libraryfolders.vdf"))

print(d['LibraryFolders']['1']) 

print(d['LibraryFolders']['2']) 

print(len(d['LibraryFolders'])-2)
 
