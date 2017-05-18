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

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()

    ##this method will be overloaded by each class inherting from DynamicVariable in order to deal with assignments of this variable
    def __call__(self, new_value=None):
        if not new_value is None:
            self.value=new_value
        return self.value


if __name__=='__main__':
    var=DynamicArray([1,2,3,4,5])
    for el in var:
        print(el)
