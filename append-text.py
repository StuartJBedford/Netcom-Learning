content = input("Enter text you would like added to file: ")
file_path = input("Enter the filename you want to add text to: ")
append_text_to_file = (file_path, content)

def append_text_to_file(file_path, content):
    try:
        with open("sudo " + file_path, 'a') as file:
            file.write(content + '\n')
        print(f"Text appended to {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")
        
         
        
append_text_to_file()