import math
#Asks abt variables
x1 = int(input("Ange x1: "))
x2 = int(input("Ange x2: "))
y1 = int(input("Ange y1: "))
y2 = int(input("Ange y2: "))
#Uses formula to calculate distance
answer = round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)

print(f"Distansen är {answer}")
