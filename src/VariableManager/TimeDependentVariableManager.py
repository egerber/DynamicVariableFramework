import numpy as np

from DynamicVariable import DelayedVariable


class TimeDependentVariableManager():

    #tuples_var_freq = [(var1, freq1),(var2, freq2), (var3, freq3)]
    def __init__(self,tuples_var_freq):
        self.vars=[pair[0] for pair in tuples_var_freq]
        self.update_frequencies=[pair[1] for pair in tuples_var_freq]
        self.iterations=0

    def add_variable(self,var,update_frequency):
        self.vars.append(var)
        self.update_frequencies.append(update_frequency)

    def tick(self):
        for var,freq in zip(self.vars,self.update_frequencies):
            if(self.iterations % freq == 0 ):
                var.tick()

        self.iterations+=1


if __name__=='__main__':
    var1= DelayedVariable(0.1, 6)
    var2= DelayedVariable(0.4, 3)
    manager=TimeDependentVariableManager([(var1,2),(var2,1)])
    for i in range(100):
        var1+=np.random.rand()
        var2+=np.random.rand()
        manager.tick()

    print(var1.value,var2.value)

