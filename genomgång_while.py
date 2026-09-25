import time
import math

#utskrift av all tal mellan 1 och 10

x = 1

while x <= 10:
    print(x)
    x += 1

print("\n")

#utskrift av jämna tal

k = 0

while True:
    n = int(input("n?, skrev ett tal mindre än eller lika med 0 för att avsluta "))
    start = time.time()

    if n <= 0:
        break

    summa = 0
    k = 1

    while k <= n:
        summa += k
        k += 1

    stop = time.time()

    print(f"Summan blir {summa}. Det tog {round(stop-start)} sekunder att räkna ut")
    




