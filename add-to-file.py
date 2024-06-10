open_file = input("What file would you like to add to? ")
content = input("What would you like to add to the file? ")

with open(open_file, "a") as file:
    file.write(content + "\n")