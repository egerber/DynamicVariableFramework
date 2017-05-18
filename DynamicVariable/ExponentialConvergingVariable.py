if __name__ == '__main__':
    from DynamicVariable import DynamicVariable
    from TimeDependentVariable import TimeDependentVariable
else:
    from .DynamicVariable import DynamicVariable
    from .TimeDependentVariable import TimeDependentVariable



#at each tick, the difference of target and current value gets reduced by factor 'exponential_factor'
class ExponentialConvergingVariable(TimeDependentVariable):

    def __init__(self,value,exponential_factor,difference):
        self.exponential_factor=exponential_factor
        self.value=value
        self.target_value=value
        self.difference=difference

    def __call__(self, new_value=None):
        if not new_value is None:
            self.target_value=new_value

    def tick(self):
        self.difference.tick(self.target_value - self.value)

        self.value=self.value+self.difference.value*self.exponential_factor


if __name__=='__main__':
    var=ExponentialConvergingVariable(10,0.2,DynamicVariable(0.))
    var.__call__(50)

    for i in range(30):
        print("currentValue",str(var.value))
        var.tick()


#class ConvergingVariable
# converger_up
# converger_down

