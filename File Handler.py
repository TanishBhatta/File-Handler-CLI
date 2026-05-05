#File Handling Python Project by Tanish Bhatta

import os
from pathlib import Path
from colorama import Fore, Style
import time
from tkinter import filedialog
import tkinter as tk

#defining pick_directory()
def pick_directory():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path

#Welcoming the user
time.sleep(0.5)
print(Fore.CYAN + "Welcome to the " + Style.RESET_ALL + Fore.LIGHTRED_EX + "File Handler Program" + Style.RESET_ALL + Fore.CYAN + " made by " + Style.RESET_ALL + Fore.MAGENTA + "Tanish Bhatta" + Style.RESET_ALL)
time.sleep(1)
print("""\nFunctions of this program:
Create — makes a new file in any folder you navigate to, with optional text written inside it on creation.
Read — opens and displays the contents of any existing file.
Update — modifies an existing file by renaming it, overwriting its content, or appending new content.
Delete — permanently removes a file from disk.""")
time.sleep(1)

while True:
    ask = input(Fore.LIGHTGREEN_EX + "\nLocate a folder to handle files? (Y or N)\n-> " + Style.RESET_ALL)
    if ask.lower() == "y":
        break
    elif ask.lower() == "n":
        exit()
    else: print(Fore.RED + "Enter (Y or N)" + Style.RESET_ALL)

#calling pick_directory()
base_path = pick_directory()

#def showing_files()
def showing_files(base_path):
    p = Path(base_path)
    items = list(p.iterdir())
    print(Fore.LIGHTRED_EX + "\n----Files inside the directory----\n" + Style.RESET_ALL)
    for i, item in enumerate(items):
        time.sleep(0.22)
        if item.is_dir():
            print(Fore.CYAN + f"{i + 1}) {item.name} (folder)" + Style.RESET_ALL)
        else: print(Fore.LIGHTMAGENTA_EX + f"{i + 1}) {item.name}" + Style.RESET_ALL)

#defining navigate()
def navigate(base_path):
    showing_files(base_path)
    time.sleep(1)
    choice = input(Fore.LIGHTYELLOW_EX + "\nOpen a folder? (Y or N)\n-> " + Style.RESET_ALL)
    if choice.lower() == "y":
        time.sleep(0.5)
        num = int(input(Fore.LIGHTYELLOW_EX + "Enter folder number: " + Style.RESET_ALL))
        items = list(Path(base_path).iterdir())
        selected = items[num - 1]
        if selected.is_dir():
            return navigate(str(selected))
        else: 
            print(Fore.RED + "\nThat is not a folder." + Style.RESET_ALL)
            return base_path
    return base_path

#Defining createfile()
def createfile(base_path):
    try:
        base_path = navigate(base_path)
        time.sleep(0.5)
        name = input(Fore.LIGHTYELLOW_EX + "\nEnter the new file name : " + Style.RESET_ALL)
        p = Path(base_path) / name
        if not p.exists():
            with open(p, 'w') as fs:
                while True:
                    time.sleep(0.5)
                    ask = input(Fore.CYAN + "\nDo you want to write anything inside the file? (Y or N)\n->" + Style.RESET_ALL)

                    if ask.lower() == "y":
                        data = input(Fore.LIGHTWHITE_EX + "\nWrite:\n-> " + Style.RESET_ALL)
                        fs.write(data)
                        print(Fore.LIGHTBLACK_EX + "Creating file..." + Style.RESET_ALL)
                        time.sleep(2)
                        print(Fore.GREEN + "\nFile successfully created!" + Style.RESET_ALL)
                        time.sleep(1)
                        break

                    elif ask.lower() == "n":
                        print(Fore.LIGHTBLACK_EX + "Creating file..." + Style.RESET_ALL)
                        time.sleep(2)
                        print(Fore.GREEN + "\nFile created successfully!" + Style.RESET_ALL)
                        time.sleep(1)
                        break

                    else: print("Enter (Y or N)")

        else: print(Fore.RED + "\nThe file already exists." + Style.RESET_ALL)
    except Exception as error:
        print(Fore.RED + f"\nError : {error}" + Style.RESET_ALL)
            

#Defining readfile()
def readfile(base_path):
    try:
        base_path = navigate(base_path)
        time.sleep(0.5)
        name = input(Fore.LIGHTYELLOW_EX + "\nEnter the filename you want to read : " + Style.RESET_ALL)
        p = Path(base_path) / name
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                read = fs.read()
                print(Fore.LIGHTWHITE_EX + "Loading..." + Style.RESET_ALL)
                time.sleep(1)
                print(Fore.WHITE + read + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.GREEN + "\nFile read successfully!" + Style.RESET_ALL)

        else: print(Fore.RED + "\nThe file does not exist." + Style.RESET_ALL)
    except Exception as error:
        print(Fore.RED + f"\nError : {error}" + Style.RESET_ALL)

#Defining updatefile()
def updatefile(base_path):
    try:
        base_path = navigate(base_path)
        time.sleep(0.5)
        name = input(Fore.LIGHTYELLOW_EX + "\nEnter the filename you want to update : " + Style.RESET_ALL)
        p = Path(base_path) / name
        if p.exists() and p.is_file():
            time.sleep(0.5)
            print(Fore.CYAN + "\nPress 1 to change the filename" + Style.RESET_ALL)
            print(Fore.CYAN + "Press 2 to overwrite the file" + Style.RESET_ALL)
            print(Fore.CYAN + "Press 3 to add something in the file" + Style.RESET_ALL)

            resp = input(Fore.LIGHTYELLOW_EX + "Enter: " + Style.RESET_ALL)
            if resp == "1":
                time.sleep(1)
                name2 = input(Fore.LIGHTMAGENTA_EX + "New filename : " + Style.RESET_ALL)
                p2 = Path(name2)
                p.rename(p2)
                print("Finalizing...")
                time.sleep(1.5)
                print(Fore.GREEN + "\nFile updated successfully!" + Style.RESET_ALL)

            elif resp == "2":
                time.sleep(1)
                data = input(Fore.LIGHTMAGENTA_EX + "\nEnter something you want to overwrite\n-> " + Style.RESET_ALL)
                with open(p, 'w') as fs:
                    fs.write(data)
                time.sleep(1.5)
                print(Fore.GREEN + "\nFile updated successfully!" + Style.RESET_ALL)
            
            elif resp == "3":
                time.sleep(1)
                data = input(Fore.LIGHTMAGENTA_EX + "\nEnter something you want to add in the file\n-> " + Style.RESET_ALL)
                with open(p, 'a') as fs:
                    fs.write(" " + data)
                time.sleep(1.5)
                print(Fore.GREEN + "\nFile updated successfully!" + Style.RESET_ALL)

            else: print(Fore.RED + "\nInvalid input." + Style.RESET_ALL)


        else: print(Fore.RED + "\nThe file does not exist." + Style.RESET_ALL)



    except Exception as error:
        print(Fore.RED + f"\nError : {error}" + Style.RESET_ALL)

#Defining deletefile()
def deletefile(base_path):
    try:
        base_path = navigate(base_path)
        time.sleep(0.5)
        name = input(Fore.LIGHTYELLOW_EX + "\nEnter the filename you want to delete : " + Style.RESET_ALL)
        p = Path(base_path) / name
        if p.exists() and p.is_file():
            os.remove(p)
            print(Fore.LIGHTBLACK_EX + "\nDeleting file..." + Style.RESET_ALL)
            time.sleep(1.5)
            print(Fore.GREEN + "File deleted successfully!" + Style.RESET_ALL)
        else: print(Fore.RED + "\nThe file does not exist." + Style.RESET_ALL)


    except Exception as error:
        print(Fore.RED + f"\nError : {error}" + Style.RESET_ALL)


while True:
    #Interface
    time.sleep(1)
    print(Fore.LIGHTWHITE_EX + "\n-File handling options-" + Style.RESET_ALL)
    print(Fore.CYAN + "Press 1 to create a file" + Style.RESET_ALL)
    print(Fore.CYAN + "Press 2 to read a file" + Style.RESET_ALL)
    print(Fore.CYAN + "Press 3 to update a file" + Style.RESET_ALL)
    print(Fore.CYAN + "Press 4 to delete a file" + Style.RESET_ALL)
    print(Fore.CYAN + "Press E to Exit" + Style.RESET_ALL)

    response = input(Fore.YELLOW + "Response : " + Style.RESET_ALL)

    if response == "1":
        createfile(base_path)
    elif response == "2":
        readfile(base_path)
    elif response == "3":
        updatefile(base_path)
    elif response == "4":
        deletefile(base_path)
    elif response.lower() == "e":
        exit()