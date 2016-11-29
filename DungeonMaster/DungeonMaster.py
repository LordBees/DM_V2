##d&d char sheet
##imports
import os,sys,random##packages
#from tkinter import *#tk
#from tkinter import messagebox,filedialog##specific imports testing
import tkinter as tk
import MEGA##custom lib
##classes imports
import Class_mainwin#, Class_dicerollerwin, Class_createcharwin, Class_optwin


#code


##actually starts the tkinter program and loads data file 
if __name__ == '__main__':
    ##preload
    datamain = MEGA.mega2('DATA')##loads main data file
    
    #tk win stuff
    root = tk.Tk()#establish root here instead of in window class
    app = Class_mainwin.main_win(root,datamain)
    root.mainloop()
    
#m = Class_mainwin.main_win()##actually instanciates the window