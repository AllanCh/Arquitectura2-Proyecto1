import block

class CacheBlock(block.Block):

    def __init__(self, dir, val, state = "I", tag = "", bitVal = 1, LRU = 1):
        block.Block.__init__(self, dir, val, state = "I")
        self.tag = tag
        self.bitVal = bitVal
        self.LRU = LRU

    def setTag(self, tag):
        self.tag = tag
    
    def getTag(self):
        return self.tag

    def setBitVal(self, bitVal):
        self.bitVal = bitVal

    def getBitVal(self):
        return self.bitVal

    def setLRU(self, LRU):
        self.LRU =LRU

    def  getLRU(self):
        return self.LRU


