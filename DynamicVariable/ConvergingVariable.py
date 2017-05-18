if __name__=='__main__':
    from DynamicVariable import DynamicVariable
    from MomentumVariable import MomentumVariable
else:
    from .DynamicVariable import DynamicVariable

class ConvergingVariable(DynamicVariable):

    #lambda_update_up and #lambda_update_down have to be lambda expressions taking currentValue,targetValue and returning update value
    #update value is saved in update which is a dynamicVariable (e.g. momentumRate, delayed, clipped)
    def __init__(self, value, lambda_updater_up, lambda_updater_down, updater):
        self.value=value
        self.target_value=self.value

        self.updater_down=lambda_updater_down
        self.updater_up=lambda_updater_up
        self.updater=updater

    def tick(self):

        if(self.target_value>self.value):
            update=self.updater(self.updater_up(self.value, self.target_value))
        else:
            update=self.updater(self.updater_down(self.value, self.target_value))
        self.value+=update


    def __call__(self, new_value=None):
        if not new_value is None:
            self.target_value=new_value
        return self.value
    


if __name__=='__main__':
    MomentumVariable(10,0.9,DynamicVariable(10))

