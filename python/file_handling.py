# file handling
"""
'r'  read
'w'  write- creates file or overwrite
'a'  append- adds to end of file
'x'  create - creates a new file, fails if it exists

p = open(r'E:\Machine Learning\python\loops.py')   # read
print(p.read())

a = open("demo.txt",'w')       # overwrites 
a.write("Hello i am div")
a.close()

b = open("demo.txt",'a')      # append 
b.write("and i am a student")
b.close()

c = open("new.txt" , 'x')     # creates file if not exists
"""

# project 
from pathlib import Path
import os

def readFileandFolder():
    path = Path('')
    items = list(path.rglob('*'))    # to 
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createFile():
    try:
        readFileandFolder()
        name = input("please tell your file name:-")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data = input("What you want to write in this file :-")
                fs.write(data)
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print()
    except Exception as err:
        print(f"An error occured as {err}")


def readFile():
    try:
        readFileandFolder()
        name = input("which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("Readed successfully")
        else:
            print("The file doesn't exist")
    except Exception as err:
        print(f"An error occured as {err}")

def updateFile():
    try:
        readFileandFolder()
        name = input("tel which file do you want to update")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")

            res = int(input("tell your response"))

            if res == 1:
                name2 = input("tell your new file name")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write this is overwrite the data")
                    fs.write(data)
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to write this is overwrite the data")
                    fs.write(data)  
    except Exception as err:
        print(f"An error occured as {err}")


def deleteFile():
    try:
        readFileandFolder()
        name = input("which file you want to delete ")
        p = Path('')

        if p.exists() and p.is_file():
            os.remove(name)

            print("File removed successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for reading a file")

check = int(input("please tell your response :-"))

if check == 1:
    createFile()
elif check == 2:
    readFile()
elif check == 3:
    updateFile()
elif check == 4:
    deleteFile()