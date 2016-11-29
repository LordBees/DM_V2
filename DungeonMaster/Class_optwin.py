from tkinter import *
#import Class_mainwin, Class_dicerollerwin, Class_createcharwin#, Class_optwin

#import standard libs 
import BeeLibv3 as Blib
import Common

class optwin:##options window
             ##working on options as an improvement to my existing project for the next development cycle
    #CHANGED= True
    OPTIONSNAME = 'OPTIONS.CFF'
    optionssnapshot = []
    optionsmain=[]

    

    def __init__(self,masterwin,mega_main_datafile):
        self.This_win = masterwin
        self.datamain = mega_main_datafile

        #self.This_win = Toplevel()
        self.This_win.title('Options Menu')
        self.This_win.geometry('600x200')
        ##tk vars
        self.load_RCL_BTN_VAR = IntVar()
        self.load_RCL_BOX_VAR = StringVar()
        self.load_UPDATE_RM_BTN = IntVar()

        ##widgets
        
        load_LF = LabelFrame(self.This_win,text = 'resume last loaded character sheet')
        load_RCL_BTN = Checkbutton(load_LF,text = 'load file at startup',variable = self.load_RCL_BTN_VAR).grid(row=0,column=0)
        load_RCL_BOX = Entry(load_LF,textvariable = self.load_RCL_BOX_VAR).grid(row=0,column=1)
        load_UPDATE_RM_BTN = Checkbutton(load_LF,text = 'auto update roll modifiers',variable = self.load_UPDATE_RM_BTN).grid(row=1,column=0) 
        load_LF.place(x=5,y=5)

        main_SAV_BTN = Button(self.This_win,text = 'save changes',command = self.savedata).place(x=100,y=100)
        ## post widget code
        self.This_win.after(1500,self.Alt_loop)
        self.This_win.mainloop()
        
    def __del__(self):##checks for changes to the options when closed so user can save if they want to if changes not saved
        self.Alt_loop()##forces update check
        for x in range(len(self.optionsmain)):
            if self.optionsmain[x] == self.optionssnapshot[x]:
                if askokcancel('unsaved changes','some changes are unsaved\ndo you want to save?'):
                    self.datamain.replacedata([OPTIONSNAME,self.savedata])

    def Alt_loop(self):
        ##additional event loop code here

        ##end
        self.This_win.after(1500,self.Alt_loop)
        
    def get_load(self):
        return load_RCL_BTN_VAR.get()
    
    def get_ALL(self):
        return[
            self.get_load()
            ]
    def savedata(self):
        retdata = []
        temp = []

        ##loadoptions
        temp.append(str(load_RCL_BTN_VAR.get()))
        retdata.append(array2csv(temp))
        temp=[]
        return retdata