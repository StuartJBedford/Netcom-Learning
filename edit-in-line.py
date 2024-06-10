content = input("Input the text you would like to add ")
filename = input("Specify the file you'd like to add text to ")
f2 = open("sudo "  + filename, "w")
f2.write(content)
f2.close()

