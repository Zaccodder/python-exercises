"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

# calculate area of a circle
# the formular is area = #r2

from math import pi

r = float(input("enter radius of a circle: "))


area = pi * r * r

print(f"The area of a circle is: {area}")