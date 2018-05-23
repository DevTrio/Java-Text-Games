print("Welcome to Python Adventure.")
print("Your progress will be automatically resumed from the last time you saved.")
print("loading...\n\n")
save = open("./data/location.txt", "r")
loc = save.readline()
if loc == "intro":
    exec(open("./intro.py").read())
elif loc == "mainField":
    exec(open("./area1.py").read())
else:
    print("A loading error occurred. Visit the github page to find out how to fix it.")
