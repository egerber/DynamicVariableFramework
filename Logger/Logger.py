import json

import codecs
import numpy as np
import os
from DynamicVariable import DynamicVariable
from collections import defaultdict
from DynamicVariable.ExponentialConvergingVariable import ExponentialConvergingVariable


#logs any variable overtime
#frequency determines after how many timesteps (ticks) the value gets saved
class Logger():

    def __init__(self):
        self.vars={}
        self.logs=defaultdict(list)
        self.iterations=0



    def tick(self):
        for name,var in self.vars.items():
            self.logs[name].append(var.value)

    def add_variable(self,name,variable):
        self.vars[name]=variable
        self.logs[name]=[]

    def save(self,filename):
        json.dump(self.logs,codecs.open(filename,'w',encoding='utf-8'),separators=(',',':'))

    def __getitem__(self, name):
        return self.logs[name]


if __name__=='__main__':
    exp=ExponentialConvergingVariable(10,0.02,DynamicVariable(None))
    dyn=DynamicVariable(10)

    logger=Logger()
    logger.add_variable("exponential",exp)
    logger.add_variable("dynamic",dyn)

    for i in range(1000):
        exp.assign(np.random.rand()*100.)
        dyn.assign(np.random.rand()*100)
        exp.tick()
        logger.tick()


