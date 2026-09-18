import random

#Skapar en loop för att kunna slå tärningen hur många gånger som helst
while True:
    input("Tryck någon knapp för att slå tärningen")
    ditt_slag = random.randint(1,6)
    datorns_slag = random.randint(1,6)
    print(f"Du fick {ditt_slag}")
    print(f"Datorn slog {datorns_slag}\n")
    if ditt_slag == datorns_slag:
        print("Ni slog lika")
    elif ditt_slag > datorns_slag:
        skillnad = ditt_slag - datorns_slag
        print(f"Du slog högre med {skillnad}")
        break
    elif ditt_slag < datorns_slag:
        skillnad = datorns_slag - ditt_slag
        print(f"Dator slog högre med {skillnad}")
