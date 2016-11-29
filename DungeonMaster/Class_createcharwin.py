from tkinter import *
from tkinter import messagebox,filedialog##specific imports testing
#import Class_mainwin, Class_dicerollerwin, Class_optwin #Class_createcharwin, 

#import standard libs 
import BeeLibv3 as Blib
import Common

class createcharwin:#(main_win):##better to create new window form,from scratch
    #vars
    char_BG_NAMES = []
    


    
    def __init__(self,masterwin,mega_main_datafile):
        self.This_win = masterwin
        self.datamain = mega_main_datafile

        #self.This_win = Toplevel()
        self.This_win.title('Character Creation Setup')
        self.This_win.geometry('640x720')
        ##preload
        self.internal_preload()

        ##tk vars
        ##setup
        self.charbase_name_IRL_BOX_VAR = StringVar()
        self.charbase_name_CHR_BOX_VAR = StringVar()
        #primaryattributes_setup_DRL_LBX = None

        #primary attribute allocation
        self.primaryattributes_STR_BTN_VAR = StringVar()
        self.primaryattributes_DEX_BTN_VAR = StringVar()
        self.primaryattributes_CON_BTN_VAR = StringVar()
        self.primaryattributes_INT_BTN_VAR = StringVar()
        self.primaryattributes_WIS_BTN_VAR = StringVar()
        self.primaryattributes_CHR_BTN_VAR = StringVar()

        self.primaryattributes_STR_LBL_VAR = StringVar()
        self.primaryattributes_DEX_LBL_VAR = StringVar()
        self.primaryattributes_CON_LBL_VAR = StringVar()
        self.primaryattributes_INT_LBL_VAR = StringVar()
        self.primaryattributes_WIS_LBL_VAR = StringVar()
        self.primaryattributes_CHR_LBL_VAR = StringVar()

        ##roll modifiers for race
        self.Backgrounds_rollmod_STR_LBL_VAR = StringVar()
        self.Backgrounds_rollmod_DEX_LBL_VAR = StringVar()
        self.Backgrounds_rollmod_CON_LBL_VAR = StringVar()
        self.Backgrounds_rollmod_INT_LBL_VAR = StringVar()
        self.Backgrounds_rollmod_WIS_LBL_VAR = StringVar()
        self.Backgrounds_rollmod_CHR_LBL_VAR = StringVar()

        self.Backgrounds_rollmod_STR_LBL_VAR.set('STR modifier|+-0')
        self.Backgrounds_rollmod_DEX_LBL_VAR.set('DEX modifier|+-0')
        self.Backgrounds_rollmod_CON_LBL_VAR.set('CON modifier|+-0')
        self.Backgrounds_rollmod_INT_LBL_VAR.set('INT modifier|+-0')
        self.Backgrounds_rollmod_WIS_LBL_VAR.set('WIS modifier|+-0')
        self.Backgrounds_rollmod_CHR_LBL_VAR.set('CHR modifier|+-0')

        ##inventory
        ##bg setup
        self.Backgrounds_setup_CBG_CURR_LBL_VAR = StringVar()
        self.Backgrounds_setup_CBS_CURR_LBL_VAR = StringVar()
        self.Backgrounds_setup_CBO_CURR_LBL_VAR = StringVar()
    
        self.Backgrounds_setup_CBG_CURR_LBL_VAR.set('None selected!')#.set('CBG')
        self.Backgrounds_setup_CBS_CURR_LBL_VAR.set('None selected!')#.set('CBS')
        self.Backgrounds_setup_CBO_CURR_LBL_VAR.set('None selected!')#.set('CBO')
        ##race variable
       #Backgrounds_setup_CBS_RACE_VAR = ''
       #Backgrounds_setup_CBG_RACE_VAR = 'None'
        ##hpmiscskills
        self.HPmiscskills_AMC_BOX_VAR = StringVar()
        self.HPmiscskills_INI_BOX_VAR = StringVar()
        self.HPmiscskills_SPD_BOX_VAR = StringVar()
        self.HPmiscskills_HMX_BOX_VAR = StringVar()
        self.HPmiscskills_HTP_BOX_VAR = StringVar()
        self.HPmiscskills_HCR_BOX_VAR = StringVar()

        ##saving throws
        self.savingthrows_STR_CHK_VAR = IntVar()##chkboxes
        self.savingthrows_DEX_CHK_VAR = IntVar()
        self.savingthrows_CON_CHK_VAR = IntVar()
        self.savingthrows_INT_CHK_VAR = IntVar()
        self.savingthrows_WIS_CHK_VAR = IntVar()
        self.savingthrows_CHR_CHK_VAR = IntVar()
    
        self.savingthrows_STR_BOX_VAR = StringVar()##entries
        self.savingthrows_DEX_BOX_VAR = StringVar()
        self.savingthrows_CON_BOX_VAR = StringVar()
        self.savingthrows_INT_BOX_VAR = StringVar()
        self.savingthrows_WIS_BOX_VAR = StringVar()
        self.savingthrows_CHR_BOX_VAR = StringVar()

    
        ##secondary skills
        self.secondaryskills_ACR_CHK_VAR = IntVar()
        self.secondaryskills_ACR_BOX_VAR = StringVar()
        self.secondaryskills_ANH_CHK_VAR = IntVar()
        self.secondaryskills_ANH_BOX_VAR = StringVar()
        self.secondaryskills_ARC_CHK_VAR = IntVar()
        self.secondaryskills_ARC_BOX_VAR = StringVar()
        self.secondaryskills_ATH_CHK_VAR = IntVar()
        self.secondaryskills_ATH_BOX_VAR = StringVar()
        self.secondaryskills_DEC_CHK_VAR = IntVar()
        self.secondaryskills_DEC_BOX_VAR = StringVar()
        self.secondaryskills_HIS_CHK_VAR = IntVar()
        self.secondaryskills_HIS_BOX_VAR = StringVar()
        self.secondaryskills_CHR_CHK_VAR = IntVar()
        self.secondaryskills_CHR_BOX_VAR = StringVar()
        self.secondaryskills_IDT_CHK_VAR = IntVar()
        self.secondaryskills_IDT_BOX_VAR = StringVar()
        self.secondaryskills_INV_CHK_VAR = IntVar()
        self.secondaryskills_INV_BOX_VAR = StringVar()
        self.secondaryskills_MED_CHK_VAR = IntVar()
        self.secondaryskills_MED_BOX_VAR = StringVar()
        self.secondaryskills_NAT_CHK_VAR = IntVar()
        self.secondaryskills_NAT_BOX_VAR = StringVar()
        self.secondaryskills_PER_CHK_VAR = IntVar()
        self.secondaryskills_PER_BOX_VAR = StringVar()
        self.secondaryskills_PRF_CHK_VAR = IntVar()
        self.secondaryskills_PRF_BOX_VAR = StringVar()
        self.secondaryskills_PRS_CHK_VAR = IntVar()
        self.secondaryskills_PRS_BOX_VAR = StringVar()
        self.secondaryskills_REL_CHK_VAR = IntVar()
        self.secondaryskills_REL_BOX_VAR = StringVar()
        self.secondaryskills_SOH_CHK_VAR = IntVar()
        self.secondaryskills_SOH_BOX_VAR = StringVar()
        self.secondaryskills_STE_CHK_VAR = IntVar()
        self.secondaryskills_STE_BOX_VAR = StringVar()
        self.secondaryskills_SRV_CHK_VAR = IntVar()
        self.secondaryskills_SRV_BOX_VAR = StringVar()
        ##hit dice
        self.Backgrounds_hitdie_HTD_BOX_VAR = StringVar()
        
        ##widgets

        ##personality traits
        #Backgrounds_misctraits_DPT_LBL_VAR = StringVar()
        #Backgrounds_misctraits_DPI_LBL_VAR = StringVar()
        #Backgrounds_misctraits_DPB_LBL_VAR = StringVar()
        #Backgrounds_misctraits_DPF_LBL_VAR = StringVar()
        ##widgets
        ##scharbase_name
        charbase_name_LF = LabelFrame(self.This_win,text = 'character\ninformation')
        charbase_name_IRL_LBL = Label(charbase_name_LF,text = 'player name').grid(row=0,column=0)
        charbase_name_IRL_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_IRL_BOX_VAR).grid(row=1,column=0)
        charbase_name_CHR_LBL = Label(charbase_name_LF,text = 'character name').grid(row=0,column=1)
        charbase_name_CHR_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_CHR_BOX_VAR).grid(row=1,column=1)
        charbase_name_LF.place(x=5,y=5)
        primaryattributes_setup_LF = LabelFrame(self.This_win,text= 'primary attributes dice roller')
        primaryattributes_setup_RTD_BTN = Button(primaryattributes_setup_LF,text = 'randomize values',command = self.sub_button_rollprimary).grid(row=0,column=0)
        primaryattributes_setup_RSV_BTN = Button(primaryattributes_setup_LF,text = 'Clear values',command = self.sub_button_resetvalues).grid(row=0,column=1)
        self.primaryattributes_setup_DRL_LBX = Listbox(primaryattributes_setup_LF,height = 6,width = 5)
        self.primaryattributes_setup_DRL_LBX.grid(row=1,column=0)
        primaryattributes_setup_LF.place(x=5,y=150)
        

        #primaryattributes_LF
        #buttons display 'SEt Value' then when clicked change to the selected diceroll on a listbox eg 'assigned:'+str(droll[x])
        #text = 'Set Value!'
        primaryattributes_LF = LabelFrame(self.This_win,text = 'primary\nattributes')
        primaryattributes_HAD_LBL = Label(primaryattributes_LF,text = 'attribute\nname').grid(row=0,column=0)
        primaryattributes_HAS_LBL = Label(primaryattributes_LF,text = 'attribute\nvalue').grid(row=0,column=1)
        primaryattributes_HRM_LBL = Label(primaryattributes_LF,text = 'roll modifier').grid(row=0,column=2)
        
        primaryattributes_STR_LBL = Label(primaryattributes_LF,text = 'Strength').grid(row=1,column=0)
        primaryattributes_STR_BTN = Button(primaryattributes_LF,width = 10,textvariable = self.primaryattributes_STR_BTN_VAR,command = self.sub_button_STR,).grid(row=1,column=1)#.pack()##was width = 3
        primaryattributes_STR_LBL = Label(primaryattributes_LF,width = 4,textvariable = self.primaryattributes_STR_LBL_VAR).grid(row=1,column=2)
        primaryattributes_DEX_LBL = Label(primaryattributes_LF,text = 'Dexterity').grid(row=2,column=0)
        primaryattributes_DEX_BTN = Button(primaryattributes_LF,width = 10,textvariable = self.primaryattributes_DEX_BTN_VAR,command = self.sub_button_DEX).grid(row=2,column=1)
        primaryattributes_DEX_LBL = Label(primaryattributes_LF,width = 4,textvariable = self.primaryattributes_DEX_LBL_VAR).grid(row=2,column=2)
        primaryattributes_CON_LBL = Label(primaryattributes_LF,text = 'Constitution').grid(row=3,column=0)      
        primaryattributes_CON_BTN = Button(primaryattributes_LF,width = 10,textvariable = self.primaryattributes_CON_BTN_VAR,command = self.sub_button_CON).grid(row=3,column=1)
        primaryattributes_CON_LBL = Label(primaryattributes_LF,width = 4,textvariable = self.primaryattributes_CON_LBL_VAR).grid(row=3,column=2)
        primaryattributes_INT_LBL = Label(primaryattributes_LF,text = 'Intelligence').grid(row=4,column=0)
        primaryattributes_INT_BTN = Button(primaryattributes_LF,width = 10,textvariable = self.primaryattributes_INT_BTN_VAR,command = self.sub_button_INT).grid(row=4,column=1)
        primaryattributes_INT_LBL = Label(primaryattributes_LF,width = 4,textvariable = self.primaryattributes_INT_LBL_VAR).grid(row=4,column=2)
        primaryattributes_WIS_LBL = Label(primaryattributes_LF,text = 'Wisdom').grid(row=5,column=0)
        primaryattributes_WIS_BTN = Button(primaryattributes_LF,width = 10,textvariable = self.primaryattributes_WIS_BTN_VAR,command = self.sub_button_WIS).grid(row=5,column=1)
        primaryattributes_WIS_LBL = Label(primaryattributes_LF,width = 4,textvariable = self.primaryattributes_WIS_LBL_VAR).grid(row=5,column=2)
        primaryattributes_CHR_LBL = Label(primaryattributes_LF,text = 'Charisma').grid(row=6,column=0)
        primaryattributes_CHR_BTN = Button(primaryattributes_LF,width = 10,textvariable = self.primaryattributes_CHR_BTN_VAR,command = self.sub_button_CHR).grid(row=6,column=1)
        primaryattributes_CHR_LBL = Label(primaryattributes_LF,width = 4,textvariable = self.primaryattributes_CHR_LBL_VAR).grid(row=6,column=2)
        primaryattributes_LF.place(x=5,y=300)##was w3
        self.internal_button_primary_Resetvalues()
        #primaryattributes_setup_LF.place(x=0,y=0)

        #character background
        Backgrounds_setup_LF = LabelFrame(self.This_win,text = 'BG\nbackground selection')
        Backgrounds_setup_CBG_LBL = Label(Backgrounds_setup_LF,text = 'Pick a race!').grid(row=0,column=0) 
        self.Backgrounds_setup_CBG_LBX = Listbox(Backgrounds_setup_LF,width=10,height = 5)
        self.Backgrounds_setup_CBG_LBX.grid(row=1,column=0)##choosebackground
        Backgrounds_setup_CBG_CURR_LBL = Label(Backgrounds_setup_LF,textvariable = self.Backgrounds_setup_CBG_CURR_LBL_VAR).grid(row=2,column=0)
        Backgrounds_setup_CBG_CNF_BTN = Button(Backgrounds_setup_LF,command = self.button_sub_confirmbackground,text = 'Pick!').grid(row=3,column=0)
        
        Backgrounds_setup_CBS_LBL = Label(Backgrounds_setup_LF,text = 'Pick a subrace!').grid(row=0,column=1)
        self.Backgrounds_setup_CBS_LBX = Listbox(Backgrounds_setup_LF,width=10,height = 5)
        self.Backgrounds_setup_CBS_LBX.grid(row=1,column=1)#choosebackgroundsub
        Backgrounds_setup_CBS_CURR_LBL = Label(Backgrounds_setup_LF,textvariable = self.Backgrounds_setup_CBS_CURR_LBL_VAR).grid(row=2,column=1)
        Backgrounds_setup_CBS_CNF_BTN = Button(Backgrounds_setup_LF,command = self.button_sub_confirmsubrace,text = 'Pick!').grid(row=3,column=1)
        
        Backgrounds_setup_CBO_LBL = Label(Backgrounds_setup_LF,text = 'Pick a Class!').grid(row=0,column=2)##was 'Pick a Background!'
        self.Backgrounds_setup_CBO_LBX = Listbox(Backgrounds_setup_LF,width=10,height = 5)
        self.Backgrounds_setup_CBO_LBX.grid(row=1,column=2)#choosebackgroundorigin  #Edit:now class
        Backgrounds_setup_CBO_CURR_LBL = Label(Backgrounds_setup_LF,textvariable = self.Backgrounds_setup_CBO_CURR_LBL_VAR).grid(row=2,column=2)
        Backgrounds_setup_CBO_CNF_BTN = Button(Backgrounds_setup_LF,command = self.sub_button_confirmclass,text = 'Pick!').grid(row=3,column=2)
        Backgrounds_setup_LF.place(x=500,y=0)


        Backgrounds_rollmod_LF = LabelFrame(self.This_win,text = 'BG\nprimary attribute modifiers')
        Backgrounds_rollmod_LBL = Label(Backgrounds_rollmod_LF,text = '==Roll Modifiers==').grid(row=0,column=0)
        Backgrounds_rollmod_STR_LBL = Label(Backgrounds_rollmod_LF,width = 16,textvariable = self.Backgrounds_rollmod_STR_LBL_VAR).grid(row=1,column=0)
        Backgrounds_rollmod_DEX_LBL = Label(Backgrounds_rollmod_LF,width = 16,textvariable = self.Backgrounds_rollmod_DEX_LBL_VAR).grid(row=2,column=0)
        Backgrounds_rollmod_CON_LBL = Label(Backgrounds_rollmod_LF,width = 16,textvariable = self.Backgrounds_rollmod_CON_LBL_VAR).grid(row=3,column=0)
        Backgrounds_rollmod_INT_LBL = Label(Backgrounds_rollmod_LF,width = 16,textvariable = self.Backgrounds_rollmod_INT_LBL_VAR).grid(row=4,column=0)
        Backgrounds_rollmod_WIS_LBL = Label(Backgrounds_rollmod_LF,width = 16,textvariable = self.Backgrounds_rollmod_WIS_LBL_VAR).grid(row=5,column=0)
        Backgrounds_rollmod_CHR_LBL = Label(Backgrounds_rollmod_LF,width = 16,textvariable = self.Backgrounds_rollmod_CHR_LBL_VAR).grid(row=6,column=0)
        Backgrounds_rollmod_LF.place(x=500,y=200)

        Backgrounds_traits_LF = LabelFrame(self.This_win,text = 'BG\ntrait modifiers')
        self.Backgrounds_traits_TRT_TXT = Text(Backgrounds_traits_LF,height = 15,width = 25)#add scrollbar to list##alt height = 10,width = 20
        self.Backgrounds_traits_TRT_TXT .grid(row=0,column=0)#.pack() ##was height 10
        Backgrounds_traits_LF.place(x=500,y=390)
        
        Backgrounds_LANG_LF = LabelFrame(self.This_win,text = 'BG\nLanguages')
        self.Backgrounds_LANG_TRT_TXT = Text(Backgrounds_LANG_LF,height = 6,width = 10)#add scrollbar to list
        self.Backgrounds_LANG_TRT_TXT .grid(row=0,column=0)#.pack() ##was height 10
        Backgrounds_LANG_LF.place(x=675,y=200)

        ##hp misc stuff
##        HPMISC_SETUP_LF = LabelFrame(self.This_win,text = 'armour class\nhealth stats selection')
##        HPMISC_SETUP_LF.place(x=0,y=0)
        HPmiscskills_LF = LabelFrame(self.This_win,text = 'BG\nHP/misc')
        HPmiscskills_AMC_BOX = Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_AMC_BOX_VAR,state = DISABLED)             .grid(row=1,column=0)#.pack()
        HPmiscskills_AMC_LBL = Label(HPmiscskills_LF,text = 'armour class') .grid(row=0,column=0)#.pack()
        HPmiscskills_INI_BOX = Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_INI_BOX_VAR,state = DISABLED)             .grid(row=1,column=1)#.pack()
        HPmiscskills_INI_LBL = Label(HPmiscskills_LF,text = 'initiative')   .grid(row=0,column=1)#.pack()
        HPmiscskills_SPD_BOX = Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_SPD_BOX_VAR,state = DISABLED)             .grid(row=1,column=2)#.pack()
        HPmiscskills_SPD_LBL = Label(HPmiscskills_LF,text = 'Speed')        .grid(row=0,column=2)#.pack()
        
        HPmiscskills_HMX_BOX = Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HMX_BOX_VAR,state = DISABLED)             .grid(row=4,column=1)#.pack()
        HPmiscskills_HMX_LBL = Label(HPmiscskills_LF,text = 'MAX HP')        .grid(row=4,column=0)#.pack()
        HPmiscskills_HTP_BOX = Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HTP_BOX_VAR,state = DISABLED)              .grid(row=5,column=1)#.pack()
        HPmiscskills_HTP_LBL = Label(HPmiscskills_LF,text = 'temp HP')        .grid(row=5,column=0)#.pack()
        HPmiscskills_HCR_BOX = Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HCR_BOX_VAR,state = DISABLED)              .grid(row=6,column=1)#.pack()
        HPmiscskills_HCR_LBL = Label(HPmiscskills_LF,text = 'current HP')        .grid(row=6,column=0)#.pack()
        HPmiscskills_LF.place(x=500,y=675)##was 375

        Backgrounds_setup_misctraits_LF = LabelFrame(self.This_win,text = 'MISC\nBackground traits setup')
        Backgrounds_setup_misctraits_DPT_LBL = Label(Backgrounds_setup_misctraits_LF,text = 'Pick a personailty trait!').grid(row=0,column=1)
        self.Backgrounds_setup_misctraits_DPT_LBX = Listbox(Backgrounds_setup_misctraits_LF,width=10,height = 5)
        self.Backgrounds_setup_misctraits_DPT_LBX.grid(row=1,column=1)
        Backrounds_setup_misctraits_DPT_BTN = Button(Backgrounds_setup_misctraits_LF,text = 'Pick!',command = self.sub_button_confirmtrait_PERS).grid(row=2,column=1)
        Backgrounds_setup_misctraits_DPI_LBL = Label(Backgrounds_setup_misctraits_LF,text = 'Pick a personality ideal!').grid(row=0,column=2)
        self.Backgrounds_setup_misctraits_DPI_LBX = Listbox(Backgrounds_setup_misctraits_LF,width=10,height = 5)
        self.Backgrounds_setup_misctraits_DPI_LBX.grid(row=1,column=2)
        Backrounds_setup_misctraits_DPI_BTN = Button(Backgrounds_setup_misctraits_LF,text = 'Pick!',command = self.sub_button_confirmtrait_IDEAL).grid(row=2,column=2)
        Backgrounds_setup_misctraits_DPF_LBL = Label(Backgrounds_setup_misctraits_LF,text = 'Pick a personality bond!').grid(row=0,column=3)
        self.Backgrounds_setup_misctraits_DPB_LBX = Listbox(Backgrounds_setup_misctraits_LF,width=10,height = 5)
        self.Backgrounds_setup_misctraits_DPB_LBX.grid(row=1,column=3)
        Backrounds_setup_misctraits_DPB_BTN = Button(Backgrounds_setup_misctraits_LF,text = 'Pick!',command = self.sub_button_confirmtrait_BOND).grid(row=2,column=3)
        Backgrounds_setup_misctraits_DPF_LBL = Label(Backgrounds_setup_misctraits_LF,text = 'Pick a personality flaw!').grid(row=0,column=4)
        self.Backgrounds_setup_misctraits_DPF_LBX = Listbox(Backgrounds_setup_misctraits_LF,width=10,height = 5)
        self.Backgrounds_setup_misctraits_DPF_LBX.grid(row=1,column=4)
        Backrounds_setup_misctraits_DPF_BTN = Button(Backgrounds_setup_misctraits_LF,text = 'Pick!',command = self.sub_button_confirmtrait_FLAW).grid(row=2,column=4)
        Backgrounds_setup_misctraits_RNG_BTN = Button(Backgrounds_setup_misctraits_LF,text = 'Randomize\nall selections!',command =self.sub_button_confirmtrait_RNG).grid(row=3,column=1)
        Backgrounds_setup_misctraits_LF.place(x=825,y=0)#.grid(row=0,column=0)

        #savingthrows_LF
        savingthrows_LF = LabelFrame(self.This_win,text = 'BG\nSaving Throws')
        savingthrows_STR_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_STR_CHK_VAR).grid(row = 0,column=0)#.pack()
        savingthrows_STR_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_STR_BOX_VAR,state = DISABLED).grid(row = 0,column=1)#.pack()
        savingthrows_STR_LBL = Label(savingthrows_LF,text = 'Strength')                                     .grid(row = 0,column=2)#.pack()
        savingthrows_DEX_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_DEX_CHK_VAR).grid(row = 1,column=0)#.pack()
        savingthrows_DEX_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_DEX_BOX_VAR,state = DISABLED).grid(row = 1,column=1)#.pack()
        savingthrows_DEX_LBL = Label(savingthrows_LF,text = 'Dexterity')                                    .grid(row = 1,column=2)#.pack()
        savingthrows_CON_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_CON_CHK_VAR).grid(row = 2,column=0)#.pack()
        savingthrows_CON_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CON_BOX_VAR,state = DISABLED).grid(row = 2,column=1)#.pack()
        savingthrows_CON_LBL = Label(savingthrows_LF,text = 'Constitution')                                 .grid(row = 2,column=2)#.pack()
        savingthrows_INT_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_INT_CHK_VAR).grid(row = 3,column=0)#.pack()
        savingthrows_INT_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_INT_BOX_VAR,state = DISABLED).grid(row = 3,column=1)#.pack()
        savingthrows_INT_LBL = Label(savingthrows_LF,text = 'Intelligence')                                 .grid(row = 3,column=2)#.pack()
        savingthrows_WIS_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_WIS_CHK_VAR).grid(row = 4,column=0)#.pack()
        savingthrows_WIS_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_WIS_BOX_VAR,state = DISABLED).grid(row = 4,column=1)#.pack()
        savingthrows_WIS_LBL = Label(savingthrows_LF,text = 'Wisdom')                                       .grid(row = 4,column=2)#.pack()
        savingthrows_CHR_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_CHR_CHK_VAR).grid(row = 5,column=0)#.pack()
        savingthrows_CHR_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CHR_BOX_VAR,state = DISABLED).grid(row = 5,column=1)#.pack()
        savingthrows_CHR_LBL = Label(savingthrows_LF,text = 'Charisma')                                     .grid(row = 5,column=2)#.pack()
        savingthrows_LF.place(x=325,y=130)

        #secondaryskills_LF
        secondaryskills_LF = LabelFrame(self.This_win,text = 'BG\nskills')
        secondaryskills_ACR_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ACR_CHK_VAR).grid(row=0,column=0)#).pack(side=LEFT)
        secondaryskills_ACR_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ACR_BOX_VAR,state = DISABLED).grid(row=0,column=1)#.pack()
        secondaryskills_ACR_LBL = Label(secondaryskills_LF,text = 'acrobatics').grid(row=0,column=2)#.pack()
        secondaryskills_ANH_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ANH_CHK_VAR).grid(row=1,column=0)#.pack()
        secondaryskills_ANH_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ANH_BOX_VAR,state = DISABLED).grid(row=1,column=1)#.pack()
        secondaryskills_ANH_LBL = Label(secondaryskills_LF,text = 'animal handling').grid(row=1,column=2)#.pack()
        secondaryskills_ARC_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ARC_CHK_VAR).grid(row=2,column=0)#.pack()
        secondaryskills_ARC_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ARC_BOX_VAR,state = DISABLED).grid(row=2,column=1)#.pack()
        secondaryskills_ARC_LBL = Label(secondaryskills_LF,text = 'arcana').grid(row=2,column=2)#.pack()
        secondaryskills_ATH_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ATH_CHK_VAR).grid(row=3,column=0)#.pack()
        secondaryskills_ATH_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ATH_BOX_VAR,state = DISABLED).grid(row=3,column=1)#.pack()
        secondaryskills_ATH_LBL = Label(secondaryskills_LF,text = 'athletics').grid(row=3,column=2)#.pack()
        secondaryskills_DEC_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_DEC_CHK_VAR).grid(row=4,column=0)#.pack()
        secondaryskills_DEC_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_DEC_BOX_VAR,state = DISABLED).grid(row=4,column=1)#.pack()
        secondaryskills_DEC_LBL = Label(secondaryskills_LF,text = 'deception').grid(row=4,column=2)#.pack()
        secondaryskills_HIS_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_HIS_CHK_VAR).grid(row=5,column=0)#.pack()
        secondaryskills_HIS_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_HIS_BOX_VAR,state = DISABLED).grid(row=5,column=1)#.pack()
        secondaryskills_HIS_LBL = Label(secondaryskills_LF,text = 'history').grid(row=5,column=2)#.pack()
        secondaryskills_CHR_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_CHR_CHK_VAR).grid(row=6,column=0)#.pack()
        secondaryskills_CHR_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_CHR_BOX_VAR,state = DISABLED).grid(row=6,column=1)#.pack()
        secondaryskills_CHR_LBL = Label(secondaryskills_LF,text = 'insight').grid(row=6,column=2)#.pack()
        secondaryskills_IDT_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_IDT_CHK_VAR).grid(row=7,column=0)#.pack()
        secondaryskills_IDT_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_IDT_BOX_VAR,state = DISABLED).grid(row=7,column=1)#.pack()
        secondaryskills_IDT_LBL = Label(secondaryskills_LF,text = 'intimidation').grid(row=7,column=2)#.pack()
        secondaryskills_INV_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_INV_CHK_VAR).grid(row=8,column=0)#.pack()
        secondaryskills_INV_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_INV_BOX_VAR,state = DISABLED).grid(row=8,column=1)#.pack()
        secondaryskills_INV_LBL = Label(secondaryskills_LF,text = 'investigation').grid(row=8,column=2)#.pack()
        secondaryskills_MED_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_MED_CHK_VAR).grid(row=9,column=0)#.pack()
        secondaryskills_MED_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_MED_BOX_VAR,state = DISABLED).grid(row=9,column=1)#.pack()
        secondaryskills_MED_LBL = Label(secondaryskills_LF,text = 'medicine').grid(row=9,column=2)#.pack()
        secondaryskills_NAT_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_NAT_CHK_VAR).grid(row=10,column=0)#.pack()
        secondaryskills_NAT_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_NAT_BOX_VAR,state = DISABLED).grid(row=10,column=1)#.pack()
        secondaryskills_NAT_LBL = Label(secondaryskills_LF,text = 'nature').grid(row=10,column=2)#.pack()
        secondaryskills_PER_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PER_CHK_VAR).grid(row=11,column=0)#.pack()
        secondaryskills_PER_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PER_BOX_VAR,state = DISABLED).grid(row=11,column=1)#.pack()
        secondaryskills_PER_LBL = Label(secondaryskills_LF,text = 'perception').grid(row=11,column=2)#.pack()
        secondaryskills_PRF_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PRF_CHK_VAR).grid(row=12,column=0)#.pack()
        secondaryskills_PRF_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PRF_BOX_VAR,state = DISABLED).grid(row=12,column=1)#.pack()
        secondaryskills_PRF_LBL = Label(secondaryskills_LF,text = 'performance').grid(row=12,column=2)#.pack()
        secondaryskills_PRS_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PRS_CHK_VAR).grid(row=13,column=0)#.pack()
        secondaryskills_PRS_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PRS_BOX_VAR,state = DISABLED).grid(row=13,column=1)#.pack()
        secondaryskills_PRS_LBL = Label(secondaryskills_LF,text = 'persuasion').grid(row=13,column=2)#.pack()
        secondaryskills_REL_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_REL_CHK_VAR).grid(row=14,column=0)#.pack()
        secondaryskills_REL_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_REL_BOX_VAR,state = DISABLED).grid(row=14,column=1)#.pack()
        secondaryskills_REL_LBL = Label(secondaryskills_LF,text = 'religion').grid(row=14,column=2)#.pack()
        secondaryskills_SOH_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_SOH_CHK_VAR).grid(row=15,column=0)#.pack()
        secondaryskills_SOH_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_SOH_BOX_VAR,state = DISABLED).grid(row=15,column=1)#.pack()
        secondaryskills_SOH_LBL = Label(secondaryskills_LF,text = 'sleight of hand').grid(row=15,column=2)#.pack()
        secondaryskills_STE_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_STE_CHK_VAR).grid(row=16,column=0)#.pack()
        secondaryskills_STE_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_STE_BOX_VAR,state = DISABLED).grid(row=16,column=1)#.pack()
        secondaryskills_STE_LBL = Label(secondaryskills_LF,text = 'stealth').grid(row=16,column=2)#.pack()
        secondaryskills_SRV_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_SRV_CHK_VAR).grid(row=17,column=0)#.pack()
        secondaryskills_SRV_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_SRV_BOX_VAR,state = DISABLED).grid(row=17,column=1)#.pack()
        secondaryskills_SRV_LBL = Label(secondaryskills_LF,text = 'survival').grid(row=17,column=2)#.pack()
        secondaryskills_LF.place(x=325,y=315)

        Backgrounds_hitdie_LF = LabelFrame(self.This_win,text = 'BG\nHit Dice')
        Backgrounds_hitdie_HTD_BOX = Entry(Backgrounds_hitdie_LF,width = 5,textvariable = self.Backgrounds_hitdie_HTD_BOX_VAR,state = DISABLED).grid(row=0,column=1)
        Backgrounds_hitdie_HTD_LBL = Label(Backgrounds_hitdie_LF,text = 'hit die = ').grid(row=0,column=0)
        Backgrounds_hitdie_LF.place(x=675,y=340)
        
        Backgrounds_misctraits_LF = LabelFrame(self.This_win,text = 'MISC\nBackground traits setup')
        Backgrounds_misctraits_DPT_LBL_LBL = Label(Backgrounds_misctraits_LF,text = '==personailty trait==').grid(row=0,column=0)##displaypersonalitytrait
        Backgrounds_misctraits_DPI_LBL_LBL = Label(Backgrounds_misctraits_LF,text = '==personailty ideal==').grid(row=0,column=1)##displaypersonalityideal
        Backgrounds_misctraits_DPB_LBL_LBL = Label(Backgrounds_misctraits_LF,text = '==personailty bond ==').grid(row=2,column=0)##displaypersonalitybond
        Backgrounds_misctraits_DPF_LBL_LBL = Label(Backgrounds_misctraits_LF,text = '==personailty flaw ==').grid(row=2,column=1)##displaypersonalityflaw
        
        #Backgrounds_misctraits_DPT_LBL = Label(Backgrounds_misctraits_LF,textvariable = self.Backgrounds_misctraits_DPT_LBL_VAR).grid(row=1,column=0)##displaypersonalitytrait
        #Backgrounds_misctraits_DPI_LBL = Label(Backgrounds_misctraits_LF,textvariable = self.Backgrounds_misctraits_DPI_LBL_VAR).grid(row=1,column=1)##displaypersonalityideal
        #Backgrounds_misctraits_DPB_LBL = Label(Backgrounds_misctraits_LF,textvariable = self.Backgrounds_misctraits_DPB_LBL_VAR).grid(row=3,column=0)##displaypersonalitybond
        #Backgrounds_misctraits_DPF_LBL = Label(Backgrounds_misctraits_LF,textvariable = self.Backgrounds_misctraits_DPF_LBL_VAR).grid(row=3,column=1)##displaypersonalityflaw

        self.Backgrounds_misctraits_DPT_TXT = Text(Backgrounds_misctraits_LF,height = 5,width = 25)##width was 15
        self.Backgrounds_misctraits_DPT_TXT.grid(row=1,column=0)
        self.Backgrounds_misctraits_DPI_TXT = Text(Backgrounds_misctraits_LF,height = 5,width = 25)
        self.Backgrounds_misctraits_DPI_TXT.grid(row=1,column=1)
        self.Backgrounds_misctraits_DPB_TXT = Text(Backgrounds_misctraits_LF,height = 5,width = 25)
        self.Backgrounds_misctraits_DPB_TXT.grid(row=3,column=0)
        self.Backgrounds_misctraits_DPF_TXT = Text(Backgrounds_misctraits_LF,height = 5,width = 25)
        self.Backgrounds_misctraits_DPF_TXT.grid(row=3,column=1)
        Backgrounds_misctraits_LF.place(x=825,y=225)#.grid(row=0,column=0)


        Backgrounds_misctraits_inventory_LF = LabelFrame(self.This_win,text = 'INV\nbasic inventory')
        self.Backgrounds_misctraits_inventory_INV_TXT = Text(Backgrounds_misctraits_inventory_LF,width = 50,height = 10)
        self.Backgrounds_misctraits_inventory_INV_TXT.grid(row=0,column=0)
        Backgrounds_misctraits_inventory_LF.place(x=825,y=475)#(x=900,y=600)



        finalizechar_setup_LF = LabelFrame(self.This_win,text = 'options')
        finalizechar_setup_FIN_BTN = Button(finalizechar_setup_LF,text = 'create character',command = self.sub_button_FIN).grid(row=0,column=0)
        finalizechar_setup_FIN_BTN = Button(finalizechar_setup_LF,text = 'reset character',command = self.sub_button_CLR).grid(row=1,column=0)
        finalizechar_setup_LF.place(x=825,y=700)
        #print('x',self.primaryattributes_setup_DRL_LBX)

        
        ## post widget code
        self.internal_preload_data()#loads listboxes
        self.intenal_preload_traitselectiondata()##loads personality trait listboxes

        #tkloop
        
        self.This_win.after(1500,self.Alt_loop)
        self.This_win.mainloop() 
        
        
    def Alt_loop(self):##runs every 1.5 seconds
        ##additional event loop code here
        self.internal_calcrollmod_primary_LBL()
        self.internal_calcprofbonusplushpmisc()
        #self.internal_process_backgrounddata()
        print(self.internal_validaterolls())
        ##end
        self.This_win.after(1500,self.Alt_loop)
    def internal_preload(self):##for loading background info
        pass
    ##temp
    def array2csv(self,array):##from beelib
        temp = ''
        for fl in array:
            #print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
    def csv2array(self,csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
        arrayreturn = []
        temp = ''
        flag = False
        for x in csvstr:#range(len(csvnames)):
            if flag and (x==','):## ,, delimiter
                break
            if x ==',':
                arrayreturn.append(temp)
                temp = ''
                flag = True
            else:
                temp+=x
                flag = False
        return arrayreturn
    
    ###############
    ##button subs
    def sub_button_rollprimary(self):
        self.internal_button_primary_Resetvalues()
        x = self.internal_rollprimary()
        print(x)
        self.internal_refresh_DRL_listbox(x)
    def sub_button_resetvalues(self):
        self.internal_clear_DRL_listbox()
        self.internal_button_primary_Resetvalues()
    #primary attributes
    def sub_button_STR(self):
        x = self.internal_get_DRL_currselection_listbox()
        if x != False:
            self.primaryattributes_STR_BTN_VAR.set('set as| '+str(x))
        else:
            messagebox.showwarning('ERROR!','please select a value!')
    def sub_button_DEX(self):
        x = self.internal_get_DRL_currselection_listbox()
        if x != False:
            self.primaryattributes_DEX_BTN_VAR.set('set as| '+str(x))
        else:
            messagebox.showwarning('ERROR!','please select a value!')
    def sub_button_CON(self):
        x = self.internal_get_DRL_currselection_listbox()
        if x != False:
            self.primaryattributes_CON_BTN_VAR.set('set as| '+str(x))
        else:
            messagebox.showwarning('ERROR!','please select a value!')
    def sub_button_INT(self):
        x = self.internal_get_DRL_currselection_listbox()
        if x != False:
            self.primaryattributes_INT_BTN_VAR.set('set as| '+str(x))
        else:
            messagebox.showwarning('ERROR!','please select a value!')
    def sub_button_WIS(self):
        x = self.internal_get_DRL_currselection_listbox()
        if x != False:
            self.primaryattributes_WIS_BTN_VAR.set('set as| '+str(x))
        else:
            messagebox.showwarning('ERROR!','please select a value!')
    def sub_button_CHR(self):
        x = self.internal_get_DRL_currselection_listbox()
        if x != False:
            self.primaryattributes_CHR_BTN_VAR.set('set as| '+str(x))
        else:
            messagebox.showwarning('ERROR!','please select a value!')

    def sub_button_FIN(self):##finalize and export character creation to existing character sheet and save
        FLAG_OK = False
        FLAG_WRITE = False
        ##checking routine
        if self.internal_validaterolls() == False:## check dice attributes have not been assigned
            messagebox.showwarning('rolls','please check primary attributes')
            #charclass == 'None selected!'
        elif self.Backgrounds_setup_CBG_CURR_LBL_VAR.get() == 'None selected!':#check race has not been selected
            messagebox.showwarning('race','Please select a race!')
        elif self.Backgrounds_setup_CBS_CURR_LBL_VAR.get() == 'None selected!':#check subrace has not been selected
            messagebox.showwarning('subrace','Please select a subrace!')
        elif self.Backgrounds_setup_CBO_CURR_LBL_VAR.get()  == 'None selected!':#check background has not been selected
            messagebox.showwarning('background','Please select a character background')
        elif len(self.get_Backgrounds_misctraits_DPT_TXT()) == 0:#len(self.Backgrounds_misctraits_DPT_LBL_VAR.get()) == 0:
            messagebox.showwarning('background trait','Please select a character Trait!')#check background Trait has not been selected
        elif len(self.get_Backgrounds_misctraits_DPI_TXT()) == 0:#len(self.Backgrounds_misctraits_DPI_LBL_VAR.get()) == 0:
            messagebox.showwarning('background trait','Please select a character Ideal!')#check background Ideal has not been selected
        elif len(self.get_Backgrounds_misctraits_DPB_TXT()) == 0:#len(self.Backgrounds_misctraits_DPB_LBL_VAR.get()) == 0:
            messagebox.showwarning('background trait','Please select a character Bond!')#check background Bond has not been selected
        elif len(self.get_Backgrounds_misctraits_DPF_TXT()) == 0:#len(self.Backgrounds_misctraits_DPF_LBL_VAR.get()) == 0:
            messagebox.showwarning('background trait','Please select a character Flaw!')#check background Flaw has not been selected

        
        
        else:##if no issues raised then ok to continue
            FLAG_OK = True

        #print(len(self.get_Backgrounds_misctraits_DPT_TXT()))
        #print(len(self.get_Backgrounds_misctraits_DPI_TXT()))
        #print(len(self.get_Backgrounds_misctraits_DPB_TXT()))
        #print(len(self.get_Backgrounds_misctraits_DPF_TXT()))
        
        #FLAG_OK = True
        if FLAG_OK:
            if messagebox.askokcancel('Are You Sure?','finalize your character\nAre you sure'):   
                #choosing save location
                saveloc  = self.internal_savefileaskchecker()
                if saveloc[1]:##if file already exists
                    if messagebox.askokcancel('save file','Overwrite existing file\nare you sure?'):
                        FLAG_WRITE = True
                else:#else file does not exist
                    if messagebox.askokcancel('save file','are you sure?'):
                        FLAG_WRITE = True

                if FLAG_WRITE == True:#if user decides to save
                    ##preparing data
                    #print(self.get_Backgrounds_rollmod_LBL(),'\n',self.get_primaryattributes_LBL())#get rollmod primary
                    #input()
                    TOSAVE = []
                    B_RM = self.get_Backgrounds_rollmod_LBL()##background rollmod
                    P_RM = self.get_primaryattributes_LBL()##primary rollmod

                    for x in range(len(B_RM)):
                        B_RM[x] = B_RM[x].split('|')[1]##splits then discards the first entry
                        if B_RM[x] == '+-0':
                            B_RM[x] = '0'
                    print('========\n',B_RM,'\n',P_RM,'\n========')
                    temp = []
                    for x in range(len(B_RM)):#B_RM and P_RM are both same length
                        temp.append(int(B_RM[x])+int(P_RM[x]))#add them together
                    print(temp)
                    ARRAY_PATTR_RMOD=[]
                    ARRAY_PATTR_RMOD=temp
                    temp = []

                    P_ST = self.get_primaryattributes_BTN()
                    for x in range(len(P_ST)):#split and replace with just number part
                        P_ST[x] = P_ST[x].split('|')[1]
                    ARRAY_PATTR=[]
                    ARRAY_PATTR = P_ST

##                    S_ST = self.get_secondaryskills()
##                    temp = []
##                    for x in range(len(S_ST[0])):##both should be same length
##                        temp.append((S_ST[0][x],S_ST[1][x]))
##                    ARRAY_SATTR=[]
##                    ARRAY_SATTR = temp
##                    temp = []
                    ARRAY_SKILLS = self.get_secondaryskills()

                    ARRAY_SAVES = self.get_savingthrows()

                    ARRAY_HPMISC = self.get_hpmiscskills()

                    print(ARRAY_PATTR_RMOD,';',ARRAY_SKILLS)
                    STRING_PERCEPTION = str(10+int(ARRAY_PATTR_RMOD[4])+int(ARRAY_SKILLS[0][11]))##perception=10+wisdom rollmod+proficiency in perception
                    #input()
                    #rolling other dice for misc
                        #initiative
                        #hp
                    ##setting data into format
                    
                    
                    #primary info box
                    ARRAY_NAMESTAT=[self.charbase_name_CHR_BOX_VAR.get(),#char name
                     self.charbase_name_IRL_BOX_VAR.get(),#irl name
                     self.Backgrounds_setup_CBO_CURR_LBL_VAR.get(),#background
                     'level',#lvl
                     'faction',#faction
                     str(self.Backgrounds_setup_CBS_CURR_LBL_VAR.get())+' '+str(self.Backgrounds_setup_CBG_CURR_LBL_VAR.get()),#race [subrace race]
                     '0XP']#xp
                    #print('NAMeSTAT\n',yu)
                    #input()

                    TOSAVE = [ARRAY_NAMESTAT,ARRAY_PATTR,ARRAY_PATTR_RMOD,STRING_PERCEPTION,'0','0',ARRAY_SAVES,ARRAY_SKILLS,ARRAY_HPMISC,##profbonus =0 at lvl:0 inspiration is 0 at start normally
                              [self.Backgrounds_hitdie_HTD_BOX_VAR.get(), '1x', 0, 0, 0, 0, 0, 0],[[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],' '],#1x is hit dice
                              self.get_Backgrounds_LANG_TRT_TXT(),self.get_Backgrounds_misctraits_inventory_INV_TXT(),
                              [self.get_Backgrounds_misctraits_DPT_TXT(),self.get_Backgrounds_misctraits_DPI_TXT(),self.get_Backgrounds_Common.internal_prepsavemisctraits_DPB_TXT(),self.get_Backgrounds_misctraits_DPF_TXT(),
                               self.get_Backgrounds_traits_TRT_TXT()]]
                    print('\n\nsave{}>')
                    #for x in TOSAVE:
                        #print(x)
                    print(TOSAVE)
                    print('ss')
                    ##saving data

                    Fs = MEGA.mega2(saveloc[0])
                    if saveloc[1]:##if file exists already
                        Fs.clear()##clears data
                        #Fs.close()
                        #Fs.LOADED = True## hack to overwrite the file

                    TOSAVE = Common.internal_prepsave(TOSAVE)
                    for x in range(len(TOSAVE)-1):
                        print(TOSAVE[x],end='')
                        Fs.adddata(TOSAVE[x])
                        print('Done')
                    Fs.save()
                    
                    #finally close window
                    messagebox.showinfo('test','save complete')
                    
                    self.This_win.destroy()
                    
                else:#print to console dbg
                    print('save cancelled')
                    
                
    def sub_button_CLR(self):##reset all values
        if messagebox.askokcancel('Are You Sure?','reset all values to default\nAre you sure'):
            self.This_win.destroy()##destroys current window instance then creates a new instance of the window
            createcharwin()
    ##get
    def get_primaryattributes_BTN(self):##get button content:primary stats
        return[
            self.primaryattributes_STR_BTN_VAR.get(),
            self.primaryattributes_DEX_BTN_VAR.get(),
            self.primaryattributes_CON_BTN_VAR.get(),
            self.primaryattributes_INT_BTN_VAR.get(),
            self.primaryattributes_WIS_BTN_VAR.get(),
            self.primaryattributes_CHR_BTN_VAR.get()
            ]
    
    def get_primaryattributes_LBL(self):##get label content: roll modifier for primary stats
        return[
            self.primaryattributes_STR_LBL_VAR.get(),
            self.primaryattributes_DEX_LBL_VAR.get(),
            self.primaryattributes_CON_LBL_VAR.get(),
            self.primaryattributes_INT_LBL_VAR.get(),
            self.primaryattributes_WIS_LBL_VAR.get(),
            self.primaryattributes_CHR_LBL_VAR.get()
            ]
    def get_Backgrounds_rollmod_LBL(self):##get button content
        return[
            self.Backgrounds_rollmod_STR_LBL_VAR.get(),
            self.Backgrounds_rollmod_DEX_LBL_VAR.get(),
            self.Backgrounds_rollmod_CON_LBL_VAR.get(),
            self.Backgrounds_rollmod_INT_LBL_VAR.get(),
            self.Backgrounds_rollmod_WIS_LBL_VAR.get(),
            self.Backgrounds_rollmod_CHR_LBL_VAR.get()
            ]
    def get_Backgrounds_traits_TRT_TXT(self):
        return self.Backgrounds_traits_TRT_TXT.get(1.0, 'end-1c')
    
    def get_Backgrounds_LANG_TRT_TXT(self):
        return self.Backgrounds_LANG_TRT_TXT.get(1.0, 'end-1c')
    
    def get_savingthrows(self):
        return[
            (self.savingthrows_STR_CHK_VAR.get(),self.savingthrows_STR_BOX_VAR.get()),
            (self.savingthrows_DEX_CHK_VAR.get(),self.savingthrows_DEX_BOX_VAR.get()),
            (self.savingthrows_CON_CHK_VAR.get(),self.savingthrows_CON_BOX_VAR.get()),
            (self.savingthrows_INT_CHK_VAR.get(),self.savingthrows_INT_BOX_VAR.get()),
            (self.savingthrows_WIS_CHK_VAR.get(),self.savingthrows_WIS_BOX_VAR.get()),
            (self.savingthrows_CHR_CHK_VAR.get(),self.savingthrows_CHR_BOX_VAR.get())]##return tuples of each attribute(proficient,throw)

    def get_secondaryskills(self):
        return[[
            self.secondaryskills_ACR_BOX_VAR.get(),
            self.secondaryskills_ANH_BOX_VAR.get(),
            self.secondaryskills_ARC_BOX_VAR.get(),
            self.secondaryskills_ATH_BOX_VAR.get(),
            self.secondaryskills_DEC_BOX_VAR.get(),
            self.secondaryskills_HIS_BOX_VAR.get(),
            self.secondaryskills_CHR_BOX_VAR.get(),
            self.secondaryskills_IDT_BOX_VAR.get(),
            self.secondaryskills_INV_BOX_VAR.get(),
            self.secondaryskills_MED_BOX_VAR.get(),
            self.secondaryskills_NAT_BOX_VAR.get(),
            self.secondaryskills_PER_BOX_VAR.get(),
            self.secondaryskills_PRF_BOX_VAR.get(),
            self.secondaryskills_PRS_BOX_VAR.get(),
            self.secondaryskills_REL_BOX_VAR.get(),
            self.secondaryskills_SOH_BOX_VAR.get(),
            self.secondaryskills_STE_BOX_VAR.get(),
            self.secondaryskills_SRV_BOX_VAR.get(),
            ],[
            self.secondaryskills_ACR_CHK_VAR.get(),
            self.secondaryskills_ANH_CHK_VAR.get(),
            self.secondaryskills_ARC_CHK_VAR.get(),
            self.secondaryskills_ATH_CHK_VAR.get(),
            self.secondaryskills_DEC_CHK_VAR.get(),
            self.secondaryskills_HIS_CHK_VAR.get(),
            self.secondaryskills_CHR_CHK_VAR.get(),
            self.secondaryskills_IDT_CHK_VAR.get(),
            self.secondaryskills_INV_CHK_VAR.get(),
            self.secondaryskills_MED_CHK_VAR.get(),
            self.secondaryskills_NAT_CHK_VAR.get(),
            self.secondaryskills_PER_CHK_VAR.get(),
            self.secondaryskills_PRF_CHK_VAR.get(),
            self.secondaryskills_PRS_CHK_VAR.get(),
            self.secondaryskills_REL_CHK_VAR.get(),
            self.secondaryskills_SOH_CHK_VAR.get(),
            self.secondaryskills_STE_CHK_VAR.get(),
            self.secondaryskills_SRV_CHK_VAR.get()]]
    
    def get_hpmiscskills(self):
        ##hpmiscskills
        return[self.HPmiscskills_AMC_BOX_VAR.get(),
               self.HPmiscskills_INI_BOX_VAR.get(),
               self.HPmiscskills_SPD_BOX_VAR.get(),
               self.HPmiscskills_HMX_BOX_VAR.get(),
               self.HPmiscskills_HTP_BOX_VAR.get(),
               self.HPmiscskills_HCR_BOX_VAR.get()]
    
    def get_Backgrounds_misctraits_DPT_TXT(self):
        return self.Backgrounds_misctraits_DPT_TXT.get(1.0,'end-1c')
    def get_Backgrounds_misctraits_DPI_TXT(self):
        return self.Backgrounds_misctraits_DPI_TXT.get(1.0,'end-1c')
    def get_Backgrounds_misctraits_DPB_TXT(self):
        return self.Backgrounds_misctraits_DPB_TXT.get(1.0,'end-1c')
    def get_Backgrounds_misctraits_DPF_TXT(self):
        return self.Backgrounds_misctraits_DPF_TXT.get(1.0,'end-1c')
    def get_Backgrounds_misctraits_inventory_INV_TXT(self):
        return self.Backgrounds_misctraits_inventory_INV_TXT.get(1.0,'end-1c')
    ##set
    def set_primaryattributes_LBL(self,data):##set rollmod label
        self.primaryattributes_STR_LBL_VAR.set(data[0])
        self.primaryattributes_DEX_LBL_VAR.set(data[1])
        self.primaryattributes_CON_LBL_VAR.set(data[2])
        self.primaryattributes_INT_LBL_VAR.set(data[3])
        self.primaryattributes_WIS_LBL_VAR.set(data[4])
        self.primaryattributes_CHR_LBL_VAR.set(data[5])
        
    def set_Backgrounds_rollmod_LBL(self,data):##set rollmod label
        self.Backgrounds_rollmod_STR_LBL_VAR.set(data[0])
        self.Backgrounds_rollmod_DEX_LBL_VAR.set(data[1])
        self.Backgrounds_rollmod_CON_LBL_VAR.set(data[2])
        self.Backgrounds_rollmod_INT_LBL_VAR.set(data[3])
        self.Backgrounds_rollmod_WIS_LBL_VAR.set(data[4])
        self.Backgrounds_rollmod_CHR_LBL_VAR.set(data[5])

    def set_hpmiscskills(self,data):
        ##hpmiscskills
        self.HPmiscskills_AMC_BOX_VAR.set(data[0])
        self.HPmiscskills_INI_BOX_VAR.set(data[1])
        self.HPmiscskills_SPD_BOX_VAR.set(data[2])
        self.HPmiscskills_HMX_BOX_VAR.set(data[3])
        self.HPmiscskills_HTP_BOX_VAR.set(data[4])
        self.HPmiscskills_HCR_BOX_VAR.set(data[5])
        
    def set_Backgrounds_traits_TRT_TXT(self,Larray):
        self.Backgrounds_traits_TRT_TXT.delete(1.0, 'end-1c')
        for x in Larray:
            self.Backgrounds_traits_TRT_TXT.insert(INSERT,x)
    def set_Backgrounds_traits_TRT_TXT_CLR(self):
        self.Backgrounds_traits_TRT_TXT.delete(1.0, 'end-1c')
        
    def set_Backgrounds_LANG_TRT_TXT(self,Larray):
        self.Backgrounds_LANG_TRT_TXT.delete(1.0, 'end-1c')
        for x in Larray:
            self.Backgrounds_LANG_TRT_TXT.insert(INSERT,x)
    def set_Backgrounds_LANG_TRT_TXT_CLR(self):
        self.Backgrounds_LANG_TRT_TXT.delete(1.0, 'end-1c')

    def set_savingthrows(self,data):
        self.savingthrows_STR_BOX_VAR.set(data[0][1])
        self.savingthrows_DEX_BOX_VAR.set(data[1][1])
        self.savingthrows_CON_BOX_VAR.set(data[2][1])
        self.savingthrows_INT_BOX_VAR.set(data[3][1])
        self.savingthrows_WIS_BOX_VAR.set(data[4][1])
        self.savingthrows_CHR_BOX_VAR.set(data[5][1])
        
        self.savingthrows_STR_CHK_VAR.set(data[0][0])
        self.savingthrows_DEX_CHK_VAR.set(data[1][0])
        self.savingthrows_CON_CHK_VAR.set(data[2][0])
        self.savingthrows_INT_CHK_VAR.set(data[3][0])
        self.savingthrows_WIS_CHK_VAR.set(data[4][0])
        self.savingthrows_CHR_CHK_VAR.set(data[5][0])
    #secondary stats
    def set_secondaryskills(self,data):#[boxdata/checkboxdata][data]
        self.secondaryskills_ACR_BOX_VAR.set(data[0][0])
        self.secondaryskills_ANH_BOX_VAR.set(data[0][1])
        self.secondaryskills_ARC_BOX_VAR.set(data[0][2])
        self.secondaryskills_ATH_BOX_VAR.set(data[0][3])
        self.secondaryskills_DEC_BOX_VAR.set(data[0][4])
        self.secondaryskills_HIS_BOX_VAR.set(data[0][5])
        self.secondaryskills_CHR_BOX_VAR.set(data[0][6])
        self.secondaryskills_IDT_BOX_VAR.set(data[0][7])
        self.secondaryskills_INV_BOX_VAR.set(data[0][8])
        self.secondaryskills_MED_BOX_VAR.set(data[0][9])
        self.secondaryskills_NAT_BOX_VAR.set(data[0][10])
        self.secondaryskills_PER_BOX_VAR.set(data[0][11])
        self.secondaryskills_PRF_BOX_VAR.set(data[0][12])
        self.secondaryskills_PRS_BOX_VAR.set(data[0][13])
        self.secondaryskills_REL_BOX_VAR.set(data[0][14])
        self.secondaryskills_SOH_BOX_VAR.set(data[0][15])
        self.secondaryskills_STE_BOX_VAR.set(data[0][16])
        self.secondaryskills_SRV_BOX_VAR.set(data[0][17])
        
        self.secondaryskills_ACR_CHK_VAR.set(data[1][0])
        self.secondaryskills_ANH_CHK_VAR.set(data[1][1])
        self.secondaryskills_ARC_CHK_VAR.set(data[1][2])
        self.secondaryskills_ATH_CHK_VAR.set(data[1][3])
        self.secondaryskills_DEC_CHK_VAR.set(data[1][4])
        self.secondaryskills_HIS_CHK_VAR.set(data[1][5])
        self.secondaryskills_CHR_CHK_VAR.set(data[1][6])
        self.secondaryskills_IDT_CHK_VAR.set(data[1][7])
        self.secondaryskills_INV_CHK_VAR.set(data[1][8])
        self.secondaryskills_MED_CHK_VAR.set(data[1][9])
        self.secondaryskills_NAT_CHK_VAR.set(data[1][10])
        self.secondaryskills_PER_CHK_VAR.set(data[1][11])
        self.secondaryskills_PRF_CHK_VAR.set(data[1][12])
        self.secondaryskills_PRS_CHK_VAR.set(data[1][13])
        self.secondaryskills_REL_CHK_VAR.set(data[1][14])
        self.secondaryskills_SOH_CHK_VAR.set(data[1][15])
        self.secondaryskills_STE_CHK_VAR.set(data[1][16])
        self.secondaryskills_SRV_CHK_VAR.set(data[1][17])
#   text for personailty traits  _LIN
    def set_Backgrounds_misctraits_DPT_TXT_CLR(self):
        self.Backgrounds_misctraits_DPT_TXT.delete(1.0, 'end-1c')
    def set_Backgrounds_misctraits_DPT_TXT_LIN(self,x):##insert a single line
        self.Backgrounds_misctraits_DPT_TXT.insert(INSERT,x)
    def set_Backgrounds_misctraits_DPT_TXT(self,Larray):
        self.Backgrounds_misctraits_DPT_TXT.delete(1.0, 'end-1c')
        for x in Larray:
            self.Backgrounds_misctraits_DPT_TXT.insert(INSERT,x)
        
    def set_Backgrounds_misctraits_DPI_TXT_CLR(self):
        self.Backgrounds_misctraits_DPI_TXT.delete(1.0, 'end-1c')
    def set_Backgrounds_misctraits_DPI_TXT_LIN(self,x):
        self.Backgrounds_misctraits_DPI_TXT.insert(INSERT,x)
    def set_Backgrounds_misctraits_DPI_TXT(self,Larray):
        self.Backgrounds_misctraits_DPI_TXT.delete(1.0, 'end-1c')
        for x in Larray:
            self.Backgrounds_misctraits_DPI_TXT.insert(INSERT,x)
        
    def set_Backgrounds_misctraits_DPB_TXT_CLR(self):
        self.Backgrounds_misctraits_DPB_TXT.delete(1.0, 'end-1c')
    def set_Backgrounds_misctraits_DPB_TXT_LIN(self,x):
        self.Backgrounds_misctraits_DPB_TXT.insert(INSERT,x)
    def set_Backgrounds_misctraits_DPB_TXT(self,Larray):
        self.Backgrounds_misctraits_DPB_TXT.delete(1.0, 'end-1c')
        for x in Larray:
            self.Backgrounds_misctraits_DPB_TXT.insert(INSERT,x)
        
    def set_Backgrounds_misctraits_DPF_TXT_CLR(self):
        self.Backgrounds_misctraits_DPF_TXT.delete(1.0, 'end-1c')
    def set_Backgrounds_misctraits_DPI_TXT_LIN(self,x):
        self.Backgrounds_misctraits_DPI_TXT.insert(INSERT,x)
    def set_Backgrounds_misctraits_DPF_TXT(self,Larray):
        self.Backgrounds_misctraits_DPF_TXT.delete(1.0, 'end-1c')
        for x in Larray:
            self.Backgrounds_misctraits_DPF_TXT.insert(INSERT,x)
    ##inv txt
    #self.Backgrounds_misctraits_inventory_INV_TXT
    def set_Backgrounds_misctraits_inventory_INV_TXT_CLR(self):
        self.Backgrounds_misctraits_inventory_INV_TXT.delete(1.0, 'end-1c')
    def set_Backgrounds_misctraits_inventory_INV_TXT(self,Larray):
        self.Backgrounds_misctraits_inventory_INV_TXT.delete(1.0, 'end-1c')
        for x in Larray:
            self.Backgrounds_misctraits_inventory_INV_TXT.insert(INSERT,x)
    ##internal
    def internal_calcprofbonusplushpmisc(self):
        PROFBONUS_LVL = 2 ## i am going to expand this later to include starting level on the page but for now is fixed at 2 as character will be lvl 0 at start
        B_RM = self.get_Backgrounds_rollmod_LBL()##background rollmod
        P_RM = self.get_primaryattributes_LBL()##primary rollmod
        T_RM = []
        if 'NA' in P_RM:## if primary attributes are not calculated  dont calculate the rest
            pass
        else:
            for x in range(len(B_RM)):
                B_RM[x] = B_RM[x].split('|')[1]##splits then discards the first entry
                if B_RM[x] == '+-0':
                    B_RM[x] = '0'
            print('========\n',B_RM,'\n',P_RM,'\n========')
            #temp = []
            for x in range(len(B_RM)):#B_RM and P_RM are both same length
                T_RM.append(int(B_RM[x])+int(P_RM[x]))#add them together
                
    ##        ARRAY_HPMISC[0] = str(10+int(ARRAY_PATTR[1]))##armour class = 10+rollmod(dexterity)
    ##        ARRAY_HPMISC[5] = str(10+int(ARRAY_PATTR[1]))##hp max = 10+rollmod(dexterity)
    ##        ARRAY_HPMISC[3] = str(10+int(ARRAY_PATTR[1]))##current hp is the same as hp max as character is just starting
    ####      print(ARRAY_HPMISC)
    ####      input()
    ##        
    ##        ARRAY_PERCEPTION = str(10+int(ARRAY_PATTR_ROLLMOD[4])+int())##perception=10+wisdom rollmod+proficiency in perception
            
            ##update saving throws and skill proficiency bonuses
            A_SF = self.get_savingthrows()##array_savingthrows
            A_SP = self.get_secondaryskills()##array_skillproficiencies##sp not needed as lvl 0

            for x in range(len(A_SF)):
                print(A_SF[x])
                if A_SF[x][0] == 1:##if proficent put rollmod of primary attribute into box
                    A_SF[x] = [1,str(T_RM[x])]##reassign tuple as list ##EDIT now includes modifiers
                else:
                    A_SF[x] = [0,str('0')]##reassign tuple as list
                    
            for x in range(len(A_SP[1])):
                if A_SP[1][x] == 1:
                    A_SP[0][x] = str(PROFBONUS_LVL)
                else:
                    A_SP[0][x] = str(0)
                #A_SP[0][x] = str(PROFBONUS_LVL)

            #set the values
            self.set_savingthrows(A_SF)##array_savingthrows
            self.set_secondaryskills(A_SP)##array_skillproficiencies

            
            ##caclulate and update wisdom##EDIT: now done on finalisation of character
            #self.str(10+int(ARRAY_PATTR_ROLLMOD[4])+int())
                
            ##calculate and update hpmisc(hp and ac)
            temp = self.get_hpmiscskills()
            temp[0] = str(10+int(T_RM[1]))##armour class = 10+rollmod(dexterity)
            temp[1] = str(T_RM[1])##initiative = dex rollmod
            temp[5] = str(10+int(T_RM[1]))##hp max = 10+rollmod(dexterity)
            temp[3] = temp[5]#  = str(10+int(ARRAY_PATTR[1]))##current hp is the same as hp max as character is just starting
            self.set_hpmiscskills(temp)

            
    def internal_savefileaskchecker(self):##returns name and true if file exists
        FPath = filedialog.asksaveasfilename(filetypes=(("D&D character sheet", "*.MEGA"),("All Files", "*.*") ))##adv extention is forced onto ##EDIT took out this defaultextension=".ADV", 
        EXISTS_FLAG = False
        if os.path.isfile(FPath):# or os.path.isfile(FPath.strip('.ADV')):##hack to get around
            EXISTS_FLAG = True
        else:
            EXISTS_FLAG = False
        print(os.path.isfile(FPath))
        return[FPath,EXISTS_FLAG]
    
    def internal_calcrollmod_primary_LBL(self):##calculates the values for the roll modifers in the primary attribute window
        rollmod = []
        Bcontents = self.get_primaryattributes_BTN()##button text
        for x in range(len(Bcontents)):
            if Bcontents[x] == 'Set Value!':
                #Bcontents[x] = Bcontents[x].strip('Set Value!')
                Bcontents[x] = 100
            else:
                Bcontents[x] = int(Bcontents[x].strip('set as| '))

            if Bcontents[x] == 1:##max score = 18
                rollmod.append('-5')
            elif Bcontents[x] <= 3:
                rollmod.append('-4')
            elif Bcontents[x] <= 5:
                rollmod.append('-3')
            elif Bcontents[x] <= 7:
                rollmod.append('-2')
            elif Bcontents[x] <= 9:
                rollmod.append('-1')
            elif Bcontents[x] <= 11:
                rollmod.append('0')
            elif Bcontents[x] <= 13:
                rollmod.append('+1')
            elif Bcontents[x] <= 15:
                rollmod.append('+2')
            elif Bcontents[x] <= 17:
                rollmod.append('+3')
            elif Bcontents[x] <= 19:
                rollmod.append('+4')
            else:
                rollmod.append('NA')
        self.set_primaryattributes_LBL(rollmod)

    def internal_validaterolls(self):##checks rolls are valid when finalizing character
        VALID = True
        listvalues = self.internal_get_DRL_listbox()
        if len(listvalues) == 0:
            listvalues = [-1]*6
        else:
            listvalues = list(listvalues)
        
        btndat = self.get_primaryattributes_BTN()
        for x in range(len(btndat)):
            if btndat[x] == 'Set Value!':
                btndat[x] = -2##stops false positive in validation as listvalues invalid value is -1
            else:
                btndat[x] = int(btndat[x].strip('set as| '))
        print('|\n')
        print(listvalues)
        print(btndat)
        listvalues.sort()
        btndat.sort()
##        for x in range(len(btndat)):##sort list and compare against sorted list of the rng values
##            if listvalues[x] == 'Set Value!':
##                VALID = False
##            elif listvalues[x] == btndat[x]:
##                VALID = True
##            else:
##                VALID = False
##        return VALID
        for x in range(len(btndat)):##sort list and compare against sorted list of the rng values
            if listvalues[x] != btndat[x]:
                VALID = False
        return VALID
            
                
        
    def internal_button_primary_Resetvalues(self):
        self.primaryattributes_STR_BTN_VAR.set('Set Value!')
        self.primaryattributes_DEX_BTN_VAR.set('Set Value!')
        self.primaryattributes_CON_BTN_VAR.set('Set Value!')
        self.primaryattributes_INT_BTN_VAR.set('Set Value!')
        self.primaryattributes_WIS_BTN_VAR.set('Set Value!')
        self.primaryattributes_CHR_BTN_VAR.set('Set Value!')
        
    def internal_rollprimary(self):##rolls dice for primary attributes then returns them
        #4d6-lowest
        rolls = []
        for Pattr in range(0,6):
            temp = []
            tint = 0
            for droll in range(0,4):
                #print(random.randint(1,6))
                temp.append(random.randint(1,6))
            print(temp)
            temp.sort()
            #temp.remove(temp[0])
            for x in range(1,len(temp)-1):
                tint+=temp[x]
            rolls.append(tint)
        return rolls
                
    #dice roller listbox functions        
    def internal_get_DRL_currselection_listbox(self):
        try:
            return self.primaryattributes_setup_DRL_LBX.get(self.primaryattributes_setup_DRL_LBX.curselection())

        except:#catches exeption thrown by  null selection
            return False
            #return ['']*6

            
    def internal_refresh_DRL_listbox(self,dat):##for diceroll listbox
        self.internal_clear_DRL_listbox()
        self.internal_addlist_DRL_listbox(dat)
        
    def internal_clear_DRL_listbox(self):#clear roll box
        self.primaryattributes_setup_DRL_LBX.delete(0,self.primaryattributes_setup_DRL_LBX.size())
        
    def internal_additem_DRL_listbox(self,Litem):#add item to listbox
        self.primaryattributes_setup_DRL_LBX.insert(END,Litem)
        
    def internal_addlist_DRL_listbox(self,Listitems):#add list of items to listbox
        for x in Listitems:
            self.internal_additem_DRL_listbox(x)
            
    def internal_get_DRL_listbox(self):
            return self.primaryattributes_setup_DRL_LBX.get(0,self.primaryattributes_setup_DRL_LBX.size())

    ##end diceroller##
    ##################


    
    def internal_preload_data(self):#pre loads some data
        #race listbox
        ##populates class listbox with values
        
        print('loading')
        bgs = self.internal_process_getBG()
        print('bgs\n',bgs)
        self.internal_refresh_CBG_listbox(bgs)
        
        ##class listbox
        self.internal_refresh_CBO_listbox(['Cleric','Fighter','Rogue','Wizard'])
        
    def internal_process_getBG(self):##gets preset character backgrounds
        Files_dat = self.datamain.peek()
        #print('fdats\n',Files_dat)
        loaded_races =[]
        if 'Races.txt' in Files_dat:
            loaded_races = self.csv2array(self.datamain.fetch('Races.txt')[0])
        return loaded_races
    def internal_process_getTRT(self,name):
        pass

    #CharacterBackGround listbox functions
    #Backgrounds_setup_CBG_LBX
    def internal_get_CBG_currselection_listbox(self):
       #print(self.Backgrounds_setup_CBG_LBX.get(self.Backgrounds_setup_CBG_LBX.curselection()))
        try:
            return self.Backgrounds_setup_CBG_LBX.get(self.Backgrounds_setup_CBG_LBX.curselection())

        except:#catches exeption thrown by  null selection
            return False
        
    def internal_refresh_CBG_listbox(self,dat):##for character background listbox
        self.internal_clear_CBG_listbox()
        self.internal_addlist_CBG_listbox(dat)
        
    def internal_clear_CBG_listbox(self):#clear box
        self.Backgrounds_setup_CBG_LBX.delete(0,self.Backgrounds_setup_CBG_LBX.size())
        
    def internal_additem_CBG_listbox(self,Litem):#add item to listbox
        self.Backgrounds_setup_CBG_LBX.insert(END,Litem)
        
    def internal_addlist_CBG_listbox(self,Listitems):#add list of items to listbox
        for x in Listitems:
            self.internal_additem_CBG_listbox(x)
            
    def internal_get_CBG_listbox(self):
            return self.Backgrounds_setup_CBG_LBX.get(0,self.Backgrounds_setup_CBG_LBX.size())
    ########



    #Charactersubracelistbox functions
    #Backgrounds_setup_CBS_LBX
    def internal_get_CBS_currselection_listbox(self):
        #print(self.Backgrounds_setup_CBS_LBX.get(self.Backgrounds_setup_CBS_LBX.curselection()))
        try:
            return self.Backgrounds_setup_CBS_LBX.get(self.Backgrounds_setup_CBS_LBX.curselection())

        except:#catches exeption thrown by  null selection
            return False
        
    def internal_refresh_CBS_listbox(self,dat):##for character background listbox
        self.internal_clear_CBS_listbox()
        self.internal_addlist_CBS_listbox(dat)
        
    def internal_clear_CBS_listbox(self):#clear box
        self.Backgrounds_setup_CBS_LBX.delete(0,self.Backgrounds_setup_CBS_LBX.size())
        
    def internal_additem_CBS_listbox(self,Litem):#add item to listbox
        self.Backgrounds_setup_CBS_LBX.insert(END,Litem)
        
    def internal_addlist_CBS_listbox(self,Listitems):#add list of items to listbox
        for x in Listitems:
            self.internal_additem_CBS_listbox(x)
            
    def internal_get_CBS_listbox(self):
            return self.Backgrounds_setup_CBS_LBX.get(0,self.Backgrounds_setup_CBS_LBX.size())
        
    def internal_currselection_RAW_CBS_listbox(self):
        try:
            return self.Backgrounds_setup_CBS_LBX.curselection()
        except:
            return False
    def internal_setindex_CBS_listbox(self,Iitem):#change index in listbox
        self.Backgrounds_setup_CBS_LBX.activate(Iitem)
    ########

        
    #Characterclasslistbox functions
    #Backgrounds_setup_CBO_LBX
    def internal_get_CBO_currselection_listbox(self):
        #print(self.Backgrounds_setup_CBO_LBX.get(self.Backgrounds_setup_CBO_LBX.curselection()))
        try:
            return self.Backgrounds_setup_CBO_LBX.get(self.Backgrounds_setup_CBO_LBX.curselection())

        except:#catches exeption thrown by  null selection
            return False
        
    def internal_refresh_CBO_listbox(self,dat):##for character background listbox
        self.internal_clear_CBO_listbox()
        self.internal_addlist_CBO_listbox(dat)
        
    def internal_clear_CBO_listbox(self):#clear box
        self.Backgrounds_setup_CBO_LBX.delete(0,self.Backgrounds_setup_CBO_LBX.size())
        
    def internal_additem_CBO_listbox(self,Litem):#add item to listbox
        self.Backgrounds_setup_CBO_LBX.insert(END,Litem)
        
    def internal_addlist_CBO_listbox(self,Listitems):#add list of items to listbox
        for x in Listitems:
            self.internal_additem_CBO_listbox(x)
            
    def internal_get_CBO_listbox(self):
            return self.Backgrounds_setup_CBO_LBX.get(0,self.Backgrounds_setup_CBO_LBX.size())
        
    def internal_currselection_RAW_CBO_listbox(self):
        try:
            return self.Backgrounds_setup_CBO_LBX.curselection()
        except:
            return False
    def internal_setindex_CBO_listbox(self,Iitem):#change index in listbox
        self.Backgrounds_setup_CBO_LBX.activate(Iitem)
        
    ########

        
    def internal_stripbrackets(self,strng):
        return strng[:-1].strip('[')

    def button_sub_confirmbackground(self):
        lang_temp = []
        if self.internal_get_CBG_currselection_listbox() ==  False:
            pass
        else:
            racemain = self.internal_get_CBG_currselection_listbox()
            self.Backgrounds_setup_CBG_CURR_LBL_VAR.set(racemain)
            data = self.datamain.fetch((racemain+str('.txt')))
            subraces = self.csv2array(data[0])
            subraces.remove('[BGS]')
            self.internal_refresh_CBS_listbox(subraces)
            
            self.set_Backgrounds_traits_TRT_TXT_CLR()##clears traits
            self.set_Backgrounds_rollmod_LBL(##clears roll modifiers
                ['STR modifier|+-0',##default values
                       'DEX modifier|+-0',
                       'CON modifier|+-0',
                       'INT modifier|+-0',
                       'WIS modifier|+-0',
                       'CHR modifier|+-0'])#*6
            ##processing race languages
            for x in range(len(data)):
                    data[x] = self.csv2array(data[x])#arrays each entry
            for x in range(len(data)):
                if data[x][0] == '[LANG]':
                    data[x].remove('[LANG]')
                    for y in range(len(data[x])):
                        lang_temp.append(data[x][y]+'\n')
                        print(data[x][y])
                if data[x][0] == '[SPD]':
                    data[x].remove('[SPD]')
                    self.HPmiscskills_SPD_BOX_VAR.set(data[x][0])
            print(lang_temp)
            self.set_Backgrounds_LANG_TRT_TXT(lang_temp)##clears textbox then adds
            self.Backgrounds_setup_CBS_CURR_LBL_VAR.set('None selected!')##removes subrace label data 
            
            
            
    def button_sub_confirmsubrace(self):
        traits_temp = []
        lang_temp=[]
        if self.internal_get_CBS_currselection_listbox() ==  False or (self.Backgrounds_setup_CBG_CURR_LBL_VAR.get() =='None Selected!'):
            pass
        else:
            subrace = self.internal_get_CBS_currselection_listbox()
            self.Backgrounds_setup_CBS_CURR_LBL_VAR.set(subrace)
            data = self.datamain.fetch((self.Backgrounds_setup_CBG_CURR_LBL_VAR.get()+str('.txt')))
            #subraces = self.csv2array(data[0])
            for x in range(len(data)):
                data[x] = self.csv2array(data[x])
            
            print('done\n',data,'\n=========')
            dat2set = ['STR modifier|+-0',##default values
                       'DEX modifier|+-0',
                       'CON modifier|+-0',
                       'INT modifier|+-0',
                       'WIS modifier|+-0',
                       'CHR modifier|+-0']#*6
            print(len(dat2set))

            
            for x in range(len(data)):
                if data[x][0] == '[SBASE]':##stats decode
                    print('sbase//')
                    data[x].remove('[SBASE]')
                    #print(data[x])
                    for y in range(len(data[x])):
                        #print(data[x][y])
                        data[x][y] = data[x][y].split('=')
                        print(data[x][y])
                        #print(data)
                        if data[x][y][0] == 'STR':
                            dat2set[0] = 'STR modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'DEX':
                            dat2set[1] = 'DEX modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'CON':
                            dat2set[2] = 'CON modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'INT':
                            dat2set[3] = 'INT modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'WIS':
                            dat2set[4] = 'WIS modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'CHR':
                            dat2set[5] = 'CHR modifier|'+data[x][y][1]

                        
                elif data[x][0] == '[S'+subrace.upper()+']':
                    #data[x].remove(data[x][0])#(str('[S'+subrace.upper()+']'))##always the first entry to be removed
                    data[x].remove('[S'+subrace.upper()+']')
                    #input()
                    #print(data[x])
                    for y in range(len(data[x])):
                        #print(data[x][y])
                        data[x][y] = data[x][y].split('=')
                        print(data[x][y])
                        #print(data)
                        if data[x][y][0] == 'STR':
                            dat2set[0] = 'STR modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'DEX':
                            dat2set[1] = 'DEX modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'CON':
                            dat2set[2] = 'CON modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'INT':
                            dat2set[3] = 'INT modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'WIS':
                            dat2set[4] = 'WIS modifier|'+data[x][y][1]
                        elif data[x][y][0] == 'CHR':
                            dat2set[5] = 'CHR modifier|'+data[x][y][1]

                    
                elif data [x][0] == '[TBASE]':##traits
                    data[x].remove('[TBASE]')
                    for y in range(len(data[x])):
                        traits_temp.append(data[x][y]+'\n')
                                   
                elif data[x][0] == '[T'+subrace.upper()+']':
                    data[x].remove('[T'+subrace.upper()+']')
                    for y in range(len(data[x])):
                        traits_temp.append(data[x][y]+'\n')


##                elif data[x][0] == '[LANG]':##in wrong section
##                    data[x].remove('[LANG]')
##                    for y in range(len(data[x])):
##                        lang_temp.append(data[x][y]+'\n')
                
                
                            
            ##setting roll modifiers
            #dat2set[0] = 'aaa'
            print('setting',dat2set)
            self.set_Backgrounds_rollmod_LBL(dat2set)

            ##setting traits menu
            self.set_Backgrounds_traits_TRT_TXT(traits_temp)

            #setting languages
            #self.set_Backgrounds_LANG_TRT_TXT(lang_temp)
            

    def sub_button_confirmclass(self):#'Cleric','Fighter','Rogue','Wizard'
        if self.internal_get_CBO_currselection_listbox() ==  False:
            pass
        else:
            HITDICE = 'Dxx'
            PRIM_PROF = self.get_savingthrows()##gets proficiency for saving throws and refreshes them after updating
            SEC_PROF = self.get_secondaryskills()##secondary skill proficiency
            charclass = self.internal_get_CBO_currselection_listbox()
            INV = []
            self.Backgrounds_setup_CBO_CURR_LBL_VAR.set(charclass)
            self.set_Backgrounds_misctraits_inventory_INV_TXT_CLR()##clears inv

            #print('\n',SEC_PROF)
            #input(self.get_secondaryskills())
            
            #fetches data for specific background, loads numbers 1-4 into each listbox
            #display and populate listbox background table
            ##removes all proficienies
            for x in range(len(PRIM_PROF)):
                PRIM_PROF[x] = (0,PRIM_PROF[x][1])
                
##            for x in range(len(SEC_PROF)):
##                print(SEC_PROF[x])
##                SEC_PROF[x] = (0,SEC_PROF[x][1])
            for x in range(len(SEC_PROF[1])):
                SEC_PROF[1][x] = 0
            #print(SEC_PROF[1])

            #print('\n',SEC_PROF)
            #input(self.get_secondaryskills())
            #set specific attributes for each class here
            #print('charclass',charclass=='Cleric')
                ##actual backgrounds,cleric-acolyte,figter-soldier,rogue-criminal,wizard-sage,,
            if charclass == 'Cleric':
                HITDICE = 'D8'
                PRIM_PROF[4] = (1,PRIM_PROF[4][1])##assigns data as tuple (proficency flag,text in proficiency box)
                PRIM_PROF[5] = (1,PRIM_PROF[5][1])
                SEC_PROF[1][15] = 1#(1,SEC_PROF[15][1])
                SEC_PROF[1][6] = 1#(1,SEC_PROF[6][1])
                INV = ['A holy symbol (a gift to you when you entered the priesthood)\n','a prayer book or prayer wheel\n','5 sticks of incense\n','vestments\n','a set of common clothes\n','a pouch containing 15 gp\n','Priests Pack']
                
            elif charclass == 'Fighter':
                HITDICE = 'D10'
                PRIM_PROF[0] = (1,PRIM_PROF[0][1])
                PRIM_PROF[2] = (1,PRIM_PROF[2][1])
                SEC_PROF[1][3] = 1#(1,SEC_PROF[5][1])
                SEC_PROF[1][7] = 1#(1,SEC_PROF[2][1])
                INV = ['An insignia of rank\n', 'a trophy taken from a fallen enemy\n','a deck of cards\n','a set of common clothes\n','a pouch containing 10 gp\n','Dungeoneers Pack']
            elif charclass == 'Rogue':
                HITDICE = 'D8'
                PRIM_PROF[1] = (1,PRIM_PROF[1][1])
                PRIM_PROF[3] = (1,PRIM_PROF[3][1])
                SEC_PROF[1][4] = 1#(1,SEC_PROF[5][1])
                SEC_PROF[1][16] = 1#(1,SEC_PROF[2][1])
                INV = ['A crowbar\n','a set of dark common clothes including a hood\n','a pouch containing 15 gp\n','Burglars Pack']
                
            elif charclass == 'Wizard':
                HITDICE = 'D6'
                PRIM_PROF[3] = (1,PRIM_PROF[3][1])
                PRIM_PROF[4] = (1,PRIM_PROF[4][1])
                SEC_PROF[1][5] = 1#(1,SEC_PROF[5][1])
                SEC_PROF[1][2] = 1#(1,SEC_PROF[2][1])
                INV = ['A bottle of black ink\n','a quill\n','a small knife\n','a letter from a dead colleague posing a question\n you have not yet been able to answer\n','a set of common clothes\n','a pouch containing 10 gp\n','Scholars Pack']
                

            

            self.Backgrounds_hitdie_HTD_BOX_VAR.set(HITDICE)
            self.set_savingthrows(PRIM_PROF)
            self.set_secondaryskills(SEC_PROF)
            self.set_Backgrounds_misctraits_inventory_INV_TXT(INV)
            self.set_Backgrounds_misctraits_DPT_TXT_CLR()##clear backgrounds
            self.set_Backgrounds_misctraits_DPI_TXT_CLR()
            self.set_Backgrounds_misctraits_DPB_TXT_CLR()
            self.set_Backgrounds_misctraits_DPF_TXT_CLR()
            
            
    def internal_processbgtraitsdata(self,charclass,bgid):##sets up background class data based on background for testing
        data = self.datamain.fetch(charclass+'.txt')##repurposed as random
        for x in range(len(data)):
            data[x] = self.csv2array(data[x])
        for x in range(len(data)):
            if data[x][0] == '[BG1]':
                data[x].remove('[BG1]')
                
                #self.Backgrounds_misctraits_DPT_LBL_VAR.set(data[x][bgid[0]])##removed labels in favour of text entries
                print(bgid)
                #input()
                self.set_Backgrounds_misctraits_DPT_TXT(data[x][bgid[0]])
                #for y in range(len(data[x])):
                    #print('datagggg##~~',data[x][y])
                    #pass##set lbx for background as numbers
            elif data[x][0] == '[BG2]':
                data[x].remove('[BG2]')
                
                #self.Backgrounds_misctraits_DPI_LBL_VAR.set(data[x][bgid[1]])
                self.set_Backgrounds_misctraits_DPI_TXT(data[x][bgid[1]])

            elif data[x][0] == '[BG3]':
                data[x].remove('[BG3]')
                
                #self.Backgrounds_misctraits_DPB_LBL_VAR.set(data[x][bgid[2]])
                self.set_Backgrounds_misctraits_DPB_TXT(data[x][bgid[2]])

            elif data[x][0] == '[BG4]':
                data[x].remove('[BG4]')
                
                #self.Backgrounds_misctraits_DPF_LBL_VAR.set(data[x][bgid[3]])
                self.set_Backgrounds_misctraits_DPF_TXT(data[x][bgid[3]])
        #self.Backgrounds_misctraits_DPT_LBL_VAR.set()
        #self.Backgrounds_misctraits_DPI_LBL_VAR.set()
        #self.Backgrounds_misctraits_DPB_LBL_VAR.set()
        #self.Backgrounds_misctraits_DPF_LBL_VAR.set()

    def intenal_preload_traitselectiondata(self):##populates listbox with values
        self.Backgrounds_setup_misctraits_DPT_LBX.delete(0,self.Backgrounds_setup_misctraits_DPT_LBX.size())#.clear()
        self.Backgrounds_setup_misctraits_DPI_LBX.delete(0,self.Backgrounds_setup_misctraits_DPI_LBX.size())#.clear()
        self.Backgrounds_setup_misctraits_DPB_LBX.delete(0,self.Backgrounds_setup_misctraits_DPB_LBX.size())#.clear()
        self.Backgrounds_setup_misctraits_DPF_LBX.delete(0,self.Backgrounds_setup_misctraits_DPF_LBX.size())#.clear()

        self.Backgrounds_setup_misctraits_DPT_LBX.insert(END,'1')
        self.Backgrounds_setup_misctraits_DPT_LBX.insert(END,'2')
        self.Backgrounds_setup_misctraits_DPT_LBX.insert(END,'3')
        self.Backgrounds_setup_misctraits_DPT_LBX.insert(END,'4')

        self.Backgrounds_setup_misctraits_DPI_LBX.insert(END,'1')
        self.Backgrounds_setup_misctraits_DPI_LBX.insert(END,'2')
        self.Backgrounds_setup_misctraits_DPI_LBX.insert(END,'3')
        self.Backgrounds_setup_misctraits_DPI_LBX.insert(END,'4')

        self.Backgrounds_setup_misctraits_DPB_LBX.insert(END,'1')
        self.Backgrounds_setup_misctraits_DPB_LBX.insert(END,'2')
        self.Backgrounds_setup_misctraits_DPB_LBX.insert(END,'3')
        self.Backgrounds_setup_misctraits_DPB_LBX.insert(END,'4')

        self.Backgrounds_setup_misctraits_DPF_LBX.insert(END,'1')
        self.Backgrounds_setup_misctraits_DPF_LBX.insert(END,'2')
        self.Backgrounds_setup_misctraits_DPF_LBX.insert(END,'3')
        self.Backgrounds_setup_misctraits_DPF_LBX.insert(END,'4')
        
    #def sub_button_confirmtrait(self):
        #names = ['Cleric','Fighter','Rogue','Wizard']
        #self.internal_processbgtraitsdata(names[lbxget])
        
    def sub_button_confirmtrait_RNG(self):
        charclass = self.Backgrounds_setup_CBO_CURR_LBL_VAR.get()
        if charclass == 'None selected!':
            pass
        else:
            temp = []
            for x in range(0,4):
                temp.append(random.randint(0,3))
            self.internal_processbgtraitsdata(charclass,temp)
            
    def sub_button_confirmtrait_PERS(self):
        charclass = self.Backgrounds_setup_CBO_CURR_LBL_VAR.get()#self.internal_get_CBO_currselection_listbox()
        bgid = self.Backgrounds_setup_misctraits_DPT_LBX.curselection()##check
        bgid = bgid[0]#takes value out of tuple
        print(bgid)
        if charclass == 'None selected!':
            pass
        else:
            data = self.datamain.fetch(charclass+'.txt')
            for x in range(len(data)):
                data[x] = self.csv2array(data[x])
            for x in range(len(data)):
                if data[x][0] == '[BG1]':
                    data[x].remove('[BG1]')
                    
                    ##self.Backgrounds_misctraits_DPT_LBL_VAR.set(data[x][bgid])
                    self.set_Backgrounds_misctraits_DPT_TXT(data[x][bgid])
                    #for y in range(len(data[x])):
                        #print('datagggg##~~',data[x][y])
                        #pass##set lbx for background as numbers

                
    def sub_button_confirmtrait_IDEAL(self):
        charclass = self.Backgrounds_setup_CBO_CURR_LBL_VAR.get()#self.internal_get_CBO_currselection_listbox()
        bgid = self.Backgrounds_setup_misctraits_DPI_LBX.curselection()##check
        bgid = bgid[0]#takes value out of tuple
        print(bgid)
        if charclass == 'None selected!':
            pass
        else:
            data = self.datamain.fetch(charclass+'.txt')
            for x in range(len(data)):
                data[x] = self.csv2array(data[x])
            for x in range(len(data)):
                if data[x][0] == '[BG2]':
                    data[x].remove('[BG2]')
                    
                    ##self.Backgrounds_misctraits_DPI_LBL_VAR.set(data[x][bgid])
                    self.set_Backgrounds_misctraits_DPI_TXT(data[x][bgid])
                
    def sub_button_confirmtrait_BOND(self):
        charclass = self.Backgrounds_setup_CBO_CURR_LBL_VAR.get()#self.internal_get_CBO_currselection_listbox()
        bgid = self.Backgrounds_setup_misctraits_DPB_LBX.curselection()##check
        bgid = bgid[0]#takes value out of tuple
        print(bgid)
        if charclass == 'None selected!':
            pass
        else:
            data = self.datamain.fetch(charclass+'.txt')
            for x in range(len(data)):
                data[x] = self.csv2array(data[x])
            for x in range(len(data)):
                if data[x][0] == '[BG3]':
                    data[x].remove('[BG3]')
                    
                    ##self.Backgrounds_misctraits_DPB_LBL_VAR.set(data[x][bgid])
                    self.set_Backgrounds_misctraits_DPB_TXT(data[x][bgid])
                    
    def sub_button_confirmtrait_FLAW(self):
        charclass = self.Backgrounds_setup_CBO_CURR_LBL_VAR.get()#self.internal_get_CBO_currselection_listbox()
        bgid = self.Backgrounds_setup_misctraits_DPF_LBX.curselection()##check
        bgid = bgid[0]#takes value out of tuple
        print(bgid)
        if charclass == 'None selected!':
            pass
        else:
            data = self.datamain.fetch(charclass+'.txt')
            for x in range(len(data)):
                data[x] = self.csv2array(data[x])
            for x in range(len(data)):
                if data[x][0] == '[BG4]':
                    data[x].remove('[BG4]')
                    for y in range(len(data[x])):
                        if data[x][y] == '@':
                            pass##check for adding newlines
                            
                    
                    ##self.Backgrounds_misctraits_DPF_LBL_VAR.set(data[x][bgid])
                    self.set_Backgrounds_misctraits_DPF_TXT(data[x][bgid])
                
    