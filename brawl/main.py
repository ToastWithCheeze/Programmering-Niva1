import random

#PlayerName = input("What's your name? ")
playerHP = random.randint(50,200)
EnemyHP = random.randint(50,200)

print(f"HP {playerHP}")

#Damages player until death
while playerHP > 0:
    playerHP -= random.randint(1,20)
    if playerHP <= 0:
        print("Dead")
    else:
        print(f"HP: {playerHP}")