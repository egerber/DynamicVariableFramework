from DynamicVariable import *
from Connector import *

class DynamicSystem():

    def __init__(self,inputVariables=None,timedependentVariables=None,connections=None):
        self.timedependentVariables=timedependentVariables
        self.inputVariables=inputVariables
        self.connections=connections

    def __call__(self,inputs=None):

        if(not inputs is None):
            for var,inp in zip(self.inputVariables,inputs):
                var.assign(inp)
        if(not self.timedependentVariables is None):
            for var in self.timedependentVariables:
                var.tick()

        if(not self.connections is None):
            for connection in self.connections:
                connection.tick()


if __name__=='__main__':

    subject=StaticConvergingVariable(10.,0.2)
    reference=StaticConvergingVariable(5.,0.9)
    reference.assign(100.)
    expr_condition=lambda subj,ref: subj<0.5*ref
    expr_update=lambda subj,ref: (ref-subj)*0.4
    var_update=DynamicVariable(None)

    connection=DynamicConnection(subject,reference,expr_condition,expr_update,var_update)

    system=DynamicSystem(inputVariables=[reference],timedependentVariables=[subject,reference],connections=[connection])

    for i in range(100):
        system()
        print((subject.value,reference.value))