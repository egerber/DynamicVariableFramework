from DynamicVariable import *
import numpy as np

a=MomentumVariable(10,0.3,DynamicVariable(10))
conv=ConvergingVariable(10,lambda_updater_down=lambda cur,tar:-0.2,lambda_updater_up=lambda cur,tar:0.2,updateVar=a)

for i in range(100):
    print(conv.value,conv.target_value)
    conv+=2

    #if(i%5==0):
      #  conv-=8
    conv.tick()