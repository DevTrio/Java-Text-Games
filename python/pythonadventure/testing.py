print("Location Testing and file name concatenation...")
saveFile = input("save: ")
fileLoc = "./data/save" + saveFile + "/location.txt"
print(fileLoc)
loc = open(fileLoc, "r")
print(loc.readline())
