#Aedan Maynard
#10/02/2024
#P2LAB2
#Using Dictionaries

#Create Dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

#Print Dictionary Keys
print(cars.keys())

#Get a car (key) from user
userCar = input("Enter a vehicle to see it's mpg: ")

#Display mpg fot the userCar
print(f"The {userCar} gets {cars[userCar]} mpg.")

#Get distance to be traveled in userCar
miles =int(input(f"How many miles will you drive the {userCar}? " ))

#Calculate the amount of gas required to drive (miles)
gas = miles/ cars[userCar]

print(f"{gas:.2f} gallon(s) of gas are needed to drive the {userCar} {miles} miles.")


