#Creates a list with miles/gallon
miles_by_gallon = input("Ange din (miles/gallons) så här: ").split("/")
#Extracts the variables from the list
miles = int(miles_by_gallon[0])
gallon= int(miles_by_gallon[1])

#Converts to metric
kilometers = round(miles * 1.609,2)
liter = round(gallon * 3.785,1)

#Prints result
print(f"Då blir det {kilometers}km/{liter}L")

