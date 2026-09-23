inventory = []

class weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.equipped_by = None
#Simplier way of creating items/adding items to a list
stick = weapon("Stick", 20)
inventory.append(stick)
bread = weapon("bread", 4)
inventory.append(bread)

#more compact way of creating items
def create_weapon(name, damage):
    global inventory
    item = weapon(name, damage)
    inventory.append(item)
#    return item

create_weapon("Potato", 8)


print(inventory[0].name)

print("\n--- Inventory Contents ---")
for weapon in inventory:
    print(f"- {weapon.name} (Damage: {weapon.damage})")