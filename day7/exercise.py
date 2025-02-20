"""
    Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
    """

val = input("Enter a name of  a file with it's extension: ")

result = val.split(".")

print(result[1])