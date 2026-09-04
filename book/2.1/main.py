import math

#Frågar Mätarställning
Mätarställning_idag = int(input("Vad är mätarställningen idag? "))
Mätarställning_år_sedan = int(input("Vad var mätarställningen för ett år sedan? "))

Körda_mil = Mätarställning_idag - Mätarställning_år_sedan
#Skriver ut Antal körda mil
print(f"Antal körda mil: {Körda_mil}")

#Frågar bensin förbrukning
Bensin_förbrukad = float(input("Hur många liter bensin har du förbrukat? "))

förbrukning_per_mil = round(Bensin_förbrukad / Körda_mil, 2)

#Skriver ut Förbrukning per mil
print(f"Förbrukning per mil: {förbrukning_per_mil}")