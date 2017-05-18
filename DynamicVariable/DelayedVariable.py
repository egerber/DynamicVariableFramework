import numpy as np
from .TimeDependentVariable import TimeDependentVariable


class DelayedVariable(TimeDependentVariable):

    ##delay
    def __init__(self,value,ticks_delay):
        self.ticks_delay=ticks_delay
        self.history=np.array([value for i in range(ticks_delay+1)])
        self.value=value
        self.currentPointer=0

    def __call__(self, new_value=None):
        if not new_value is None:
            self.history[self.currentPointer]=new_value

    def tick(self):
        self.currentPointer=(self.currentPointer+1)%(self.ticks_delay+1)
        self.value=self.history[(self.currentPointer-self.ticks_delay)%(self.ticks_delay+1)]


if __name__=='__main__':
    var=DelayedVariable(0,1)
    for i in range(20):
        print("current_value: ",str(var.value))
        print("assign "+str(i+1))
        var+=1
        var.tick()
