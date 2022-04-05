# Designing and debugging and small game project. 

# Some quick rules regarding for and while loops:


### IF STATEMENTS ###
    # every 'if' statement needs a 'else' statement, if the else is just meant to not 
    # do anything, call a function that will end the program such as dead() in ex35.py


    # Try not to put an if statement in another if statement, if that happens use a function
    # instead.
 
    # Treat if statements like paragraphs formatting wise. That includes elif, and else

    # Your boolean test should be simple.


### LOOPS ###
    # Use while loops only if you want something to run forever.
    # For loops should be used for everything else, especially if there is 
    # a fixed or limited number of things to loop over.

def start(): 
    print("""
    Whilst walking to your house you 
    glitched through the floor, falling into 
    what urban legends call \"The Backrooms\".  
    """)
    input("* PRESS ENTER TO CONTINUE")
    print(""" 
    You get up from the floor. As you stand up you can feel the weight
    on your feet pressing unto the carpet. You are stuck in a place with endless
    office spaces. Yellow wallpapers on every wall. The place feels like a maze.
    """)
    input("* PRESS ENTER TO CONTINUE")
    print(""" 
    Something feels off...the low yet blaring humming of the fluorescent lights 
    keep you on a continual state of uneasiness. You start to think on your plan.
    """)
    input("* PRESS ENTER TO CONTINUE")
    print("What do you do?")
    print("""
    A. Stay put! This surely is only a dream.
    B. Wander around. Better than just sitting there.
    C. Inspect the floor
    D. Inspect the room.
        """)
    next = input("> ")
    if next == 'A':
        waiting()
    elif next == 'B':
        start_wander()
    elif next == 'C':
        print("")

def waiting(): 
    print("")


def start_wander():
    print("")


start()



