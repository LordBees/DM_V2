##imports
import os,sys,random##packages
##tk
from tkinter import *
#import Class_mainwin, Class_createcharwin, Class_optwin #, Class_dicerollerwin

#import standard libs 
import BeeLibv3 as Blib
import Common

class dicewin:#(Frame):#(This_win):
    #This_win = Toplevel
    #print('init')
    ##variables
    #This_win = Tk##temp
    #TK variables
    
    
    def __init__(self,masterwin,mega_main_datafile):
        #self.This_win = Toplevel()##minus the ()?
        #self.This_win = Toplevel()
        self.This_win = masterwin
        self.datamain = mega_main_datafile

        self.Diceroller_DX1_RAD_VAR = IntVar()#StringVar()
        self.Diceroller_RDR_LBL_VAR = StringVar()

        self.This_win.title('Dice roller')
        self.This_win.geometry('415x85')
        ##widgets
        Diceroller_LF = LabelFrame(self.This_win)
        Diceroller_DXX_LBL = Label(Diceroller_LF,text = 'select a dice').grid(row=0,column=0)
        Diceroller_DX1_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 4,text = 'D4').grid(row=1,column=0)##dicetypes
        Diceroller_DX2_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 8,text = 'D8').grid(row=1,column=1)
        Diceroller_DX3_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 6,text = 'D6').grid(row=1,column=2)
        Diceroller_DX4_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 12,text = 'D12').grid(row=1,column=3)
        Diceroller_DX5_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 10,text = 'D10').grid(row=1,column=4)
        Diceroller_DX6_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 100,text = 'D100').grid(row=1,column=5)
        Diceroller_DX7_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 20,text = 'D20').grid(row=1,column=6)
        Diceroller_RTD_BTN = Button(Diceroller_LF,text = 'Roll!',command = self.roll_die).grid(row=2,column=0)
        Diceroller_RDR_LBL = Label(Diceroller_LF,textvariable = self.Diceroller_RDR_LBL_VAR,text = 'you rolled a |').grid(row=2,column=1)
        Diceroller_LF.place(x=5,y=5)
        
        ## post widget code

        ##tkloop
        self.This_win.after(1500,self.Alt_loop)
        self.This_win.mainloop() 
        

    def Alt_loop(self):
        ##additional event loop code here
        print(self.get_diceroller())
        ##end
        self.This_win.after(1500,self.Alt_loop)

    #rolls dice
    def roll_die(self):##maybe problem
        d = self.get_diceroller()
        r = 0##random roll
        if str(d) == '100':
            r= (self.internal_roller(10)*10)
        elif str(d) == '0':
            r = 'No dice Selected!'
        else:
            r= self.internal_roller(int(d))
        self.set_rollerlabel(str(r)+'  ')

    ##returns random number    
    def internal_roller(self,number):
        return random.randint(0,number)

    ##gets dice type
    def get_diceroller(self):
        return self.Diceroller_DX1_RAD_VAR.get()
    
    ##sets label of output and formats
    def set_rollerlabel(self,data):
        self.Diceroller_RDR_LBL_VAR.set('you rolled a |'+str(data))