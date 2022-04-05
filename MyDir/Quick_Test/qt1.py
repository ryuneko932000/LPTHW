# Quick test 1
# Quick Test 1
from genericpath import exists
from sys import argv

script, filename = argv


fileActualName = filename
filename = exists(filename)


if filename == False:
    print(f"File not found, creating new file: {fileActualName}")
    file = open(fileActualName, 'r+')
    text = input("Write in the text that you want to add: \n>")
    file.write(text)





