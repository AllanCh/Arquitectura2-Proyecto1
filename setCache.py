import cacheBlock

class SetCache:
    def __init__(self):
        self.block1 = cacheBlock.CacheBlock("0000","0")
        self.block2 = cacheBlock.CacheBlock("0000","0")

    def readBlock(self, tag):
        if(self.block1.getBitVal() == 0 and self.block1.getTag() == tag):
            self.block1.setLRU(0)
            self.block2.setLRU(1)
            return self.block1.getVal()
        elif(self.block1.getBitVal() == 0 and self.block2.getTag() == tag):
            self.block1.setLRU(1)
            self.block2.setLRU(0)
            return self.block2.getVal()
        else:
            return "MISS"
    
    def writeBlock(self, tag, val):
        if(self.block1.getTag() == tag):
            self.block1.setLRU(0)
            self.block2.setLRU(1)
            self.block1.setVal(val)
            return self.block1.getVal()
        elif(self.block2.getTag() == tag):
            self.block1.setLRU(1)
            self.block2.setLRU(0)
            self.block2.setVal(val)
            return self.block2.getVal()
        else:
            return "MISS"
    
    def replaceBlock(self, bitVal, tag, dir, val, state, LRU):
        block = self.getLRUBlock()
        if(block == 1):
            prevState = self.block1.getState()
            prevVal = self.block1.getVal()
            prevTag = self.block1.getTag()
            self.block1.setBitVal(bitVal)
            self.block1.setTag(tag)
            self.block1.setDir(dir)
            self.block1.setVal(val)
            self.block1.setState(state)
            self.block1.setLRU(LRU)
            self.block2.setLRU(1)
            if(prevState == "M" or prevState == "O"):
                return ["WriteBack",prevTag,prevVal]
            else:
                return ["Done"]
        else:
            prevState = self.block2.getState()
            prevVal = self.block2.getVal()
            prevTag = self.block2.getTag()
            self.block2.setBitVal(bitVal)
            self.block2.setTag(tag)
            self.block2.setDir(dir)
            self.block2.setVal(val)
            self.block2.setState(state)
            self.block2.setLRU(LRU)
            self.block1.setLRU(1)
            if(prevState == "M" or prevState == "O"):
                return ["WriteBack",prevTag,prevVal]
            else:
                return ["Done"]
        
    def getLRUBlock(self):
        if(self.block1.getLRU() == 1):
            return 1
        elif(self.block2.getLRU() == 1):
            return 2
        else:
            return 1

    def getBlockState(self, tag):
        if(self.block1.getTag() == tag):
            return self.block1.getState()
        elif(self.block2.getTag() == tag): 
            return self.block2.getState()
        else: 
            return "MISS"

    
    def setBlockState(self, tag, state):
        if(self.block1.getTag() == tag):
            self.block1.setState(state)
        elif(self.block2.getTag() == tag): 
            self.block2.setState(state)
        else: 
            return "MISS"
