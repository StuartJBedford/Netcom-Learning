import os
def manage_txt():
    confirm = "N"
    while confirm !="Y":
        filename = input("Enter the name of the file you would like to edit: ")
        filename = filename + ".txt"
        print("Open filename in vim editor? '" + filename + "'? (Y/N)")
        confirm = input().upper()
    os.system("vim " + filename)
    
manage_txt()