# Constructor, Self and Comparing Objects


class Computer:
    def __init__(self):
        self.name = "Udoy"
        self.age = 17

    def update(self):
        self.age = 29
    
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 20
c2 = Computer()

if c1.compare(c2):
    print("There are same")
else:
    print("There are different")

# c1.name = "Saifur"

# print(c1.age)
# c1.update()

print(c1.name)
print(c1.name)
# print(c1.age)