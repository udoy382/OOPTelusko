# Inheritance

class A:
    def feature1(self):
        print("Feature 1 working")

    def Feature2(self):
        print("Feature 2 working")

class B(A):
    def feature3(self):
        print("Feature 3 working")

    def Feature4(self):
        print("Feature 4 working")

class C(B):
    def Feature5(self):
        print("Feature 5 working")

a1 = A()
a1.feature1()
a1.Feature2()

b1 = B()
b1.feature1()

c1 = C()
c1.feature3()