print("Welcome to Python Adventure.")
print("Your progress will be automatically resumed from the last time you saved.")
file = input("Save File (1-3): ")
currSave = open("./currentSave.txt", "w")
print("loading...\n\n")
if file == "1":
    save = open("./data/save1/location.txt", "r")
    currSave.write("1")
elif file == "2":
    save = open("./data/save2/location.txt", "r")
    currSave.write("2")
elif file == "3":
    save = open("./data/save3/location.txt", "r")
    currSave.write("3")
loc = save.readline()
if loc == "intro":
    exec(open("./intro.py").read())
elif loc == "mainField":
    exec(open("./mainField.py").read())
else:
    print("A loading error occurred. Visit the github page to find out how to fix it.")
