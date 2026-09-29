class potato:
    def __init__(self, age, color):
        self.age = age
        self.color = color

p1 = potato(58,"rosa")
p2 = potato(19,"grön")

print(f"Potato 1 är {p1.age} gammal och {p1.color}")
print(f"Potato 2 är {p2.age} gammal och {p2.color}")