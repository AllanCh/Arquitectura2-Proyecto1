# import the required libraries  
import numpy as np
import matplotlib.pyplot as plt  
import random
from numpy import random as rand
    
# store the random numbers in a list  
nums = []  
mu = 100
sigma = 25
    
for i in range(1000):  
    #s = random.gauss(mu,sigma)  
    s = rand.poisson(3,1)
    print(s[0])
    nums.append(s[0])
    
    
        
# plotting a graph  
plt.hist(nums, bins = 200)  
plt.show() 