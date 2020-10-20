import random
from numpy import random as rand
class InstGen:

    def __init__(self,mu,sigma):
        self.mu = mu
        self.sigma = sigma

    def getInstruction(self):
        inst = random.gauss(self.mu,self.sigma) 
        if(inst < 130 and inst > 75):
            return ["Calc"]
        else:
            dir = rand.poisson(2,1)
            bindir = bin(dir[0])[2:].zfill(4)
            if(inst <= 75 ):
                return ["Write",bindir]
            else:
                return ["Read",bindir]


    

gen = InstGen(100,25)
