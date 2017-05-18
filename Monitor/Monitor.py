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
#style.use('ggplot')

class Monitor():

    #resolution: specify after how many iterations the graphics are updated
    #interval: specify how many values from the past are plotted
    def __init__(self,system,inputs=None,resolution=10,interval=100):
        self.system=system
        self.inputs=inputs
        self.resolution=resolution
        self.interval=interval
        self.logger=Logger()

        self.var_names=[]
        self.plot_types=[]
        self.axis=[]
        self.plotted_objects=[]


    def initAnimation(self):
        return tuple(self.plotted_objects)

    def tick(self,i):
        self.system.tick()
        self.logger.tick()

        if(i%self.resolution == 0):
            for draw_obj,name,plot_type in zip(self.plotted_objects,self.var_names,self.plot_types):


                if(plot_type=="Lines"): #draw dynamicArray

                    ys=self.logger[name][-self.interval:]
                    ys=np.transpose(ys)
                    xs=np.arange(len(ys[0]))

                    for y,single_obj in zip(ys,draw_obj):
                        single_obj.set_data(xs,y)

                elif plot_type=="Line": #draw dynamicVariable
                    ys=self.logger[name][-self.interval:]
                    draw_obj.set_data(np.arange(len(ys)),ys)

                elif plot_type=="Histogram":
                    pass
                    ys=self.logger[name]

                    n, _ = np.histogram(ys, 10, normed=True)
                    for rect, h in zip(draw_obj, n):
                        rect.set_height(h)

            #self.ax.set_xlim(0,len(ys))
            #self.ax.set_ylim(min_y,max_y)

        return tuple(self.plotted_objects)

    def start(self,interval,count_timesteps,fig):
        anim = animation.FuncAnimation(fig, lambda x: self.tick(x), init_func=lambda: self.initAnimation(),
                                       frames=count_timesteps, interval=interval, blit=False)

        return anim

    def add_line(self,name,index_subplot=111,min_y=0,max_y=1):
        self.logger.add_variable(name,self.system[name])
        self.var_names.append(name)
        figure=plt.gcf()
        _ax=figure.add_subplot(index_subplot,xlim=(1,self.interval),ylim=(min_y,max_y))
        #_ax.get_xaxis().set_ticks([])
        line,=_ax.plot([],[])
        _ax.tick_params(axis='both', left='on', top='off', right='off', bottom='off', labelleft='on', labeltop='off', labelright='off', labelbottom='off')
        plt.title(name)

        self.plot_types.append("Line")
        self.plotted_objects.append(line)


    def add_lines(self,name,var_arr,index_subplot=111,min_y=0,max_y=1):

        self.logger.add_variable(name,self.system[name])
        self.var_names.append(name)

        figure=plt.gcf()
        _ax=figure.add_subplot(index_subplot,xlim=(1,self.interval),ylim=(min_y,max_y))
        lines=[_ax.plot([],[])[0] for i in range(len(var_arr))]
        _ax.tick_params(axis='both', left='on', top='off', right='off', bottom='off', labelleft='on', labeltop='off', labelright='off', labelbottom='off')
        plt.title(name)

        self.plotted_objects.append(lines)
        self.plot_types.append("Lines")


    def add_hist(self,name,index_subplot,min_x=0,max_x=1):
        self.var_names.append(name)
        self.logger.add_variable(name,self.system[name])

        figure=plt.gcf()
        _ax=figure.add_subplot(index_subplot,xlim=(min_x,max_x),ylim=(0,1))
        _,_,patches=plt.hist([0], 10, normed=1)

        plt.title(name)

        self.plotted_objects.append(patches)
        self.plot_types.append("Histogram")


    def add_matrixplot(self,name,vars,index_subplot=111):
        pass


if __name__=='__main__':
    system=DynamicSystem()
    system.add_variable(ConvergingVariable(value=10.,lambda_updater_up=lambda x,y:np.random.rand()-0.5,lambda_updater_down=lambda x,y:np.random.rand()-0.5,updater=lambda x:x),"reference")
    system.add_variable(ConvergingVariable(value=10, lambda_updater_up=lambda x,y:0.1,lambda_updater_down=lambda x,y: -0.1,
                                           updater=system.add_variable(MomentumVariable(0.,0.9,lambda x:x),"momentum_subject")),
                        "subject")


    system.add_connection(DynamicConnection(system["subject"],system["reference"],lambda subj,ref: abs(subj-ref)>0,lambda subj,ref: (ref-subj)*0.4,updater=lambda x:x), "conn_subj_ref")


    fig = plt.gcf()

    monitor=Monitor(system,inputs=None,resolution=1000,interval=50)


    monitor.add_line("reference",111,min_y=0,max_y=25)
    monitor.add_line("subject",111,min_y=0,max_y=25)
    #monitor.add_lines("test2",var_arr,222,min_y=2,max_y=10)
    #monitor.add_hist("testHist",var_arr,223,min_x=-1,max_x=1)
    fig.tight_layout()
    anim=monitor.start(1,100,fig)

   # print(anim)

    #anim = animation.FuncAnimation(fig, lambda x: monitor.tick(x), init_func=lambda: monitor.initAnimation(),
     #                              frames=200, interval=20, blit=True)
    plt.show()

