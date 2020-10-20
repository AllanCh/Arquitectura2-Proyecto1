class Block:

    def __init__(self, dir, val, state = "MEM"):
        self.state = state
        self.dir = dir
        self.val = val

    def setState(self, state):
        self.state = state

    def setVal(self, val):
        self.val = val

    def setDir(self, dir):
        self.dir = dir

    def getState(self):
        return self.state

    def getVal(self):
        return self.val
    
    def getDir(self):
        return  self.dir
