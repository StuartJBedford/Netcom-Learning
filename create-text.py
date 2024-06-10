import os

def create_text():
    confirm = "N"
    while confirm != "Y":
        filename = input("Enter the name of the text file to create: ")
        filename = filename + ".txt"
        print("Create file name '" + filename + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo touch " + filename)
    
create_text()