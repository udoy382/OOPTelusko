# The __init__ method


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu, self.ram)


com1 = Computer('i3', 16)
com2 = Computer('intel 3', 8)

com1.config()
com2.config()