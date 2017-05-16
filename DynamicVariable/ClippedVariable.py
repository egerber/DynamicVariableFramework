from .DynamicVariable import DynamicVariable


class ClippedVariable(DynamicVariable):

    def __init__(self,value,min,max):
        self.min=min
        self.max=max
        self.assign(value)

    def assign(self, new_value):
        self.value=max(min(new_value, self.max),self.min)


if __name__=='__main__':
    var=ClippedVariable(0.25,0.2,0.3)
    print(var.value)
    var+=0.3
    print(var.value)