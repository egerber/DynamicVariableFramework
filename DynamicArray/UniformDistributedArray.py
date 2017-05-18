if __name__=='__main__':
    from DynamicArray import DynamicArray
else:
    from .DynamicArray import DynamicArray

import numpy as np

#TODO override all operation methods to return random element
class UniformDistributedArray(DynamicArray):

    def __init__(self,count_items,min,max):
        self.count_items=count_items
        self.min=min
        self.max=max
        self.value=np.random.uniform(low=min,high=max,size=(count_items))

    def __call__(self, new_value=None):
        if not new_value is None:
            self.value=new_value
        return self.value


    def tick(self):
        self.value=np.random.uniform(low=self.min,high=self.max,size=(self.count_items))

if __name__=='__main__':
    var=UniformDistributedArray(10,0.,0.2)
    var.tick()
    print(+var)
    var.tick()
    print(+var)