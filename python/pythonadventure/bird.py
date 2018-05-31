# the bird statue subprogram. Runs when the user activates a bird statue.
strings = ["Save", "Map", "Warp", "Save and Quit"]
# files:
currSaveFile = open("./currentSave.txt", "r")
currSave = currSaveFile.readline()
locFile = open("./data/" + currSave + "/location.txt", "w+"
currLocFile = open("./currentLocation.txt", "r+")
location = currLocFile.readline()
locFile.write(location)
