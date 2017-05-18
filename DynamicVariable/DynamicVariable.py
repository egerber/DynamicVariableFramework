import numpy as np
import timeit

class DynamicVariable:

    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return self.value+other

    def __radd__(self,other):
        return other+self.value

    def __iadd__(self, other):
        self.__call__(self.value + other)
        return self

    def __sub__(self, other):
        return self.value-other

    def __rsub__(self,other):
        return other-self.value

    def __isub__(self,other):
        self.__call__(self.value - other)
        return self

    def __mul__(self,other):
        return self.value*other

    def __rmul__(self,other):
        return other*self.value

    def __imul__(self, other):
        self.__call__(self.value * other)
        return self

    def __truediv__(self, other):
        return int(self.value/other)

    def __rtruediv__(self, other):
        return int(other/self.value)

    def __itruediv__(self, other):
        self.__call__(int(self.value / other))
        return self

    def __floordiv__(self,other):
        return float(self.value/other)

    def __rfloordiv__(self, other):
        return float(other/self.value)

    def __ifloordiv__(self, other):
        self.__call__(float(self.value / other))
        return self

    def __pow__(self, power, modulo=None):
        return pow(self.value,power,modulo)

    def __rpow__(self, other):
        return pow(other,self.value)

    def __ipow__(self, other,modulo=None):
        self.__call__(pow(self.value, other, modulo))
        return self

    def __lshift__(self, other):
        return self.value<<other

    def __rlshift__(self, other):
        return other<<self.value

    def __ilshift__(self, other):
        self.__call__(self.value << other)
        return self

    def __rshift__(self, other):
        return self.value>>other

    def __rrshift__(self, other):
        return other>>self.value

    def __irshift__(self, other):
        self.__call__(self.value >> other)

    def __and__(self, other):
        return self.value & other

    def __rand__(self, other):
        return other & self.value

    def __iand__(self, other):
        self.__call__(self.value & other)
        return self

    def __xor__(self, other):
        return self.value ^ other

    def __rxor__(self, other):
        return other ^ self.value

    def __ixor__(self, other):
        self.__call__(self.value ^ other)

    def __or__(self, other):
        return self.value | other

    def __ror__(self, other):
        return other | self.value

    def __ior__(self, other):
        self.__call__(self.value | other)
        return self
    ##end of arithmetic operations


    def __pos__(self):
        return self.value

    def __neg__(self):
        return -self.value

    def __abs__(self):
        return abs(self.value)

    def __complex__(self):
        return complex(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __round__(self, n=None):
        return round(self.value,n)

    def __invert__(self):
        pass

    ##operations for comparing
    def __lt__(self, other):
        return self.value<other

    def __le__(self, other):
        return self.value<=other

    def __eq__(self, other):
        return self.value==other

    def __ne__(self, other):
        return self.value!=other

    def __gt__(self, other):
        return self.value>other

    def __ge__(self, other):
        return self.value>=other

    ##own methods


    ##this method will be overloaded by each class inherting from DynamicVariable in order to deal with assignments of this variable
    def __call__(self, new_value=None):
        if not new_value is None:
            self.value=new_value

        return self.value


    #def __call__(self):
        #return self.value

    #gets called at every timestep, can be overriden in order to do timedependent calculation
    def tick(self):
        pass

if __name__=='__main__':
    var=DynamicVariable(10)
    #var(10)
    var+=2
    print(var+1)