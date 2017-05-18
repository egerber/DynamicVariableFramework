import numpy as np

from DynamicArray import *


class ClippedArray(DynamicArray):

    def __init__(self,value_array,min,max):
        self.min=min
        self.max=max

        self.value=np.array(value_array)

    def __setitem__(self, key, new_value):
        self.value[key]=self.value=max(min(new_value, self.max),self.min)

    def __call__(self, new_value=None):
        if not new_value is None:
            np.clip(new_value,a_min=self.min,a_max=self.max,out=self.value)
        return self.value

if __name__=='__main__':
    arr=ClippedArray([1,2,3,3,4,5,6],0.0,2.3)