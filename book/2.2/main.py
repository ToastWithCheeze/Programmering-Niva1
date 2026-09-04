import math

radie = float(input("Vad är radien på sfären? "))

volym = round( 4 * math.pi * (radie**3) /3, 2)

area = round(4 * math.pi * (radie**2), 2)

print(f"Volymen är {volym}\nArean är {area}")