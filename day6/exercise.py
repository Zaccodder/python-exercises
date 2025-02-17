"""
write a pyhton program that accepts sequence of comma separated numbers from the user and  generate a list and tuple of those numbers.

algorith

1. get the values through  the input function as a list of comma separated numbers
2. split the value using split function
3.store it in variable
4. convert the stored value to tuple
"""


value = input("Enter list of comma separated values: " )

values = value.split(",") 
print(f"list: {values}")
print(f"tuple: {tuple(values)}")
  
       
