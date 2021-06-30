# Duck Typing

class Pycharm:

    def execute(self):
        """ This is a dock typing"""
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = Pycharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)