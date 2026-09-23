inventory = []

class weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.equipped_by = None
stick = weapon("Stick", 20)

inventory.append(stick)

print(inventory[0].name)

print("\n--- Inventory Contents ---")
for weapon in inventory:
    print(f"- {weapon.name} (Damage: {weapon.damage})")