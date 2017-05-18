from DynamicVariable import *
from Connector import *

class DynamicSystem():

    def __init__(self):

        #NOTE: this approach works only with version >=3.6 because python needs to iterate over the keys in the order in which they have been added
        self.inputVariables={}
        self.connections={}
        self.variables={}

    def add_variable(self,var,name):
        assert(not name in self.variables.keys())
        self.variables[name]=var
        return var

    def add_connection(self,connection,name):
        assert(not name in self.connections.keys())
        self.connections[name]=connection
        return connection

    def __getitem__(self,name):
        return self.variables[name]

    def tick(self, inputs=None):
        for _,var in self.variables.items():
            var.tick()

        for _,conn in self.connections.items():
            conn.tick()


if __name__=='__main__':


    system=DynamicSystem()
    system.add_variable(StaticConvergingVariable(10.,0.2),"subject")
    system.add_variable(StaticConvergingVariable(5.,0.9),"reference")

    system.add_connection(DynamicConnection(system["subject"],system["reference"],lambda subj,ref: abs(subj-ref)>5,lambda subj,ref: (ref-subj)*0.4,updater=lambda x:x), "conn_subj_ref")
    system["reference"](100)

    for i in range(100):
        system.tick()
        print(system["subject"].value,system["reference"].value)