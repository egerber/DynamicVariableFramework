from .TimeDependentVariable import TimeDependentVariable

class StaticConvergingVariable(TimeDependentVariable):

    def __init__(self,value,stepsize_convergence):
        self.stepsize_convergence=stepsize_convergence
        self.value=value
        self.target_value=value

    def assign(self,new_value):
        self.target_value=new_value

    def tick(self):
        if abs(self.target_value-self.value)<self.stepsize_convergence:
            self.value=self.target_value
        elif self.target_value>self.value:
            self.value=self.value+self.stepsize_convergence
        else:
            self.value=self.value-self.stepsize_convergence

if __name__=='__main__':
    var=StaticConvergingVariable(10,0.5)
    var.assign(8.3)
    for i in range(10):
        print("currentValue: ",str(var.value))
        var.tick()
