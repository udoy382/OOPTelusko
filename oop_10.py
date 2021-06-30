# Operator Overloading


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

#       compare two value who bigger then
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

        return s3

#       run s1 and s2 value
    def __str__(self):
        return self.m1, self.m2

s1 = Student(58, 69)
s2 = Student(660, 675)

s3 = s1 + s2
# print(s3.m1)


#       compairing code
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
    

#       s1 and s2 value run code
a = 9
print(a.__str__())
print(s1.__str__())
print(s2.__str__())