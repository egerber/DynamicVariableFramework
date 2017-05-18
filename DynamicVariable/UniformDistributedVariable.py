import numpy as np
from DynamicVariable import DynamicVariable


#TODO override all operation methods to return random element
class UniformDistributedVariable(DynamicVariable):

    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.value=np.random.uniform(low=min,high=max)

    def __call__(self, new_value=None):
        if not new_value is None:
            self.value=new_value
        return self.value

    def tick(self):
        self.value=np.random.uniform(low=self.min,high=self.max)


if __name__=='__main__':
    var=UniformDistributedVariable(0.,0.2)
    print(var+0.)
    print(var+1.)
    var.tick()
    print(var.value)