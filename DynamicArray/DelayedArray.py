from DynamicArray.DynamicArray import *

class DelayedArray(DynamicArray):

    def __init__(self,value_array,ticks_delay):
        self.value=np.array(value_array)

        self.ticks_delay=ticks_delay
        self.currentPointer=0
        #each row saves the value_array for a different timestep
        #each column holds the values for the individual indices
        self.history=np.array([value_array for i in range(ticks_delay+1)])

    def tick(self):
        self.currentPointer=(self.currentPointer+1)%(self.ticks_delay+1)
        self.value=self.history[(self.currentPointer-self.ticks_delay)%(self.ticks_delay+1)]

    def __setitem__(self, key, value):
        self.history[self.currentPointer][key]=value
        #works only if ticks_delay>0

    def __call__(self, new_value_array=None):
        if not new_value_array is None:
            self.history[self.currentPointer]=new_value_array
        return self.value

if __name__=='__main__':
    delayArray=DelayedArray([1,2,3,4,5,6,7],5)

    for i in range(100):
        delayArray+=1
        print(delayArray.value)
        delayArray.tick()
