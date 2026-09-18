import random


enemy_hp = 100
max_rounds = 5
max_damage = 20

def attack(enemy, max_damage = 20):
    while enemy > 0:
        input("Press any key to Attack")
        damage = random.randint(1,max_damage)
        enemy -= damage
        #Makes any negative integer automatically to 0
        if enemy < 0:
            enemy = 0

        print(f"You did {damage} damage, {enemy}HP left on enemy.\n ")
        if enemy > 0:
            print("Enemy are still alive!")
        elif enemy <= 0:
            print("Enemy are dead probably.")
            
def attack_rounds(enemy,max_round,max_damage = 20):
    round = 0
    while round < max_round:
        print(f"\nround {round} Starting with enemies starting on {enemy} HP\n")
        attack(enemy,max_damage)
        round += 1
    print(f"You have now played your {max_round} rounds")


attack_rounds(enemy_hp,max_rounds)