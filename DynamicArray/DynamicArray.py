import numpy as np
from DynamicVariable.DynamicVariable import DynamicVariable

#Dynamic Array implements the same methods as DynamicVariable but holds a numpy array
class DynamicArray(DynamicVariable):

    def __init__(self,value_array):
        self.value=np.array(value_array)

    def __getitem__(self, item):
        return self.value[item]

    ##this method will be overriden
    def __setitem__(self, key, value):
        pass

    ##this method will be overloaded by each class inherting from DynamicVariable in order to deal with assignments of this variable
    def assign(self, new_value):
        self.value=new_value


if __name__=='__main__':
    var=DynamicArray([1,2,3,4,5])
    print(var[0])
    var[0]=10
