import time
import random

#Variables
player_hp = random.randint(50,200)
enemy_hp = random.randint(50,200)

def attack_player(player_hp, enemy_hp):
    ...

def attack_enemy(player_hp, enemy_hp):
    ...

def defend(player_hp):
    enemy_damage = random.randint(10,40)
    defense = random.randint(10,40)

    damage_amount = enemy_damage - defense
    if damage_amount < 0:
        damage_amount = 0
        print("You nullified the attacks")
    else:
        player_hp -= damage_amount
        print(f"You took {damage_amount} damage")
    return player_hp


def main():
    player_name = input("What's your name? ")

    #importing global variables
    global player_hp
    global enemy_hp

    print(f"{player_name} starts with {player_hp} HP")
    print(f"Enemy starts with {enemy_hp} HP\n")
    #Damages player until death
    while player_hp > 0:
        choice = input(f"You got {player_hp} HP, and Enemy got {enemy_hp} HP left\n[A]ttack or [D]efend: ").lower()
        if choice == "d":
            #Defends player Returns new player_hp value
            player_hp = defend(player_hp)
        elif choice =="a":
            #Player attacks enemy
            player_hp, enemy_hp = attack_enemy(player_hp,enemy_hp)
            #Enemy attacks player
            player_hp, enemy_hp = attack_player(player_hp,enemy_hp)
        else:
            print("Not valid choice!, Try again")

#Runs main function
main()