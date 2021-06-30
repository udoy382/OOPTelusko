# Constructor in Inheritance


class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A working")

    def Feature2(self):
        print("Feature 2 working")

class B:
    def __init__(self):
        # super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature 1-B working")

    def Feature4(self):
        print("Feature 4 working")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().__init__()

a1 = C()
a1.feature1()