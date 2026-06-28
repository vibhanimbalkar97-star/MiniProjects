from pathlib import Path
import os

folder = Path("File Handling")
# check file and folders
def readfileandfolder():
    path = Path('File Handling')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the file name you want to create:- ")
        p = folder / name 
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in file:- ")
                fs.write(data)
        else:
            print("File already exists")
    except Exception as err:
        print(f"An error occurred {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter file name you want to read:- ")
        p = folder / name
        if p.exists() and p.is_file():
            with open(p) as fs:
                data=fs.read()
                print(data)
            print("Readed successfully")
        else:
            print("File doesn't exists")
    except Exception as err:
        print(f"An error occurred {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the file you want to update:- ")
        p = folder / name
        if p.exists() and p.is_file():
            print("Press 1 to change the file name:- ")
            print("Press 2 to overwrite the data in file:- ")
            print("Press 3 to append the some content in file:- ")

            result = int(input("Enter your choice:- "))
        
            if result == 1:
                name2=input("Enter new file name:- ")
                p2=folder / name2
                p.rename(p2)

            if result == 2:
                with open(p, "w") as fs:
                    data = input("Tell what you want to write this is overwrite the data :- ")
                    fs.write(data)
          

            if result == 3:
                with open(p, "a") as fs:
                    data = input("Tell what you want to append :- ")
                    fs.write(" "+data)
        else:
            print("File not found")   
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter file you want to delete:- ")
        p = folder / name
        if p.exists() and p.is_file():
            os.remove(p)
            
            print("file removes suiccessfully ")
    
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")
        
while True:
    print("\nPress 1 for creating file:- ")
    print("Press 2 for reading file:- ")
    print("Press 3 for updating file:- ")
    print("Press 4 for deleting file:- ")

    choice = int(input("Enter your choice:- "))

    if choice == 1:
        createfile()

    elif choice == 2:
        readfile()

    elif choice == 3:
        updatefile()

    elif choice == 4:
        deletefile()
        break

    else:
        print("You entered wrong choice")



# | Pattern   | Meaning                        |
# | --------- | ------------------------------ |
# | `"*"`     | Everything (files and folders) |
# | `"*.txt"` | Only `.txt` files              |
# | `"*.py"`  | Only Python files              |
# | `"data*"` | Anything starting with `data`  |
# | `"*.jpg"` | Only `.jpg` files              |
