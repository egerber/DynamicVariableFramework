from DynamicArray.DynamicArray import *

class CachedArray(DynamicArray):

    def __init__(self,value_array,size_cache,aggregation_func=lambda x:sum(x)):

        self.value=np.array(value_array)
        self.history=np.array([value_array for i in range(size_cache)])
        self.currentPointer=0
        self.func=np.vectorize(aggregation_func)

        #each row saves the value_array for a different timestep
        #each column holds the values for the individual indices
        self.history=np.array([value_array for i in range(size_cache+1)])

    #TODO decide if CachedArray should be a Timedependent Array and implement tick()

    def __call__(self, new_value_array=None):
        if(not new_value_array is None):
            self.history[self.currentPointer]=new_value_array
            self.value=self.func(self.history[(self.currentPointer-self.ticks_delay)%(self.ticks_delay+1)])
            self.currentPointer=(self.currentPointer+1)%(self.ticks_delay+1)
        return self.value
