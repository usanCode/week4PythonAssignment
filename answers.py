


# Create a program that reads a file and writes a modified version to a new file.

with open("week4PythonAssignment/essai.txt", "r") as file:
    content = file.read()
    print(content)

with open("result.txt", "w") as file: 
    file.write("My name is Usanase.")
    file.write("I am happy to be here")