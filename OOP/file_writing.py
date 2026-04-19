# Python writing files

txt_data = "I like Pizza!"
file_path = "output.txt"

try:
    # mode=x writes a file if it does not already exist
    with open(file=file_path, mode="x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")
