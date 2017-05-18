if __name__=='__main__':
    from DynamicVariable import *
    from ClippedVariable import *
else:
    from .DynamicVariable import DynamicVariable
    from .ClippedVariable import ClippedVariable


class MomentumVariable(DynamicVariable):

    #value is normal variable, last_update are instances of DynamicVariable
    def __init__(self, value, momentumrate, updater):
        self.last_update=0.
        self.value=value
        self.momentumrate=momentumrate
        self.updater=updater

    def __call__(self, new_value=None):
        if not new_value is None:
            _new_change=new_value+self.momentumrate*self.last_update - self.value
            update=self.updater(_new_change)
            self.value=self.value+update
            self.last_update=update
        return self.value

if __name__=='__main__':

    var=MomentumVariable(value=1, momentumrate=0.95, updater=ClippedVariable(0.0, -10., 10.))
    var_before=var.value
    for i in range(1000):
        var+=0.1

        print(var.value-var_before)
        var_before=var.value