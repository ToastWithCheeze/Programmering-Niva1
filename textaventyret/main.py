player = input("Vad heter du? ")

print(f"Hej {player}")

choice = input("Vars vill du gå Höger elr Vänster?? ")

if choice.lower() == "höger":
    print("Du drar åt Höger, där var det väldigt kallt och du frös ihjäl.")
    
else:
    print("Du drar åt Vänster, du kommer fram till 2 färgade dörrar, blå/röd.")
    if input("Vars går du in? (blå/röd) ").lower() == "blå":
        print("Du har nått slutet, med ingen belöning och bara en återvändsgränd.")
    else:
        print("Du har hittat massa potatis säckar så det räcker för livet!")

