import time
import random

class character:
    def __init__(self, hp):
        self.name = ""
        self.hp = hp
        self.damage = 0
    def attack(self, target):
        target -= self.damage
        return target
    def defend(self, enemy_damage):
        defense = random.randint(10,40)

        damage_amount = enemy_damage - defense
        if damage_amount <= 0: 
            damage_amount = 0
            print("You nullified the attacks")
        else:
            self.hp -= damage_amount
            print(f"You took {damage_amount} damage")
        return self.hp

def main():
    player = character(random.randint(50,200))
    enemy = character(random.randint(50,200))
    
    player.name = input("What's your name? ")

    print(f"{player.name} starts with {player.hp} HP")
    print(f"Enemy starts with {enemy.hp} HP\n")
    #Damages player until death
    while player.hp > 0 and enemy.hp > 0:   
        choice = input(f"You got {player.hp} HP, and Enemy got {enemy.hp} HP left\n[A]ttack or [D]efend: ").lower()
        if choice == "d":
            #Defends player Returns new player_hp value
            player.hp = player.defend(random.randint(1,10))

        elif choice =="a":
            #Player attacks enemy
            player.damage = random.randint(1,10)
            enemy.hp = int(player.attack(enemy.hp))
            print(f"You did {player.damage} damage to enemy!")
            
            #Enemy attacks player
            enemy.damage = random.randint(1,10)
            player.hp = int(enemy.attack(player.hp))
            print(f"\nEnemy did {enemy.damage} damage on you!\n")
        else:
            print("Not valid choice!, Try again")
    
    
    if player.hp <= 0:
        print("Enemy Won!")
    elif enemy.hp <= 0:
        print("Player Won!")

#Runs main function
main()