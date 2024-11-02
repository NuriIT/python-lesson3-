try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")  


    # this function here attempts to read a file and handles the case where file doesn't exist
    # # by catching a FileNoteFoundError      