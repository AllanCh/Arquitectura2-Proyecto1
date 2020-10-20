import cache
import moesi

class CacheController:

    def __init__(self):
        self.cache = cache.Cache()
        self.moesi = moesi.Moesi()

    def readInst(self, dir):
        state = self.cache.getBlockState(dir)
        if(state != "MISS" and state != "I"):
            self.cache.setBlockState(dir,self.moesi.getResultingState(state,"PrRd")[0])
            return self.cache.read(dir)
        else:
            return  "MISS"

    def writeInst(self, dir, val):
        state = self.cache.getBlockState(dir)
        if(state != "MISS" and state != "I"):
            self.cache.setBlockState(dir,self.moesi.getResultingState(state,"PrWr")[0])
            return self.cache.write(dir,val)
        else:
            return  "MISS"
    
controller = CacheController()
print(controller.cache.replace("0000","1","M"))
print(controller.cache.replace("0010","3","M"))
print(controller.cache.replace("0100","2","M"))
print(controller.cache.replace("0000","1","M"))
print(controller.writeInst("0111","3"))
print(controller.readInst("0100"))
        
