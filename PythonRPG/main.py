import time
import random
#Variables
player_hp = random.randint(50,200)
enemy_hp = random.randint(50,200)

def attack_player(player_hp, enemy_hp):
    ...

def attack_enemy(player_hp, enemy_hp):
    ...

def defend(player_hp, enemy_hp):
    ...

def main():
    player_name = input("What's your name? ")

    #importing global variables
    global player_hp
    global enemy_hp


    print(f"{player_name} starts with {player_hp} HP")
    print(f"Enemy starts with {enemy_hp} HP\n")
    time.sleep(3)
    #Damages player until death
    while player_hp > 0:
        choice = input(f"You got {player_hp} HP, and Enemy got {enemy_hp} HP left\n[A]ttack or [D]efend: ").lower()
        if choice == "d":
            defend(player_hp, enemy_hp)
        elif choice =="a":
            attack_enemy(player_hp,enemy_hp)
        else:
            print("Not valid choice!, Try again")

#Runs main function
main()