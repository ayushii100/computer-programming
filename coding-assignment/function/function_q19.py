 #Function for File Operations
def write_and_read_file(file_name, text):
    with open(file_name, "w") as file:
        file.write(text)
    with open(file_name, "r") as file:
        return file.read()
print(write_and_read_file("example.txt", "Hello, File!"))
