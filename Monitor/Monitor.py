import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib import style
from Logger import *
from DynamicVariable import *
from Connector import *
from DynamicSystem import *
from DynamicArray import *

style.use("fivethirtyeight")


class Monitor():

    #resolution: specify after how many iterations the graphics are updated
    #interval: specify how many values from the past are plotted
    def __init__(self,system,inputs=None,resolution=10,interval=100):
        self.system=system
        self.inputs=inputs
        self.resolution=resolution
        self.interval=interval
        self.logger=Logger()
        self.monitored_vars=[]

        self.axes=[]
        #self.ax=plt.axes(xlim=(0, 100), ylim=(0, 100))

        self.plotted_objects=[]


    def initAnimation(self):
        for obj in self.plotted_objects:
            obj.set_data([],[])

        return tuple(self.plotted_objects)

    def tick(self,i):
        self.system()
        self.logger.tick()


        if(i%self.resolution == 0):
            min_y=10000.
            max_y=-10000.
            for draw_obj,name in zip(self.plotted_objects,self.monitored_vars):
                #grab the indices from within the range wanted
                ys=self.logger[name][-self.interval:]

                #min_y=min(min_y,min(ys))
                #max_y=max(max_y,max(ys))
                draw_obj.set_data(ys)
            #self.ax.set_xlim(0,len(ys))
            #self.ax.set_ylim(min_y,max_y)

        return tuple(self.plotted_objects)

    def start(self,interval,count_timesteps,fig):
        anim = animation.FuncAnimation(fig, lambda x: self.tick(x), init_func=lambda: self.initAnimation(),
                                       frames=count_timesteps, interval=interval, blit=False)

        return anim

    def add_line(self,name,var,index_subplot=111):
        self.logger.add_variable(name,var)
        self.monitored_vars.append(name)

        figure=plt.gcf()
        _ax=figure.add_subplot(index_subplot,xlim=(0,10),ylim=(0,100))
        line,=_ax.plot([],[])
        self.plotted_objects.append(line)

    def add_lines(self,name,var_arr,index_subplot=111):
        self.logger.add_variable(name,var_arr)
        self.monitored_vars.append(name)

        figure=plt.gcf()
        _ax=figure.add_subplot(index_subplot,xlim=(0,10),ylim=(0,100))
        lines,=_ax.plot([],[])
        self.plotted_objects.append(lines)



    def add_hist(self,name,vars):
        pass

    def add_matrixplot(self,name,vars,index_subplot=111):
        pass

    def add_variable(self,name,var,index_subplot=1):
        figure=plt.gcf()
        _ax=figure.add_subplot(2,2,index_subplot,xlim=(0,10),ylim=(0,100))


        self.logger.add_variable(name,var)
        self.monitored_vars.append(name)



# call the animator.  blit=True means only re-draw the parts that have changed.
#anim = animation.FuncAnimation(fig, animate, init_func=init,
 #                              frames=200, interval=20, blit=True)


if __name__=='__main__':
    subject=StaticConvergingVariable(10.,0.2)
    reference=StaticConvergingVariable(5.,0.9)
    reference.assign(100.)
    expr_condition=lambda subj,ref: subj<0.5*ref
    expr_update=lambda subj,ref: (ref-subj)*0.4
    var_update=DynamicVariable(None)

    #Random Array
    var_arr=UniformDistributedArray(10,0.,10.)

    #define connections
    connection=DynamicConnection(subject,reference,expr_condition,expr_update,var_update)

    system=DynamicSystem(inputVariables=[reference],timedependentVariables=[subject,reference,var_arr],connections=[connection])


    fig = plt.gcf()

    monitor=Monitor(system,inputs=None,resolution=1,interval=50)

    #monitor.add_variable("reference",reference,1)
    #monitor.add_variable("subject",subject,1)
    #monitor.add_line("test",subject,221)
    monitor.add_lines("test2",var_arr)

    anim=monitor.start(10,100,fig)
   # print(anim)

    #anim = animation.FuncAnimation(fig, lambda x: monitor.tick(x), init_func=lambda: monitor.initAnimation(),
     #                              frames=200, interval=20, blit=True)
    plt.show()

