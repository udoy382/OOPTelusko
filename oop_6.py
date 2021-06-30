# inner class

class Student:
    def __init__(self, name, roolno):
        self.name = name
        self.roolno = roolno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roolno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i3'
            self.ram = 4

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Udoy', 1)
s2 = Student('Jenny', 3)

# print(s1.name, s1.roolno)

s1.show()

# lap1 = s1.lap
# lap2 = s1.lap

# print(id(lap1))
# print(id(lap2))

# lap1 = Student.Laptop() # cant use this

s1.show()