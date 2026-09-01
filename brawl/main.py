import random

#PlayerName = input("What's your name? ")
PlayerHP = random.randint(50,200)
EnemyHP = random.randint(50,200)

print(f"HP {PlayerHP}")

#Damages player until death
while PlayerHP > 0:
    PlayerHP -= random.randint(1,20)
    if PlayerHP <= 0:
        print("Dead")
    else:
        print(f"HP: {PlayerHP}")