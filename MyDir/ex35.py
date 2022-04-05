# Branches and functions 
from sys import exit 

def gold_room():
    print("The room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next: 
        how_much = int(next)
    else: 
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Not a greedy man huh? Take your reward! Good job!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("Theres's a bear here.")
    print("The bear has a bunch of money.")
    print("The fat bear is in front of the other door.")
    print("What do you do to move the bear?")
    bear_moved = False

    while True: 
        print("Here are your options:")
        print("a. Take Honey")
        print("b. Taunt bear")
        next = input("> ")
         
        if next == "a":
            dead("The bear looks at you and slaps your face off.")
        elif next == "b" and not bear_moved:
            print("The bear has moved from the door. You can enter now.")
            bear_moved = True
        elif bear_moved:
            print("What is your next move?")
            print("""
            a. Open the door
            b. Stay put 
            c. Taunt the bear again
            """)
            next = input("> ")
            if next == "a": 
                gold_room()
            elif next == "b":
                print("How boring of you. You sit down and stay there for eternity.")
                exit(0)
            elif next == "c":
                dead("The bear is irritated by your lack of sense and chews your leg off.")
            else: 
                print("Yeah buddy, that's not on the options list. What do you want to do?")
        else: 
            print("Yeah buddy, that's not on the options list. What do you want to do?")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("""Do you? 
    a. flee for your life?  
    b. eat your head?
    """)
    next = input("> ")

    if next == 'a':
        start()
    elif next == 'b':
        dead("""
    Well you can't really eat your head without your head....
    Nevertheless, your head explodes... Because insanity....
            """)

def dead(reason):
    print(reason, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and to your left.")
    print("Which one do you take?")
    print(""" 
    a. Right door
    b. Left Door
    """)

    next = input("> ")
    if next == 'a':
        cthulhu_room()
    elif next == 'b':
        bear_room()
    else: 
        dead("You walk the around dark roomm turns out it's an endless void, you get lost and die.")

start()