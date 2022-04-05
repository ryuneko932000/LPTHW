# Using while loop as sa function
def myFunction(limitPoint, adder):
    i = 0 
    myList = []
    while i < limitPoint:
        print(f"Top number is: {i}")
        myList.append(i)
        i += adder
        print("Our number list: ", myList)
        print(f"Lower number is: {i}")

    print("The numbers: ")
    for num in myList:
        print(num)


def forFunction(limitPoint):
    i = 0
    myList = []
    for i in range(0, limitPoint):
        print(f"Top number is: {i}")
        myList.append(i)
        print("Our number list: ", myList)
        print(f"Lower number is: {i}")
    
    print("The numbers: ")
    for num in myList:
        print(num)


forFunction(5)
