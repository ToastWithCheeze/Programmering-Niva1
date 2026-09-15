ålder = int(input("Hur gammal är du? "))

if ålder == 17:
    print("Du är lika gammal som de flesta i EE25.")

if ålder != 43:
    print("Du är inte lika gammal som Per!")
else:
    print("Du är lika gammal som Per.")

if ålder <= 13:
    print("Du är väldig ung. ")
elif ålder <=18:
    print("Du får inte ta körkortet.")
elif ålder <= 20:
    print("Du får ta körkort")
else:
    print("Du får handla på systembolaget.")

name = input("Vad heter du? ")

if name == "Adrian":
    print("You very noob icl tsk tsk.")
elif name != "Theo":
    print("Du heter inte Theo.")
else: 
    print("Du heter Theo.")