player = input("Vad heter du? ")

print(f"Hej {player}")

choice = input("Vars vill du gå Höger elr Vänster?? ")

if choice.lower() == "Höger":
    print("Du drar åt Höger")
else:
    print("Du drar åt Vänster")
