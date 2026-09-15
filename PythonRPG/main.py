import random

#playerHP: int = 100
FirstEnemyHP: int = int(100)

def attack(enemy):
    while enemy > 0:
        input("Press any key to Attack (-10)")
        enemy -= 10
        print(f"{enemy}HP left on enemy.")
        if enemy > 0:
            print("You are still alive!")
        elif enemy <= 0:
            print("You are dead probably.")



attack(FirstEnemyHP)