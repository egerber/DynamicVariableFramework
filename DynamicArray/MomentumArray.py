from DynamicArray.DynamicArray import *

class MomentumArray(DynamicArray):

    def __init__(self,value_array,momentum_factor):

        self.value=np.array(value_array)
        self.momentum_factor=momentum_factor

        self.last_update=np.zeros(len(value_array))

    def assign(self,new_value_array):
        _new_change=new_value_array+self.momentumrate*self.last_update - self.value

        self.update.assign(_new_change)

        self.value=self.value+self.update.value
        self.last_update=self.update.value

