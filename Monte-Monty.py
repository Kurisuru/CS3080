'''
PROGRAMMER: Christopher D Colbert
USERNAME: ccolbert
PROGRAM: MONTE-Monty.py

DESCRIPTION: Monty Door simulation
'''
#Choose door at random
import random
door1 = False
door2 = False
door3 = False

choices = [1,2,3]
correct_door = int(random.choice(choices))
door = int(correct_door)

match door:
    case 1:
        door1 = True
    case 2:
        door2 = True
    case 3:
        door3 = True

#ask user to choose door
door = int(input("Choose a door to open: "))

#choose door to get rid of

choices.remove(door)
remove = int(random.choice(choices))

match remove:
    case 1:
        if door1 == False:
            choices.remove(remove)
        else:
            for n in choices:
                if n != remove:
                    choices.remove(n)
    case 2:
        if door2 == False:
            choices.remove(remove)
        else:
            for n in choices:
                if n != remove:
                    choices.remove(n)
    case 3:
        if door3 == False:
            choices.remove(remove)
        else:
            for n in choices:
                if n != remove:
                    choices.remove(n)
                    
#ask user to switch or stay

print("Would you like to keep door {0}? or switch".format(door))
switch = input("Enter switch or stay: ")
switch_table = {'switch': True, 'stay': False}
switch = switch_table[switch]

#display correct option

print("The correct door was door {0}".format(correct_door))
