import numpy as np
from DynamicVariable import DynamicVariable


#TODO override all operation methods to return random element
class NormalDistributedVariable(DynamicVariable):

    def __init__(self,mean,std):
        self.mean=mean
        self.std=std
        self.value=np.random.normal(loc=mean,scale=std)

    def __call__(self, new_value=None):
        if not new_value is None:
            self.value=new_value
        return self.value


    def tick(self):
        self.value=np.random.normal(loc=self.mean,scale=self.std)




if __name__=='__main__':
    var=NormalDistributedVariable(1.,0.2)
    print(var.value)
    print(var)
    a=var
    print(a)

