class test1:
    def __init__(self):
        self.name = "test1"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
class test2:
    def changeName(self, obj):
        obj.setName("Test2")

class test3:
    def readName(self, obj):
        print(obj.getName())

obj1 = test1()
print(obj1.getName())
obj2 = test2()
obj2.changeName(obj1)
obj3 = test3()
obj3.readName(obj1)
string = "0110"
print(string[0:3])

