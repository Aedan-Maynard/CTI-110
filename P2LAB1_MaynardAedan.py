#Aedan Maynard
#9/30/2024
#P2LAB1
#Using imported library, math, and f-string

#Import math library
import math

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate diamater
diameter = 2 * radius

#Display diameter with one decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate Circumference

CFE = 2 * math.pi * radius

#Display circumference with two decimal place
print(f"The circumference of the circle is {CFE:.2f}\n")

#Caclulate Area

area = math.pi * radius **2

#Display area with two decimal place
print(f"The area of the circle is {area:.3f}\n")

