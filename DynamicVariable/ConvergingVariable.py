if __name__=='__main__':
    from DynamicVariable import DynamicVariable
    from TimeDependentVariable import TimeDependentVariable
    from MomentumVariable import MomentumVariable
else:
    from .TimeDependentVariable import TimeDependentVariable

class ConvergingVariable(TimeDependentVariable):

    #lambda_update_up and #lambda_update_down have to be lambda expressions taking currentValue,targetValue and returning update value
    #update value is saved in update which is a dynamicVariable (e.g. momentumRate, delayed, clipped)
    def __init__(self,value,lambda_updater_up,lambda_updater_down,updateVar):
        self.value=value
        self.target_value=self.value

        self.updater_down=lambda_updater_down
        self.updater_up=lambda_updater_up
        self.updateVar=updateVar

    def tick(self):
        self.value+=self.updateVar.value

    def assign(self,new_value):
        self.target_value=new_value
        if(self.target_value>self.value):
            self.updateVar.assign(self.updater_up(self.value,self.target_value))
        else:
            self.updateVar.assign(self.updater_down(self.value,self.target_value))

    


if __name__=='__main__':
    MomentumVariable(10,0.9,DynamicVariable(10))

