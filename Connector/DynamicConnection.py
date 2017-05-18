from DynamicVariable import DynamicVariable

class DynamicConnection:

    #lambda_condition must be a lambda expression taking 2 arguments and returning a boolean value
    #lambda_update has to be a lambda expression taking 2 arguments and returning a float value
    def __init__(self,subject,reference,lambda_condition,lambda_update,updater):
        self.subject=subject
        self.reference=reference
        self.lambda_condition=lambda_condition
        self.lambda_update=lambda_update
        self.updater=updater

    def tick(self):
        if(self.lambda_condition(self.subject,self.reference)):
            update=self.updater(self.lambda_update(self.subject, self.reference))
            self.subject+=update



if __name__=='__main__':

    subject=DynamicVariable(10.)
    reference=DynamicVariable(5.)
    expr_condition=lambda x,y: x>y
    expr_update=lambda x,y: (y.value-x.value)*0.1
    var_update=DynamicVariable(None)
    connection=DynamicConnection(subject=subject,reference=reference,lambda_condition=expr_condition,lambda_update=expr_update,updater=lambda x:x)

    for i in range(100):
        connection.tick()
        print(subject.value)