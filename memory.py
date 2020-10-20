import block

class Memory:
    def __init__(self):
        self.memory = []
        self.memory.append(block.Block("0000","0"))
        self.memory.append(block.Block("0001","0"))
        self.memory.append(block.Block("0010","0"))
        self.memory.append(block.Block("0011","0"))
        self.memory.append(block.Block("0100","0"))
        self.memory.append(block.Block("0101","0"))
        self.memory.append(block.Block("0110","0"))
        self.memory.append(block.Block("0111","0"))
        self.memory.append(block.Block("1000","0"))
        self.memory.append(block.Block("1001","0"))
        self.memory.append(block.Block("1010","0"))
        self.memory.append(block.Block("1011","0"))
        self.memory.append(block.Block("1100","0"))
        self.memory.append(block.Block("1101","0"))
        self.memory.append(block.Block("1110","0"))
        self.memory.append(block.Block("1111","0"))

    def setVal(self, dir, val):
        self.memory[dir].setVal(val)

    def getVal(self, dir):
        return self.memory[dir].getVal()

