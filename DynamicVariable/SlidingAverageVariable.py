import numpy as np
from DynamicVariable import DynamicVariable


class SlidingAverageVariable(DynamicVariable):

    def __init__(self,value,count_timesteps):
        self.value=value
        self.count_timesteps=count_timesteps
        self.history=np.array([value for i in range(count_timesteps)])
        self.currentPointer=0

    def assign(self,new_value):
        self.currentPointer=(self.currentPointer+1)%(self.count_timesteps)
        self.history[self.currentPointer]=new_value
        self.value=np.mean(self.history)



if __name__=='__main__':

    var=SlidingAverageVariable(10,2)

    for i in range(20):
        print(var.value)
        var.assign(i)