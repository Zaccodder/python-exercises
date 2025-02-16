"""Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

full_name = (f_name + ' ' + l_name).split()

print(f"{full_name[1]} {full_name[0]}")
