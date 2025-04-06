


# Create a program that reads a file and writes a modified version to a new file.

with open("week4PythonAssignment/essai.txt", "r") as file:
    content = file.read()
    print(content)

with open("result.txt", "w") as file: 
    file.write("My name is Usanase.")
    file.write("I am happy to be here")

# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename you want to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found. Please check the filename.")