class InventoryShopperwin:##inventory shop manager(buy/sell items for gold here)
    
    def __init__(self,masterwin,mega_main_datafile):
        self.This_win = masterwin
        self.datamain = mega_main_datafile
        ##code








        ##end code
        #self.This_win.config(menu=Menu_main)##attach menu to window
        self.This_win.after(1500,self.Alt_loop)##alternate event loop for other parts of code(seperate event loop hooked intotkinters primary event loop)
        self.This_win.mainloop()
        ##end init



    def Alt_loop(self):
        ##additional event loop code here

        ##end
        self.This_win.after(1500,self.Alt_loop)