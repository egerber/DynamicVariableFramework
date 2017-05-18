if __name__=='__main__':
    from DynamicVariable import DynamicVariable
else:
    from .DynamicVariable import DynamicVariable

class ClippedVariable(DynamicVariable):

    def __init__(self,value,min,max):
        self.min=min
        self.max=max
        self.__call__(value)

    def __call__(self, new_value=None):
        if not new_value is None:
            self.value=max(min(new_value, self.max),self.min)
        return self.value

if __name__=='__main__':
    var=ClippedVariable(0.25,0.2,0.3)
    print(var.value)
    var+=0.3
    print(var.value)