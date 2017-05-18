from DynamicArray.DynamicArray import *

class MomentumArray(DynamicArray):

    def __init__(self,value_array,momentum_factor,updater):

        self.value=np.array(value_array)
        self.momentum_factor=momentum_factor
        self.updater=updater

        self.last_update=np.zeros(len(value_array))

    def __call__(self, new_value_array=None):
        if not new_value_array is None:
            _new_change=new_value_array+self.momentumrate*self.last_update - self.value
            update=self.updater(_new_change)
            self.value=self.value+update
            self.last_update=update

        return self.value

