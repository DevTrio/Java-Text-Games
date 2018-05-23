# An adventure game for Python 3.6.1 and above.
#
#  ________  ___    ___ _________  ___  ___  ________  ________      
# |\   __  \|\  \  /  /|\___   ___\\  \|\  \|\   __  \|\   ___  \    
# \ \  \|\  \ \  \/  / ||___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \   
#  \ \   ____\ \    / /     \ \  \ \ \   __  \ \  \\\  \ \  \\ \  \  
#   \ \  \___|\/  /  /       \ \  \ \ \  \ \  \ \  \\\  \ \  \\ \  \ 
#    \ \__\ __/  / /          \ \__\ \ \__\ \__\ \_______\ \__\\ \__\
#     \|__||\___/ /            \|__|  \|__|\|__|\|_______|\|__| \|__|
#          \|___|/                                                   
#                                                                   
#  ________  ________  ___      ___ _______   ________   _________  ___  ___  ________  _______      
# |\   __  \|\   ___ \|\  \    /  /|\  ___ \ |\   ___  \|\___   ___\\  \|\  \|\   __  \|\  ___ \     
# \ \  \|\  \ \  \_|\ \ \  \  /  / | \   __/|\ \  \\ \  \|___ \  \_\ \  \\\  \ \  \|\  \ \   __/|    
#  \ \   __  \ \  \ \\ \ \  \/  / / \ \  \_|/_\ \  \\ \  \   \ \  \ \ \  \\\  \ \   _  _\ \  \_|/__  
#   \ \  \ \  \ \  \_\\ \ \    / /   \ \  \_|\ \ \  \\ \  \   \ \  \ \ \  \\\  \ \  \\  \\ \  \_|\ \ 
#    \ \__\ \__\ \_______\ \__/ /     \ \_______\ \__\\ \__\   \ \__\ \ \_______\ \__\\ _\\ \_______\
#     \|__|\|__|\|_______|\|__|/       \|_______|\|__| \|__|    \|__|  \|_______|\|__|\|__|\|_______|
#
# art generated from http://patorjk.com/software/taag/#p=display&f=3D-ASCII&t=Python%0AAdventure                                                                                                   
# now comes the actual code...
# string arrays
strings1 = ["You wake up in a dark and mysterious cave.", "What do you want to do?", "You get up.", "You can't see anything.", "You run into a wall. It feels hard and cold...", "You start to head back when suddenly, you see a fire start.", "You can now see everything in the room."]
strings2 = ["You see a switch on the wall. Next to it is the outline of a door.", "You arrive at the switch", "The door opens.", "You are temporarily blinded by the sun as the door opens.", "You are standing outside a grassy field, and the door closes behind you.", "There is a statue of a bird nearby."]
replies1 = ["Get up", "Look around", "Walk forward"]
replies2 = ["Walk to switch", "Activate switch", "Head outside", "Look around", "Go to bird statue"]
query = ["What do you want to do? ", "What do you want to do now? "]
invalid = ["Please enter a valid response."]
control = True #change this to true after each loop
print(strings1[0])
print(strings1[1])
print(replies1[0])
reply = input().lower()
print(strings1[2])
while control:
    print(replies1[1], replies1[2], sep="\t")
    reply = input(query[0]).lower()
    if reply == "look around":
        print(strings1[3])
        control = True
    elif reply == "walk forward":
        print(strings1[4])
        control = False
    else:
        print(invalid[0])
        control = True
print(strings1[5], strings1[6]) # use set 2 now
control = True
while control:
    print(replies1[1])
    reply = input(query[1]).lower()
    if reply == "look around":
        print(strings2[0])
        control = False
    else:
        print(invalid[0])
        control = True
control = True
while control:
    print(replies2[0], sep="\t")
    reply = input(query[0]).lower
    if reply == "walk to switch":
        print(strings2[1])
        control = False
    else:
        print(invalid[0])
        control = True
control = True
print(strings2[1])
while control:
    print(replies2[1], sep="\t")
    reply = input(query[0]).lower
    if reply == "activate switch":
        print(strings2[2])
        control = False
    else:
        print(invalid[0])
        control = True
control = True
while control:
    print(replies2[2], sep="\t")
    reply = input(query[0]).lower
    if reply == "head outside":
        print(strings2[3])
        control = False
    else:
        print(invalid[0])
        control = True
control = True
while control:
    print(replies2[3], sep="\t")
    reply = input(query[0]).lower
    if reply == "look around":
        print(strings2[4])
        control = False
    else:
        print(invalid[0])
        control = True
control = True
print(strings2[5])
