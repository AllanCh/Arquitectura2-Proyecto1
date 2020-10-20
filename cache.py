import setCache

class Cache:
    def __init__(self):
        self.set0 = setCache.SetCache()
        self.set1 = setCache.SetCache()

    def read(self, dir):
        if(dir[-1] == "0"):
            return [self.set0.getBlockState(dir[0:3]),self.set0.readBlock(dir[0:3])]
        else: 
            return [self.set1.getBlockState(dir[0:3]),self.set1.readBlock(dir[0:3])]

    def write(self, dir, val):
        if(dir[-1] == "0"):
            return self.set0.writeBlock(dir[0:3], val)

        else:
            return self.set1.writeBlock(dir[0:3], val)
    
    def replace(self, dir, val, state):
        if(dir[-1] == "0"):
            response = self.set0.replaceBlock(0, dir[0:3], dir, val, state, 0)
            if(response[0] == "WriteBack"):
                response[1] = response[1] + "0"
            return response
        else:
            response = self.set1.replaceBlock(0, dir[0:3], dir, val, state, 0)
            if(response[0] == "WriteBack"):
                response[1] = response[1] + "1"
            return response

    def getBlockState(self, dir):
        if(dir[-1] == "0"):
            return self.set0.getBlockState(dir[0:3])
        else: 
            return self.set1.getBlockState(dir[0:3])

    def setBlockState(self, dir, state):
        if(dir[-1] == "0"):
            return self.set0.setBlockState(dir[0:3], state)
        else: 
            return self.set1.setBlockState(dir[0:3], state)
