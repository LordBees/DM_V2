import tkinter as tk
import os,sys,random

##import other classes associated with this win
import Class_createcharwin, Class_optwin, Class_dicerollerwin

#import standard libs 
import BeeLibv3 as Blib
import Common


#class main_win:
#    def __init__(self,masterwin):
#        self.master = masterwin
#        self.This_win = tk.Frame(self.master)

class main_win:
    ##class related variables
    QS_path_currfile = ''
    Base_ADV = None
    ##TK start
    #This_win = Tk()
    ##variables
    IS_LOADED = False
    d='1'##testing of boxes


    
    

    def __init__(self,masterwin,mega_main_datafile):
        self.This_win = masterwin
        self.datamain = mega_main_datafile
        #self.frame = tk.Frame(self.master)
        
        self.This_win.title('Dungeon Master v1')##title and window dimensions
        self.This_win.geometry('640x720')
        #TK variables for storing data
        ##charbase_name
        self.charbase_name_CNM_BOX_VAR = tk.StringVar()
        self.charbase_name_IRL_BOX_VAR = tk.StringVar()
        self.charbase_name_CLS_BOX_VAR = tk.StringVar()
        self.charbase_name_LVL_BOX_VAR = tk.StringVar()
        self.charbase_name_FAC_BOX_VAR = tk.StringVar()
        self.charbase_name_RAC_BOX_VAR = tk.StringVar()
        self.charbase_name_EXP_BOX_VAR = tk.StringVar()
    
        ##primary attributes
        self.primaryattributes_STR_BOX_VAR = tk.StringVar()
        self.primaryattributes_DEX_BOX_VAR = tk.StringVar()
        self.primaryattributes_CON_BOX_VAR = tk.StringVar()
        self.primaryattributes_INT_BOX_VAR = tk.StringVar()
        self.primaryattributes_WIS_BOX_VAR = tk.StringVar()
        self.primaryattributes_CHR_BOX_VAR = tk.StringVar()

        #roll modifier
        self.primaryattributes_STR_MOD_BOX_VAR = tk.StringVar()
        self.primaryattributes_DEX_MOD_BOX_VAR = tk.StringVar()
        self.primaryattributes_CON_MOD_BOX_VAR = tk.StringVar()
        self.primaryattributes_INT_MOD_BOX_VAR = tk.StringVar()
        self.primaryattributes_WIS_MOD_BOX_VAR = tk.StringVar()
        self.primaryattributes_CHR_MOD_BOX_VAR = tk.StringVar()
    
        #perception
        self.Perception_PER_BOX_VAR = tk.StringVar()

    
        ##inspiration
        self.inspiration_STR_BOX_VAR = tk.StringVar()

    
        ##proficiency bonus
        self.proficiencybonus_STR_BOX_VAR = tk.StringVar()

    
        ##saving throws
        self.savingthrows_STR_CHK_VAR = tk.IntVar()##chkboxes
        self.savingthrows_DEX_CHK_VAR = tk.IntVar()
        self.savingthrows_CON_CHK_VAR = tk.IntVar()
        self.savingthrows_INT_CHK_VAR = tk.IntVar()
        self.savingthrows_WIS_CHK_VAR = tk.IntVar()
        self.savingthrows_CHR_CHK_VAR = tk.IntVar()
    
        self.savingthrows_STR_BOX_VAR = tk.StringVar()##entries
        self.savingthrows_DEX_BOX_VAR = tk.StringVar()
        self.savingthrows_CON_BOX_VAR = tk.StringVar()
        self.savingthrows_INT_BOX_VAR = tk.StringVar()
        self.savingthrows_WIS_BOX_VAR = tk.StringVar()
        self.savingthrows_CHR_BOX_VAR = tk.StringVar()

    
        ##secondary skills
        self.secondaryskills_ACR_CHK_VAR = tk.IntVar()
        self.secondaryskills_ACR_BOX_VAR = tk.StringVar()
        self.secondaryskills_ANH_CHK_VAR = tk.IntVar()
        self.secondaryskills_ANH_BOX_VAR = tk.StringVar()
        self.secondaryskills_ARC_CHK_VAR = tk.IntVar()
        self.secondaryskills_ARC_BOX_VAR = tk.StringVar()
        self.secondaryskills_ATH_CHK_VAR = tk.IntVar()
        self.secondaryskills_ATH_BOX_VAR = tk.StringVar()
        self.secondaryskills_DEC_CHK_VAR = tk.IntVar()
        self.secondaryskills_DEC_BOX_VAR = tk.StringVar()
        self.secondaryskills_HIS_CHK_VAR = tk.IntVar()
        self.secondaryskills_HIS_BOX_VAR = tk.StringVar()
        self.secondaryskills_CHR_CHK_VAR = tk.IntVar()
        self.secondaryskills_CHR_BOX_VAR = tk.StringVar()
        self.secondaryskills_IDT_CHK_VAR = tk.IntVar()
        self.secondaryskills_IDT_BOX_VAR = tk.StringVar()
        self.secondaryskills_INV_CHK_VAR = tk.IntVar()
        self.secondaryskills_INV_BOX_VAR = tk.StringVar()
        self.secondaryskills_MED_CHK_VAR = tk.IntVar()
        self.secondaryskills_MED_BOX_VAR = tk.StringVar()
        self.secondaryskills_NAT_CHK_VAR = tk.IntVar()
        self.secondaryskills_NAT_BOX_VAR = tk.StringVar()
        self.secondaryskills_PER_CHK_VAR = tk.IntVar()
        self.secondaryskills_PER_BOX_VAR = tk.StringVar()
        self.secondaryskills_PRF_CHK_VAR = tk.IntVar()
        self.secondaryskills_PRF_BOX_VAR = tk.StringVar()
        self.secondaryskills_PRS_CHK_VAR = tk.IntVar()
        self.secondaryskills_PRS_BOX_VAR = tk.StringVar()
        self.secondaryskills_REL_CHK_VAR = tk.IntVar()
        self.secondaryskills_REL_BOX_VAR = tk.StringVar()
        self.secondaryskills_SOH_CHK_VAR = tk.IntVar()
        self.secondaryskills_SOH_BOX_VAR = tk.StringVar()
        self.secondaryskills_STE_CHK_VAR = tk.IntVar()
        self.secondaryskills_STE_BOX_VAR = tk.StringVar()
        self.secondaryskills_SRV_CHK_VAR = tk.IntVar()
        self.secondaryskills_SRV_BOX_VAR = tk.StringVar()

    
        ##hpmiscskills
        self.HPmiscskills_AMC_BOX_VAR = tk.StringVar()
        self.HPmiscskills_INI_BOX_VAR = tk.StringVar()
        self.HPmiscskills_SPD_BOX_VAR = tk.StringVar()
        self.HPmiscskills_HMX_BOX_VAR = tk.StringVar()
        self.HPmiscskills_HTP_BOX_VAR = tk.StringVar()
        self.HPmiscskills_HCR_BOX_VAR = tk.StringVar()


        #dice saves and hit die
        self.diceandsavesmisc_HTD_BOX_VAR = tk.StringVar()
        self.diceandsavesmisc_DTO_BOX_VAR = tk.StringVar()
        self.diceandsavesmisc_DS1_CHK_VAR = tk.IntVar()
        self.diceandsavesmisc_DS2_CHK_VAR = tk.IntVar()
        self.diceandsavesmisc_DS3_CHK_VAR = tk.IntVar()
        self.diceandsavesmisc_DF1_CHK_VAR = tk.IntVar()
        self.diceandsavesmisc_DF2_CHK_VAR = tk.IntVar()
        self.diceandsavesmisc_DF3_CHK_VAR = tk.IntVar()

    
         #attackplusspells
        self.attackplusspells_WN1_BOX_VAR = tk.StringVar()
        self.attackplusspells_WN2_BOX_VAR = tk.StringVar()
        self.attackplusspells_WN3_BOX_VAR = tk.StringVar()
         #atk bonus
        self.attackplusspells_AB1_BOX_VAR = tk.StringVar()
        self.attackplusspells_AB2_BOX_VAR = tk.StringVar()
        self.attackplusspells_AB3_BOX_VAR = tk.StringVar()
         #damage/type
        self.attackplusspells_DT1_BOX_VAR = tk.StringVar()
        self.attackplusspells_DT2_BOX_VAR = tk.StringVar()
        self.attackplusspells_DT3_BOX_VAR = tk.StringVar()
        self.attackplusspells_MSC_TXT = tk.StringVar()##hack for getting data out of text box(assigned as tk.StringVar temp to ensure .get() can be found

        ##hack for getting data out of text box(assigned as tk.StringVar temp to ensure .get() can be found before assignment
        #traits/lang box
        self.languagesplusskills_TBX_TXT = tk.StringVar()

    
        #equip/inventory
        self.equipmain_TBX_TXT = tk.StringVar()

    
        #traits
        self.personalinfo_traits_TBX_TXT = tk.StringVar()
        self.personalinfo_ideals_TBX_TXT = tk.StringVar()
        self.personalinfo_bonds_TBX_TXT = tk.StringVar()
        self.personalinfo_flaws_TBX_TXT = tk.StringVar()
        self.personalinfo_features_TBX_TXT = tk.StringVar()
        ##widgets

        ##charbase_name
        charbase_name_LF = tk.LabelFrame(self.This_win,text = 'primary info')
        charbase_name_CNM_BOX = tk.Entry(charbase_name_LF,textvariable = self.charbase_name_CNM_BOX_VAR).grid(row=0,column=1)
        charbase_name_CNM_LBL = tk.Label(charbase_name_LF,text = 'character name:').grid(row=0,column=0)
        charbase_name_IRL_BOX = tk.Entry(charbase_name_LF,textvariable = self.charbase_name_IRL_BOX_VAR).grid(row=1,column=1)
        charbase_name_IRL_LBL = tk.Label(charbase_name_LF,text = 'player name:').grid(row=1,column=0)
        charbase_name_CLS_BOX = tk.Entry(charbase_name_LF,textvariable = self.charbase_name_CLS_BOX_VAR).grid(row=1,column=3)
        charbase_name_CLS_LBL = tk.Label(charbase_name_LF,text = 'player class:').grid(row=1,column=2)
        charbase_name_LVL_BOX = tk.Entry(charbase_name_LF,textvariable = self.charbase_name_LVL_BOX_VAR).grid(row=0,column=3)
        charbase_name_LVL_LBL = tk.Label(charbase_name_LF,text = 'player level:').grid(row=0,column=2)
        charbase_name_FAC_BOX = tk.Entry(charbase_name_LF,textvariable = self.charbase_name_FAC_BOX_VAR).grid(row=0,column=5)
        charbase_name_FAC_LBL = tk.Label(charbase_name_LF,text = 'player faction:').grid(row=0,column=4)
        charbase_name_RAC_BOX = tk.Entry(charbase_name_LF,textvariable = self.charbase_name_RAC_BOX_VAR).grid(row=1,column=5)
        charbase_name_RAC_LBL = tk.Label(charbase_name_LF,text = 'player race:').grid(row=1,column=4)
        charbase_name_EXP_BOX = tk.Entry(charbase_name_LF,width = 5,textvariable = self.charbase_name_EXP_BOX_VAR).grid(row=0,column=7)
        charbase_name_EXP_LBL = tk.Label(charbase_name_LF,text = 'player experience:').grid(row=0,column=6)
        charbase_name_LF.place(x=75,y=0)
        
        #primaryattributes_LF
        primaryattributes_LF = tk.LabelFrame(self.This_win,text = 'primary\nattributes')
        primaryattributes_STR_BOX = tk.Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_STR_BOX_VAR).pack()
        primaryattributes_STR_LBL = tk.Label(primaryattributes_LF,text = 'Strength').pack()
        primaryattributes_DEX_BOX = tk.Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_DEX_BOX_VAR).pack()
        primaryattributes_DEX_LBL = tk.Label(primaryattributes_LF,text = 'Dexterity').pack()
        primaryattributes_CON_BOX = tk.Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_CON_BOX_VAR).pack()
        primaryattributes_CON_LBL = tk.Label(primaryattributes_LF,text = 'Constitution').pack()
        primaryattributes_INT_BOX = tk.Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_INT_BOX_VAR).pack()
        primaryattributes_INT_LBL = tk.Label(primaryattributes_LF,text = 'Intelligence').pack()
        primaryattributes_WIS_BOX = tk.Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_WIS_BOX_VAR).pack()
        primaryattributes_WIS_LBL = tk.Label(primaryattributes_LF,text = 'Wisdom').pack()
        primaryattributes_CHR_BOX = tk.Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_CHR_BOX_VAR).pack()
        primaryattributes_CHR_LBL = tk.Label(primaryattributes_LF,text = 'Charisma').pack()
        primaryattributes_LF.place(x=50,y=75)##was w3

        ##roll modifier
        #primaryattributes_LF
        primaryattributes_MOD_LF = tk.LabelFrame(self.This_win,text = 'Roll\nModifiers')
        primaryattributes_STR_MOD_BOX = tk.Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_STR_MOD_BOX_VAR).pack()
        primaryattributes_STR_MOD_LBL = tk.Label(primaryattributes_MOD_LF,text = 'Strength').pack()
        primaryattributes_DEX_MOD_BOX = tk.Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_DEX_MOD_BOX_VAR).pack()
        primaryattributes_DEX_MOD_LBL = tk.Label(primaryattributes_MOD_LF,text = 'Dexterity').pack()
        primaryattributes_CON_MOD_BOX = tk.Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_CON_MOD_BOX_VAR).pack()
        primaryattributes_CON_MOD_LBL = tk.Label(primaryattributes_MOD_LF,text = 'Constitution').pack()
        primaryattributes_INT_MOD_BOX = tk.Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_INT_MOD_BOX_VAR).pack()
        primaryattributes_INT_MOD_LBL = tk.Label(primaryattributes_MOD_LF,text = 'Intelligence').pack()
        primaryattributes_WIS_MOD_BOX = tk.Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_WIS_MOD_BOX_VAR).pack()
        primaryattributes_WIS_MOD_LBL = tk.Label(primaryattributes_MOD_LF,text = 'Wisdom').pack()
        primaryattributes_CHR_MOD_BOX = tk.Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_CHR_MOD_BOX_VAR).pack()
        primaryattributes_CHR_MOD_LBL = tk.Label(primaryattributes_MOD_LF,text = 'Charisma').pack()
        primaryattributes_MOD_LF.place(x=125,y=75)

        ##Perception
        Perception_LF = tk.LabelFrame(self.This_win,text = 'passive wisdom')
        Perception_PER_BOX = tk.Entry(Perception_LF,width = 5,textvariable = self.Perception_PER_BOX_VAR).grid(row = 0,column=0)#.pack()
        Perception_PER_BOX = tk.Label(Perception_LF,text = 'Perception').grid(row = 0,column=1)#.pack()
        Perception_LF.place(x=50,y=350)

    
        ##inspiration_LF
        inspiration_LF = tk.LabelFrame(self.This_win,text = ' inspiration points ')
        inspiration_STR_BOX = tk.Entry(inspiration_LF,width = 5,textvariable = self.inspiration_STR_BOX_VAR).grid(row = 0,column=1)#.pack()
        inspiration_STR_LBL = tk.Label(inspiration_LF,text = 'inspiration            ').grid(row = 0,column=0)#.pack()
        inspiration_LF.place(x=225,y=75)

        #proficiencybonus_LF
        proficiencybonus_LF = tk.LabelFrame(self.This_win,text = ' proficiency Bonus ')
        proficiencybonus_STR_BOX = tk.Entry(proficiencybonus_LF,width = 5,textvariable = self.proficiencybonus_STR_BOX_VAR).grid(row = 1,column=1)#.pack()
        proficiencybonus_STR_LBL = tk.Label(proficiencybonus_LF,text = 'Proficiency bonus').grid(row = 1,column=0)#.pack()
        proficiencybonus_LF.place(x=225,y=115)

        #savingthrows_LF
        savingthrows_LF = tk.LabelFrame(self.This_win,text = 'Saving Throws')
        savingthrows_STR_CHK = tk.Checkbutton(savingthrows_LF,variable =           self.savingthrows_STR_CHK_VAR).grid(row = 0,column=0)#.pack()
        savingthrows_STR_BOX = tk.Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_STR_BOX_VAR).grid(row = 0,column=1)#.pack()
        savingthrows_STR_LBL = tk.Label(savingthrows_LF,text = 'Strength')                                     .grid(row = 0,column=2)#.pack()
        savingthrows_DEX_CHK = tk.Checkbutton(savingthrows_LF,variable =           self.savingthrows_DEX_CHK_VAR).grid(row = 1,column=0)#.pack()
        savingthrows_DEX_BOX = tk.Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_DEX_BOX_VAR).grid(row = 1,column=1)#.pack()
        savingthrows_DEX_LBL = tk.Label(savingthrows_LF,text = 'Dexterity')                                    .grid(row = 1,column=2)#.pack()
        savingthrows_CON_CHK = tk.Checkbutton(savingthrows_LF,variable =           self.savingthrows_CON_CHK_VAR).grid(row = 2,column=0)#.pack()
        savingthrows_CON_BOX = tk.Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CON_BOX_VAR).grid(row = 2,column=1)#.pack()
        savingthrows_CON_LBL = tk.Label(savingthrows_LF,text = 'Constitution')                                 .grid(row = 2,column=2)#.pack()
        savingthrows_INT_CHK = tk.Checkbutton(savingthrows_LF,variable =           self.savingthrows_INT_CHK_VAR).grid(row = 3,column=0)#.pack()
        savingthrows_INT_BOX = tk.Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_INT_BOX_VAR).grid(row = 3,column=1)#.pack()
        savingthrows_INT_LBL = tk.Label(savingthrows_LF,text = 'Intelligence')                                 .grid(row = 3,column=2)#.pack()
        savingthrows_WIS_CHK = tk.Checkbutton(savingthrows_LF,variable =           self.savingthrows_WIS_CHK_VAR).grid(row = 4,column=0)#.pack()
        savingthrows_WIS_BOX = tk.Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_WIS_BOX_VAR).grid(row = 4,column=1)#.pack()
        savingthrows_WIS_LBL = tk.Label(savingthrows_LF,text = 'Wisdom')                                       .grid(row = 4,column=2)#.pack()
        savingthrows_CHR_CHK = tk.Checkbutton(savingthrows_LF,variable =           self.savingthrows_CHR_CHK_VAR).grid(row = 5,column=0)#.pack()
        savingthrows_CHR_BOX = tk.Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CHR_BOX_VAR).grid(row = 5,column=1)#.pack()
        savingthrows_CHR_LBL = tk.Label(savingthrows_LF,text = 'Charisma')                                     .grid(row = 5,column=2)#.pack()
        savingthrows_LF.place(x=225,y=155)

        #secondaryskills_LF
        secondaryskills_LF = tk.LabelFrame(self.This_win,text = 'skills')
        secondaryskills_ACR_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ACR_CHK_VAR).grid(row=0,column=0)#).pack(side=LEFT)
        secondaryskills_ACR_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ACR_BOX_VAR).grid(row=0,column=1)#.pack()
        secondaryskills_ACR_LBL = tk.Label(secondaryskills_LF,text = 'acrobatics').grid(row=0,column=2)#.pack()
        secondaryskills_ANH_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ANH_CHK_VAR).grid(row=1,column=0)#.pack()
        secondaryskills_ANH_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ANH_BOX_VAR).grid(row=1,column=1)#.pack()
        secondaryskills_ANH_LBL = tk.Label(secondaryskills_LF,text = 'animal handling').grid(row=1,column=2)#.pack()
        secondaryskills_ARC_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ARC_CHK_VAR).grid(row=2,column=0)#.pack()
        secondaryskills_ARC_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ARC_BOX_VAR).grid(row=2,column=1)#.pack()
        secondaryskills_ARC_LBL = tk.Label(secondaryskills_LF,text = 'arcana').grid(row=2,column=2)#.pack()
        secondaryskills_ATH_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ATH_CHK_VAR).grid(row=3,column=0)#.pack()
        secondaryskills_ATH_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ATH_BOX_VAR).grid(row=3,column=1)#.pack()
        secondaryskills_ATH_LBL = tk.Label(secondaryskills_LF,text = 'athletics').grid(row=3,column=2)#.pack()
        secondaryskills_DEC_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_DEC_CHK_VAR).grid(row=4,column=0)#.pack()
        secondaryskills_DEC_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_DEC_BOX_VAR).grid(row=4,column=1)#.pack()
        secondaryskills_DEC_LBL = tk.Label(secondaryskills_LF,text = 'deception').grid(row=4,column=2)#.pack()
        secondaryskills_HIS_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_HIS_CHK_VAR).grid(row=5,column=0)#.pack()
        secondaryskills_HIS_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_HIS_BOX_VAR).grid(row=5,column=1)#.pack()
        secondaryskills_HIS_LBL = tk.Label(secondaryskills_LF,text = 'history').grid(row=5,column=2)#.pack()
        secondaryskills_CHR_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_CHR_CHK_VAR).grid(row=6,column=0)#.pack()
        secondaryskills_CHR_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_CHR_BOX_VAR).grid(row=6,column=1)#.pack()
        secondaryskills_CHR_LBL = tk.Label(secondaryskills_LF,text = 'insight').grid(row=6,column=2)#.pack()
        secondaryskills_IDT_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_IDT_CHK_VAR).grid(row=7,column=0)#.pack()
        secondaryskills_IDT_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_IDT_BOX_VAR).grid(row=7,column=1)#.pack()
        secondaryskills_IDT_LBL = tk.Label(secondaryskills_LF,text = 'intimidation').grid(row=7,column=2)#.pack()
        secondaryskills_INV_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_INV_CHK_VAR).grid(row=8,column=0)#.pack()
        secondaryskills_INV_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_INV_BOX_VAR).grid(row=8,column=1)#.pack()
        secondaryskills_INV_LBL = tk.Label(secondaryskills_LF,text = 'investigation').grid(row=8,column=2)#.pack()
        secondaryskills_MED_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_MED_CHK_VAR).grid(row=9,column=0)#.pack()
        secondaryskills_MED_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_MED_BOX_VAR).grid(row=9,column=1)#.pack()
        secondaryskills_MED_LBL = tk.Label(secondaryskills_LF,text = 'medicine').grid(row=9,column=2)#.pack()
        secondaryskills_NAT_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_NAT_CHK_VAR).grid(row=10,column=0)#.pack()
        secondaryskills_NAT_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_NAT_BOX_VAR).grid(row=10,column=1)#.pack()
        secondaryskills_NAT_LBL = tk.Label(secondaryskills_LF,text = 'nature').grid(row=10,column=2)#.pack()
        secondaryskills_PER_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PER_CHK_VAR).grid(row=11,column=0)#.pack()
        secondaryskills_PER_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PER_BOX_VAR).grid(row=11,column=1)#.pack()
        secondaryskills_PER_LBL = tk.Label(secondaryskills_LF,text = 'perception').grid(row=11,column=2)#.pack()
        secondaryskills_PRF_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PRF_CHK_VAR).grid(row=12,column=0)#.pack()
        secondaryskills_PRF_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PRF_BOX_VAR).grid(row=12,column=1)#.pack()
        secondaryskills_PRF_LBL = tk.Label(secondaryskills_LF,text = 'performance').grid(row=12,column=2)#.pack()
        secondaryskills_PRS_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PRS_CHK_VAR).grid(row=13,column=0)#.pack()
        secondaryskills_PRS_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PRS_BOX_VAR).grid(row=13,column=1)#.pack()
        secondaryskills_PRS_LBL = tk.Label(secondaryskills_LF,text = 'persuasion').grid(row=13,column=2)#.pack()
        secondaryskills_REL_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_REL_CHK_VAR).grid(row=14,column=0)#.pack()
        secondaryskills_REL_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_REL_BOX_VAR).grid(row=14,column=1)#.pack()
        secondaryskills_REL_LBL = tk.Label(secondaryskills_LF,text = 'religion').grid(row=14,column=2)#.pack()
        secondaryskills_SOH_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_SOH_CHK_VAR).grid(row=15,column=0)#.pack()
        secondaryskills_SOH_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_SOH_BOX_VAR).grid(row=15,column=1)#.pack()
        secondaryskills_SOH_LBL = tk.Label(secondaryskills_LF,text = 'sleight of hand').grid(row=15,column=2)#.pack()
        secondaryskills_STE_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_STE_CHK_VAR).grid(row=16,column=0)#.pack()
        secondaryskills_STE_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_STE_BOX_VAR).grid(row=16,column=1)#.pack()
        secondaryskills_STE_LBL = tk.Label(secondaryskills_LF,text = 'stealth').grid(row=16,column=2)#.pack()
        secondaryskills_SRV_CHK = tk.Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_SRV_CHK_VAR).grid(row=17,column=0)#.pack()
        secondaryskills_SRV_BOX = tk.Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_SRV_BOX_VAR).grid(row=17,column=1)#.pack()
        secondaryskills_SRV_LBL = tk.Label(secondaryskills_LF,text = 'survival').grid(row=17,column=2)#.pack()
        secondaryskills_LF.place(x=225,y=325)        

        ##hpmiscskills_LF
        HPmiscskills_LF = tk.LabelFrame(self.This_win,text = 'HP/misc')
        HPmiscskills_AMC_BOX = tk.Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_AMC_BOX_VAR)             .grid(row=1,column=0)#.pack()
        HPmiscskills_AMC_LBL = tk.Label(HPmiscskills_LF,text = 'armour class') .grid(row=0,column=0)#.pack()
        HPmiscskills_INI_BOX = tk.Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_INI_BOX_VAR)             .grid(row=1,column=1)#.pack()
        HPmiscskills_INI_LBL = tk.Label(HPmiscskills_LF,text = 'initiative')   .grid(row=0,column=1)#.pack()
        HPmiscskills_SPD_BOX = tk.Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_SPD_BOX_VAR)             .grid(row=1,column=2)#.pack()
        HPmiscskills_SPD_LBL = tk.Label(HPmiscskills_LF,text = 'Speed')        .grid(row=0,column=2)#.pack()
        
        HPmiscskills_HMX_BOX = tk.Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HMX_BOX_VAR)             .grid(row=4,column=1)#.pack()
        HPmiscskills_HMX_LBL = tk.Label(HPmiscskills_LF,text = 'MAX HP')        .grid(row=4,column=0)#.pack()
        HPmiscskills_HTP_BOX = tk.Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HTP_BOX_VAR)              .grid(row=5,column=1)#.pack()
        HPmiscskills_HTP_LBL = tk.Label(HPmiscskills_LF,text = 'temp HP')        .grid(row=5,column=0)#.pack()
        HPmiscskills_HCR_BOX = tk.Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HCR_BOX_VAR)              .grid(row=6,column=1)#.pack()
        HPmiscskills_HCR_LBL = tk.Label(HPmiscskills_LF,text = 'current HP')        .grid(row=6,column=0)#.pack()
        HPmiscskills_LF.place(x=400,y=75)#50)##was 375

        ##hitdicedeathsave
        #diceandsavesmisc
        diceandsavesmisc_LF = tk.LabelFrame(self.This_win,text = 'dice/death saves')
        diceandsavesmisc_HTD_BOX = tk.Entry(diceandsavesmisc_LF,width = 5,textvariable = self.diceandsavesmisc_HTD_BOX_VAR)             .grid(row=1,column=0)#.pack()
        diceandsavesmisc_HTD_LBL = tk.Label(diceandsavesmisc_LF,text = 'hit dice') .grid(row=0,column=0)#.pack()
        diceandsavesmisc_DTO_BOX = tk.Entry(diceandsavesmisc_LF,width = 5,textvariable = self.diceandsavesmisc_DTO_BOX_VAR)             .grid(row=3,column=0)#.pack()
        diceandsavesmisc_DTO_LBL = tk.Label(diceandsavesmisc_LF,text = 'dice total')   .grid(row=2,column=0)#.pack()
        diceandsavesmisc_DSS_LBL = tk.Label(diceandsavesmisc_LF,text = 'sucesses')        .grid(row=1,column=1)#.pack()
        diceandsavesmisc_DS1_CHK = tk.Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DS1_CHK_VAR)        .grid(row=1,column=2)#.pack()
        diceandsavesmisc_DS2_CHK = tk.Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DS2_CHK_VAR)        .grid(row=1,column=3)#.pack()
        diceandsavesmisc_DS3_CHK = tk.Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DS3_CHK_VAR)        .grid(row=1,column=4)#.pack()
        diceandsavesmisc_DSF_LBL = tk.Label(diceandsavesmisc_LF,text = 'fails')        .grid(row=2,column=1)#.pack()
        diceandsavesmisc_DF1_CHK = tk.Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DF1_CHK_VAR)        .grid(row=2,column=2)#.pack()
        diceandsavesmisc_DF2_CHK = tk.Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DF2_CHK_VAR)        .grid(row=2,column=3)#.pack()
        diceandsavesmisc_DF3_CHK = tk.Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DF3_CHK_VAR)        .grid(row=2,column=4)#.pack()
        diceandsavesmisc_LF.place(x=400,y=200)

        ##attackplusspells_LF
        attackplusspells_LF = tk.LabelFrame(self.This_win,text = 'attack/magic stats')
        attackplusspells_WNM_LBL = tk.Label(attackplusspells_LF,text = 'name') .grid(row=0,column=0)#.pack()
        attackplusspells_WN1_BOX = tk.Entry(attackplusspells_LF,width = 7,textvariable = self.attackplusspells_WN1_BOX_VAR)             .grid(row=1,column=0)#.pack()
        attackplusspells_WN2_BOX = tk.Entry(attackplusspells_LF,width = 7,textvariable = self.attackplusspells_WN2_BOX_VAR)             .grid(row=2,column=0)#.pack()
        attackplusspells_WN3_BOX = tk.Entry(attackplusspells_LF,width = 7,textvariable = self.attackplusspells_WN3_BOX_VAR)             .grid(row=3,column=0)#.pack()
        attackplusspells_ATK_LBL = tk.Label(attackplusspells_LF,text = 'atk bonus') .grid(row=0,column=1)#.pack()
        attackplusspells_AB1_BOX = tk.Entry(attackplusspells_LF,width = 3,textvariable = self.attackplusspells_AB1_BOX_VAR)             .grid(row=1,column=1)#.pack()
        attackplusspells_AB2_BOX = tk.Entry(attackplusspells_LF,width = 3,textvariable = self.attackplusspells_AB2_BOX_VAR)             .grid(row=2,column=1)#.pack()
        attackplusspells_AB3_BOX = tk.Entry(attackplusspells_LF,width = 3,textvariable = self.attackplusspells_AB3_BOX_VAR)             .grid(row=3,column=1)#.pack()
        attackplusspells_DTY_LBL = tk.Label(attackplusspells_LF,text = 'damage/type') .grid(row=0,column=2)#.pack()
        attackplusspells_DT1_BOX = tk.Entry(attackplusspells_LF,width = 9,textvariable = self.attackplusspells_DT1_BOX_VAR)             .grid(row=1,column=2)#.pack()
        attackplusspells_DT2_BOX = tk.Entry(attackplusspells_LF,width = 9,textvariable = self.attackplusspells_DT2_BOX_VAR)             .grid(row=2,column=2)#.pack()
        attackplusspells_DT3_BOX = tk.Entry(attackplusspells_LF,width = 9,textvariable = self.attackplusspells_DT3_BOX_VAR)             .grid(row=3,column=2)#.pack()
        attackplusspells_NTS_LF =  tk.LabelFrame(self.This_win,text = 'atk/mag notes')#position by magic/stats
        self.attackplusspells_MSC_TXT = tk.Text(attackplusspells_NTS_LF,height = 25,width = 22)#add scrollbar to list
        self.attackplusspells_MSC_TXT                                                                                                .grid(row=4,column=0)#.pack() ##was height 10
        attackplusspells_NTS_LF.place(x=400,y=425)
        #add txt to fill spaces
        attackplusspells_LF.place(x=400,y=325)

        #language+misc skills LF
        languagesplusskills_LF = tk.LabelFrame(self.This_win,text = 'proficiencies and languages')
        self.languagesplusskills_TBX_TXT = tk.Text(languagesplusskills_LF,height = 10,width = 25)#add scrollbar to list
        self.languagesplusskills_TBX_TXT.grid(row=0,column=0)
        languagesplusskills_LF.place(x=825,y=75)

        #inventory LF
        equipmain_LF = tk.LabelFrame(self.This_win,text = 'inventory')
        self.equipmain_TBX_TXT = tk.Text(equipmain_LF,height = 25,width = 25)#add scrollbar to list
        self.equipmain_TBX_TXT.grid(row=0,column=0)
        equipmain_LF.place(x=825,y=255)

        #personalinfo_basic
        personalinfo_traits_LF = tk.LabelFrame(self.This_win,text = 'misc personality traits')
        self.personalinfo_traits_TBX_TXT = tk.Text(personalinfo_traits_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_traits_TBX_TXT.grid(row=0,column=0)
        personalinfo_traits_LF.place(x=600,y=75)

        #ideals
        personalinfo_ideals_LF = tk.LabelFrame(self.This_win,text = 'ideals')
        self.personalinfo_ideals_TBX_TXT = tk.Text(personalinfo_ideals_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_ideals_TBX_TXT.grid(row=0,column=0)
        personalinfo_ideals_LF.place(x=600,y=125)

        #bond
        personalinfo_bonds_LF = tk.LabelFrame(self.This_win,text = 'bonds')
        self.personalinfo_bonds_TBX_TXT = tk.Text(personalinfo_bonds_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_bonds_TBX_TXT.grid(row=0,column=0)
        personalinfo_bonds_LF.place(x=600,y=225)

        #personailty flaw
        personalinfo_flaws_LF = tk.LabelFrame(self.This_win,text = 'flaws')
        self.personalinfo_flaws_TBX_TXT = tk.Text(personalinfo_flaws_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_flaws_TBX_TXT.grid(row=0,column=0)
        personalinfo_flaws_LF.place(x=600,y=325)

        #other personailty feature
        personalinfo_features_LF = tk.LabelFrame(self.This_win,text = 'personality traits')
        self.personalinfo_features_TBX_TXT = tk.Text(personalinfo_features_LF,height = 25,width = 25)#add scrollbar to list
        self.personalinfo_features_TBX_TXT.grid(row=0,column=0)
        personalinfo_features_LF.place(x=600,y=425)

##        languagesplusskills_TBX_TXT
##        equipmain_TBX_TXT
##        personalinfo_traits_TBX_TXT
##        personalinfo_ideals_TBX_TXT
##        personalinfo_bonds_TBX_TXT
##        personalinfo_flaws_TBX_TXT
##        personalinfo_features_TBX_TXT

        ###print(self.get_primaryattributes())
        ##print(self.get_savingthrows())
        #print(self.attackplusspells_MSC_TXT)
        
        ##defining topbar menu on the top of the main window
        Menu_main = tk.Menu(self.This_win)

        ##file io dropdown on menubar
        Menu_FileIO = tk.Menu(Menu_main,tearoff = 0)##file tab
        Menu_FileIO.add_command(label="New", command=self.sub_button_newfile)
        Menu_FileIO.add_command(label="Load", command=self.sub_button_loadfile)
        Menu_FileIO.add_command(label="Save", command=self.sub_button_savefile)
        Menu_FileIO.add_command(label="Save As", command=self.sub_button_savefile_as)

        #settings dropdown on the menubar
        Menu_settings =tk.Menu(Menu_main,tearoff = 0)##tools tab
        #Menu_settings = Menu(menubar, tearoff=0)
        Menu_settings.add_command(label="dice roller", command = self.sub_button_domenu_dicewin)#, command=dicewin)
        Menu_settings.add_command(label="combat helper",state = tk.DISABLED)#,state = DISABLED)#, command=Menu_customchoose_window)

        ##top menu(the strip across the top of the windw with the options on)
        ##define menu dropdowns
        Menu_main.add_cascade(label = '|File|',menu = Menu_FileIO)
        Menu_main.add_cascade(label = '|Tools|',menu = Menu_settings)
        Menu_main.add_command(label="|Options|", command = self.sub_button_domenu_optwin, state = tk.DISABLED)#,command = optwin,state = DISABLED)#, command=Menu_preview_window)##EDIT disabled button
        Menu_main.add_command(label="|create new preset character|", command = self.sub_button_domenu_createcharwin)#,command = createcharwin)#, command=Menu_preview_window)

        ##post widget code
        self.This_win.config(menu=Menu_main)##attach menu to window
        self.This_win.after(1500,self.Alt_loop)##alternate event loop for other parts of code(seperate event loop hooked intotkinters primary event loop)
        self.This_win.mainloop()##start window event loop
        
    def Alt_loop(self):##alt event loop code
        ##additional event loop code here
        
        #print(self.get_attackplusspells())
        #print(self.get_secondaryskills())
        ##print(self.get_ALL())
##        self.set_primaryattributes([random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random()])
##        if self.d == '1':
##            self.d = '0'
##      self.set_ALL([['1', '2', '3', '4', '5', '6', '7'], ['1', '2', '3', '4', '5', '6'], ['1', '2', '3', '4', '5', '6'], 'qwerty', 'asdfgh', 'zxcvbn', [(1, 'aa'), (1, 'bb'), (1, 'cc'), (1, 'dd'), (1, 'ee'), (1, 'ff')], [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], ['q', 'w', 'e', 'r', 't', 'y'], ['a', 's', 1, 1, 1, 1, 1, 1], [[['1a', '2a', '3a'], ['1b', '2b', '3b'], ['1c', '2c', '3c']], 'dat text'], 'qwert', 'www', ['o', 'p', 'k', 'l', 'nm']])
##        else:
##            self.d='1'
##            self.set_ALL([['', '', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''], '', '', '', [(0, ''), (0, ''), (0, ''), (0, ''), (0, ''), (0, '')], [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], ['', '', '', '', '', ''], ['', '', 0, 0, 0, 0, 0, 0], [[['', '', ''], ['', '', ''], ['', '', '']], ''], '', '', ['', '', '', '', '']])
        ##end

        ##end
        self.This_win.after(1500,self.Alt_loop)##recalls alt loop method

##check readfile and writefile differences

    def readfile(self,fname):##file io
        try:
            f = open(fname,'r')
            data = f.readlines()
            f.close()
        except:
            try:
                f.close()
            except:
                print('error/file already closed!')
        return data

    def writefile(self,fname,dat,ARRAY = True):##file io
        try:
            f = open(fname,'w')
            if ARRAY == True:
                for x in dat:
                    f.write(str(x)+'\n')
                    print('ln=',x)
            else:
                f.write(dat)
            f.close()
        except:
            try:
                f.close()
            except:
                print('error/file already closed!')
                
    ##INTERNAL methods                               
     ## askfiledialog used here   
    def internal_savefileaskchecker(self):##returns name and true if file exists
        FPath = tk.filedialog.asksaveasfilename(filetypes=(("D&D character sheet", "*.MEGA"),("All Files", "*.*") ))##adv extention is forced onto ##EDIT took out this defaultextension=".ADV", 
        EXISTS_FLAG = False
        if os.path.isfile(FPath):# or os.path.isfile(FPath.strip('.ADV')):##hack to get around
            EXISTS_FLAG = True
        else:
            EXISTS_FLAG = False
        print(os.path.isfile(FPath))
        return[FPath,EXISTS_FLAG]
    
    def internal_loadfileaskchecker(self):##returns name and true if file exists
        FPath = tk.filedialog.askopenfilename(defaultextension=".MEGA", filetypes=(("D&D character sheet", "*.MEGA"),("All Files", "*.*") ))
        EXISTS_FLAG = False
        if os.path.isfile(FPath):# or os.path.isfile(FPath.strip('.ADV')):##hack to get around
            EXISTS_FLAG = True
        else:
            EXISTS_FLAG = False
        print(os.path.isfile(FPath))
        return[FPath,EXISTS_FLAG]
    ####
    
##    def internal_update_Charsheet(self,data):
##        self.set_ALL(data)
    

        
    ##prepares for loading        
    def internal_prepload(self,xdat):
        print('x'+str(xdat))
        Fn = ['charbase',
              'primary',
              'rollmod',
              'perception',
              'inspiration',
              'profbonus',
              'savingthrows',
              'secondary',
              'hpmisc',
              'dicesavemisc',
              'attackspells',
              'attackspells_text',
              'langskills',
              'equipmain',
              'pinfo_base',
              'pinfo_ideals',
              'pinfo_bonds',
              'pinfo_flaws',
              'pinfo_addditfeatures']
        ##de csv etc...
        if xdat[0] == Fn[0]:
            return self.Blib.csv2array(xdat[1][0])
        elif xdat[0] == Fn[1]:
            return self.Blib.csv2array(xdat[1][0])
        elif xdat[0] == Fn[2]:
            return self.Blib.csv2array(xdat[1][0])#removed[]
        
        elif xdat[0] == Fn[3]:
            return self.Blib.csv2array(xdat[1][0])
        elif xdat[0] == Fn[4]:
            return self.Blib.csv2array(xdat[1][0])
        elif xdat[0] == Fn[5]:
            return self.Blib.csv2array(xdat[1][0])
        
        elif xdat[0] == Fn[6]:
            xdat[1] = self.Blib.csv2array(xdat[1][0])
            for x in range(len(xdat[1])):
                xdat[1][x] = [int(xdat[1][x][:1]),xdat[1][x][1:]]##splits into tuples (intcbox,strdat)
            return xdat[1]
        
        elif xdat[0] == Fn[7]:
            xdat[1][1] = self.Blib.csv2array(xdat[1][1])
            for x in range(len(xdat[1][1])):##reconstruct type
                xdat[1][1][x] = int(xdat[1][1][x])
            return [self.Blib.csv2array(xdat[1][0]),xdat[1][1]]
        
        elif xdat[0] == Fn[8]:
            return self.Blib.csv2array(xdat[1][0])
        elif xdat[0] == Fn[9]:
            xdat[1][0] = self.Blib.csv2array(xdat[1][0])
            #print(xdat[1][0])
            for x in range(2,len(xdat[1][0])):
                xdat[1][0][x] = int(xdat[1][0][x])##reconstructing ints
            return xdat[1][0]
        
        elif xdat[0] == Fn[10]:
            for x in range(len(xdat[1])):
                xdat[1][x]= self.Blib.csv2array(xdat[1][x])
            return xdat[1]
        
        elif xdat[0] == Fn[11]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
            
        elif xdat[0] == Fn[12]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
        elif xdat[0] == Fn[13]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
        elif xdat[0] == Fn[14]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
        elif xdat[0] == Fn[15]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
        elif xdat[0] == Fn[16]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
        elif xdat[0] == Fn[17]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
        elif xdat[0] == Fn[18]:
            temp = []
            if len(xdat[1]) == 1:
                return xdat[1]
            else:
                for x in range(len(xdat[1])):
                    temp.append(xdat[1][x]+'\n')
                return temp
            
        
        else:
            print('unused file in loading')#,xdat[0])
    ##additional data manipulation to ensure data is fromatted properly        
    def internal_loadRC(self,xdat):
        temp = []
        temp.append(xdat[0])
        temp.append(xdat[1])
        temp.append(xdat[2])
        temp.append(xdat[3][0])
        temp.append(xdat[4][0])
        temp.append(xdat[5][0])
        temp.append(xdat[6])
        temp.append(xdat[7])
        temp.append(xdat[8])
        temp.append(xdat[9])
        temp.append([xdat[10],xdat[11][0]])
        temp.append(xdat[12])
        temp.append(xdat[13])
        temp.append([xdat[14],xdat[15],xdat[16],xdat[17],xdat[18]])
        return temp
    
    ##button commands
    ##new file button on menubar file
    def sub_button_newfile(self):##Testcharacter1
        Fpath = self.internal_savefileaskchecker()
        #Fpath[0] = self.internal_resolve_ADV(Fpath[0])
        print(Fpath)                                                                                            #list address
        dat = [['New Character', 'New Player', 'None', '0', 'None', 'None', '0XP'],#1                               0
               ['0', '0', '0', '0', '0', '0'],#2                                                                    1
               ['-+0', '-+0', '-+0', '-+0', '-+0', '-+0'],#3                                                        2
               '-+0', '0', '-+0',#4,5,6                                                                             3,4,5
               [(0, '-+0'), (0, '-+0'), (0, '-+0'), (0, '-+0'), (0, '-+0'), (0, '-+0')],#7                          6
               [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],#8a      7[0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],#8b                                         7[1]
               ['0', '-+0', '0', '0', '0', '0'],#9                                                                  8
               ['-+0', '0', 0, 0, 0, 0, 0, 0],#10                                                                   9
               [[['name', 'name', 'name'],#11a                                                                      10[0][0]
                 ['-+0', '-+0', '-+0'],#11b                                                                         10[0][1]
                 ['None', 'None', 'None']],#11c                                                                     10[0][2]
                'enter weapon notes here'],#12 /11[1]                                                               10[1]
               'Enter proficiences and languages here',#13                                                          11
               'enter inventory information here',#14                                                               12
               ['Enter Personality Traits here.',#15                                                                13[0]
                'Enter character ideals here.',#16                                                                  13[1]
                'Enter\ncharacter bonds here.',#17                                                                  13[2]
                'Enter Personality flaws here.',#18                                                                 13[3]
                'enter additional \nfeatures,traits and other\ninformation such as \nbackground traits here.']]#19  13[4]
        
        if tk.messagebox.askokcancel(title = 'confirm save',message = 'save the file: '+str(Fpath[0])+'\nare you sure?'):##could use flag
            if Fpath[1] == True:
                if tk.messagebox.askokcancel(title = 'confirm',message = 'this will OVERWRITE the selected file with data\nare you sure?'):
                    #self.writefile(Fpath,self.Blib.array2csv(self.internal_savefile(dat)),ARRAY = False)##temp
                    #self.writefile(str(Fpath[1]),self.internal_savefile2(dat))
                    dat = Common.internal_prepsave(dat)
                    self.base_ADV = MEGA.mega2(Fpath[0])
                    for x in dat:
                        print(x)
                    for x in range(len(dat)-1):
                        print(dat[x],end='')
                        self.base_ADV.adddata(dat[x])
                        print('Done')
                    self.base_ADV.save()
                        
                else:
                    pass
            else:
                dat = Common.internal_prepsave(dat)
                self.base_ADV = MEGA.mega2(Fpath[0])
                for x in range(len(dat)-1):
                    print(dat[x],end='')
                    self.base_ADV.adddata(dat[x])
                    print('Done')
                self.base_ADV.save()
##                print(self.internal_savefile2(dat))
##                self.writefile(str(Fpath[0]),self.internal_savefile2(dat))
                
        #dat
##    def sub_button_loadfile(self):##load file menubutton
##        FPath = filedialog.askopenfilename(defaultextension=".ADV", filetypes=(("D&D character sheet", "*.ADV"),("All Files", "*.*") ))
##        #dat = self.readfile(FPath)
##        self.QS_path_currfile = FPath##sets var for quicksaving
                
    ## load file button on menubar file
    def sub_button_loadfile(self):##load file menubutton
        FPath = self.internal_loadfileaskchecker()
        print(FPath)
        postprocess_DAT = []
        if tk.messagebox.askokcancel(title = 'load',message = '\nare you sure?'):
            
            if FPath[1] == True:
                self.IS_LOADED = True
                #FPath[0] = self.QS_path_currfile
                self.base_ADV = MEGA.mega2(FPath[0])
                Mfiles = self.base_ADV.peek()
##                print(Mfiles)
##                for x in range(len(Mfiles)):
##                    print(self.base_ADV.fetch(Mfiles[x]))
                for x in Mfiles:
                    print('fetching'+str(self.base_ADV.fetch(x)))
                    postprocess_DAT.append(self.internal_prepload([x,self.base_ADV.fetch(x)]))
                    print(self.internal_prepload([x,self.base_ADV.fetch(x)]))
                print('\n\n\n',postprocess_DAT,'\n\n\n')
                ##final reconstruction
                postprocess_DAT = self.internal_loadRC(postprocess_DAT)
                self.set_ALL(postprocess_DAT)
                self.QS_path_currfile = FPath[0]##sets var for quicksaving
                
            else:
                tk.messagebox.showwarning('error!','no file selected!')
        
        #dat = self.readfile(FPath)
        #self.QS_path_currfile = FPath##sets var for quicksaving

    #save file button on menubar file
    def sub_button_savefile(self):##save file menubutton
        if self.IS_LOADED == True:
            dat = self.get_ALL()
            FPath = self.QS_path_currfile
            dat = Common.internal_prepsave(dat)
            #dat = dat[0]
            self.base_ADV.clear()##edit: method replaces this
            #self.base_ADV.close()
            #self.base_ADV.LOADED = True##hack to open so megafile thinks can be read
            
            #self.base_ADV.save()
            #self.base_ADV = None
            #self.base_ADV = MEGA.mega2(FPath)
            
            #self.base_ADV
##            for x in range(len(dat)):
##                print(dat[x])
##                self.base_ADV.replacedata([dat[x][0],dat[x][1][0]])
            print('dat\n\n',dat)
            for x in dat:
                print(x)
            print('\n\n')
            for x in range(len(dat)-1):
                print('adding',dat[x])
                self.base_ADV.adddata(dat[x])
            self.base_ADV.save()
            print('saved!\n\n====')
            self.base_ADV.dumpall(DATA=True)
            print('====\n\n')
        else:
            #pass
            self.sub_button_savefile_as()#hack for moment
            #self.

    #save file as button on menubar file        
    def sub_button_savefile_as(self):##save as separate file ##later add :if no file is loaded load file as existing
        FP = self.internal_savefileaskchecker()
        print(FP)
        if tk.messagebox.askokcancel(title = 'saveas',message = '\nare you sure?'):
            dat = self.get_ALL()
            dat = Common.internal_prepsave(dat)
            if FP[1] == True:
                if tk.messagebox.askokcancel(title = 'confirm',message = 'this will OVERWRITE the selected file with data\nare you sure?'):
                    self.base_ADV = MEGA.mega2(FP[0])
                    #self.base_ADV.close()##clear file
                    #self.base_ADV.LOADED = True##hack to open so megafile thinks can be read
                    self.base_ADV.clear()##edit: this replaces the close fix
                    for x in dat:
                        print(x)
                    for x in range(len(dat)-1):
                        print(dat[x],end='')
                        #self.base_ADV.replacedata(dat[x])#fix for problem will work out later
                        self.base_ADV.adddata(dat[x])
                        print('Done')
                    self.base_ADV.save()
                else:
                    pass
            else:
                #dat = Common.internal_prepsave(dat)
                self.base_ADV = MEGA.mega2(FP[0])
                for x in dat:
                    print(x)
                for x in range(len(dat)-1):
                    print(dat[x],end='')
                    self.base_ADV.adddata(dat[x])
                    print('Done')
                self.base_ADV.save()
            #self.internal_savefile(FP[0])

    def sub_button_domenu_dicewin(self):
        self.newwindow_DW = tk.Toplevel(self.This_win)
        Class_dicerollerwin.dicewin(self.newwindow_DW,self.datamain)

    def sub_button_domenu_createcharwin(self):
        #pass#command = Class_createcharwin.createcharwin
        self.newwindow_CCW = tk.Toplevel(self.This_win)
        Class_createcharwin.createcharwin(self.newwindow_CCW,self.datamain)

    def sub_button_domenu_optwin(self):
        pass#command = Class_optwin.optwin

    #get functions for returning variables by section(easier than calling individually)   
    ##get
    def get_charbase_name(self):
        return[
            self.charbase_name_CNM_BOX_VAR.get(),
            self.charbase_name_IRL_BOX_VAR.get(),
            self.charbase_name_CLS_BOX_VAR.get(),
            self.charbase_name_LVL_BOX_VAR.get(),
            self.charbase_name_FAC_BOX_VAR.get(),
            self.charbase_name_RAC_BOX_VAR.get(),
            self.charbase_name_EXP_BOX_VAR.get()]
    
    def get_primaryattributes(self):
        return[ self.primaryattributes_STR_BOX_VAR.get(),
                self.primaryattributes_DEX_BOX_VAR.get(),
                self.primaryattributes_CON_BOX_VAR.get(),
                self.primaryattributes_INT_BOX_VAR.get(),
                self.primaryattributes_WIS_BOX_VAR.get(),
                self.primaryattributes_CHR_BOX_VAR.get()]
  
    def get_rollmod(self):
        return[ self.primaryattributes_STR_MOD_BOX_VAR.get(),
                self.primaryattributes_DEX_MOD_BOX_VAR.get(),
                self.primaryattributes_CON_MOD_BOX_VAR.get(),
                self.primaryattributes_INT_MOD_BOX_VAR.get(),
                self.primaryattributes_WIS_MOD_BOX_VAR.get(),
                self.primaryattributes_CHR_MOD_BOX_VAR.get()]

    def get_Perception(self):
        return self.Perception_PER_BOX_VAR.get()
    
    def get_inspiration(self):
        return self.inspiration_STR_BOX_VAR.get()
    
    def get_proficiencybonus(self):
        return self.proficiencybonus_STR_BOX_VAR.get()
    
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
        return[
        self.HPmiscskills_AMC_BOX_VAR.get(),
        self.HPmiscskills_INI_BOX_VAR.get(),
        self.HPmiscskills_SPD_BOX_VAR.get(),
        self.HPmiscskills_HMX_BOX_VAR.get(),
        self.HPmiscskills_HTP_BOX_VAR.get(),
        self.HPmiscskills_HCR_BOX_VAR.get()]

    def get_diceandsavesmisc(self):
        #di
        return[
        self.diceandsavesmisc_HTD_BOX_VAR.get(),
        self.diceandsavesmisc_DTO_BOX_VAR.get(),
        self.diceandsavesmisc_DS1_CHK_VAR.get(),
        self.diceandsavesmisc_DS2_CHK_VAR.get(),
        self.diceandsavesmisc_DS3_CHK_VAR.get(),
        self.diceandsavesmisc_DF1_CHK_VAR.get(),
        self.diceandsavesmisc_DF2_CHK_VAR.get(),
        self.diceandsavesmisc_DF3_CHK_VAR.get()]
    
    def get_attackplusspells_VAR(self):#[weaps/notes][data][weapno]
                                       #weapno
                                       #1=name
                                       #2=attack bonus
                                       #3=damagetype
        return[
        ##name
            [
                self.attackplusspells_WN1_BOX_VAR.get(),
                self.attackplusspells_WN2_BOX_VAR.get(),
                self.attackplusspells_WN3_BOX_VAR.get()
            ],
        ##atk bonus
            [
                self.attackplusspells_AB1_BOX_VAR.get(),
                self.attackplusspells_AB2_BOX_VAR.get(),
                self.attackplusspells_AB3_BOX_VAR.get()
            ],
        ##damage/type
            [
                self.attackplusspells_DT1_BOX_VAR.get(),
                self.attackplusspells_DT2_BOX_VAR.get(),
                self.attackplusspells_DT3_BOX_VAR.get()
            ]]
        #text hack
        #self.attackplusspells_MSC_TXT
    
    def get_attackplusspells_TXT(self):
        #text hack
        return self.attackplusspells_MSC_TXT.get(1.0, 'end-1c')##char1 2 end
    
    def get_attackplusspells(self):
        return [self.get_attackplusspells_VAR(),self.get_attackplusspells_TXT()]
    #text boxes additionally need to be added
    
    def get_languageplusskills(self):
        #traits/lang box
        return self.languagesplusskills_TBX_TXT.get(1.0, 'end-1c')
    
    def get_equipmain(self):
        #equip/inventory
        return self.equipmain_TBX_TXT.get(1.0, 'end-1c')
    
    def get_personalinfo_basic(self):
        #traits
        return[
            self.personalinfo_traits_TBX_TXT.get(1.0, 'end-1c'),
            self.personalinfo_ideals_TBX_TXT.get(1.0, 'end-1c'),
            self.personalinfo_bonds_TBX_TXT.get(1.0, 'end-1c'),
            self.personalinfo_flaws_TBX_TXT.get(1.0, 'end-1c'),
            self.personalinfo_features_TBX_TXT.get(1.0, 'end-1c')]
    
    def get_ALL(self):
        return[
        self.get_charbase_name(),
        self.get_primaryattributes(),
        self.get_rollmod(),
        self.get_Perception(),
        self.get_inspiration(),
        self.get_proficiencybonus(),
        self.get_savingthrows(),
        self.get_secondaryskills(),
        self.get_hpmiscskills(),
        self.get_diceandsavesmisc(),
        self.get_attackplusspells(),
        self.get_languageplusskills(),
        self.get_equipmain(),
        self.get_personalinfo_basic()]
        #add txt boxes


    ##SETTING DATA
    ##set functions for setting by area(easier then individually)
    #base stats
    def set_charbase_name(self,data):
        self.charbase_name_CNM_BOX_VAR.set(data[0])
        self.charbase_name_IRL_BOX_VAR.set(data[1])
        self.charbase_name_CLS_BOX_VAR.set(data[2])
        self.charbase_name_LVL_BOX_VAR.set(data[3])
        self.charbase_name_FAC_BOX_VAR.set(data[4])
        self.charbase_name_RAC_BOX_VAR.set(data[5])
        self.charbase_name_EXP_BOX_VAR.set(data[6])
        
    #primaryattributes
    def set_primaryattributes(self,data):
        self.primaryattributes_STR_BOX_VAR.set(data[0])
        self.primaryattributes_DEX_BOX_VAR.set(data[1])
        self.primaryattributes_CON_BOX_VAR.set(data[2])
        self.primaryattributes_INT_BOX_VAR.set(data[3])
        self.primaryattributes_WIS_BOX_VAR.set(data[4])
        self.primaryattributes_CHR_BOX_VAR.set(data[5])

    #rollmod
    def set_rollmod(self,data):
        self.primaryattributes_STR_MOD_BOX_VAR.set(data[0])
        self.primaryattributes_DEX_MOD_BOX_VAR.set(data[1])
        self.primaryattributes_CON_MOD_BOX_VAR.set(data[2])
        self.primaryattributes_INT_MOD_BOX_VAR.set(data[3])
        self.primaryattributes_WIS_MOD_BOX_VAR.set(data[4])
        self.primaryattributes_CHR_MOD_BOX_VAR.set(data[5])

    #perception
    def set_Perception(self,data):
        self.Perception_PER_BOX_VAR.set(data)

    #inspiration
    def set_inspiration(self,data):
        self.inspiration_STR_BOX_VAR.set(data)

    # proviciency bonus
    def set_proficiencybonus(self,data):
        self.proficiencybonus_STR_BOX_VAR.set(data)

    #saving throws
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

    def set_hpmiscskills(self,data):
        ##hpmiscskills
        self.HPmiscskills_AMC_BOX_VAR.set(data[0])
        self.HPmiscskills_INI_BOX_VAR.set(data[1])
        self.HPmiscskills_SPD_BOX_VAR.set(data[2])
        self.HPmiscskills_HMX_BOX_VAR.set(data[3])
        self.HPmiscskills_HTP_BOX_VAR.set(data[4])
        self.HPmiscskills_HCR_BOX_VAR.set(data[5])


    def set_diceandsavesmisc(self,data):
        #di
        self.diceandsavesmisc_HTD_BOX_VAR.set(data[0])
        self.diceandsavesmisc_DTO_BOX_VAR.set(data[1])
        self.diceandsavesmisc_DS1_CHK_VAR.set(data[2])
        self.diceandsavesmisc_DS2_CHK_VAR.set(data[3])
        self.diceandsavesmisc_DS3_CHK_VAR.set(data[4])
        self.diceandsavesmisc_DF1_CHK_VAR.set(data[5])
        self.diceandsavesmisc_DF2_CHK_VAR.set(data[6])
        self.diceandsavesmisc_DF3_CHK_VAR.set(data[7])
    
    def set_attackplusspells_VAR(self,data):#[weaps/notes][data][weapno]
                                       #weapno
                                       #1=name
                                       #2=attack bonus
                                       #3=damagetype
        ##name
                self.attackplusspells_WN1_BOX_VAR.set(data[0][0])
                self.attackplusspells_WN2_BOX_VAR.set(data[0][1])
                self.attackplusspells_WN3_BOX_VAR.set(data[0][2])
                
        ##atk bonus
                self.attackplusspells_AB1_BOX_VAR.set(data[1][0])
                self.attackplusspells_AB2_BOX_VAR.set(data[1][1])
                self.attackplusspells_AB3_BOX_VAR.set(data[1][2])

        ##damage/type
                self.attackplusspells_DT1_BOX_VAR.set(data[2][0])
                self.attackplusspells_DT2_BOX_VAR.set(data[2][1])
                self.attackplusspells_DT3_BOX_VAR.set(data[2][2])
        #text hack
        #self.attackplusspells_MSC_TXT
                
    def set_attackplusspells_TXT(self,data):
        #text hack
        self.attackplusspells_MSC_TXT.delete(1.0, 'end-1c')
        for x in data:#.insert for loop or pass whole string with newlines
            self.attackplusspells_MSC_TXT.insert(INSERT,x)#.set(data[0])##char1 2 end
            
    def set_attackplusspells(self,data):
        self.set_attackplusspells_VAR(data[0])
        self.set_attackplusspells_TXT(data[1])
    #text boxes additionally need to be added
        
    def set_languageplusskills(self,data):
        #traits/lang box
        self.languagesplusskills_TBX_TXT.delete(1.0, 'end-1c')
        for x in data:
            self.languagesplusskills_TBX_TXT.insert(INSERT,x)
            
    def set_equipmain(self,data):
        #equip/inventory
        self.equipmain_TBX_TXT.delete(1.0, 'end-1c')
        for x in data:
            self.equipmain_TBX_TXT.insert(INSERT,x)
            
    def set_personalinfo_basic(self,data):
        #traits

        self.personalinfo_traits_TBX_TXT.delete(1.0, 'end-1c')
        self.personalinfo_ideals_TBX_TXT.delete(1.0, 'end-1c')
        self.personalinfo_bonds_TBX_TXT.delete(1.0, 'end-1c')
        self.personalinfo_flaws_TBX_TXT.delete(1.0, 'end-1c')
        self.personalinfo_features_TBX_TXT.delete(1.0, 'end-1c')
            
        for x in data[0]:   
            self.personalinfo_traits_TBX_TXT.insert(INSERT,x)
        for x in data[1]:
            self.personalinfo_ideals_TBX_TXT.insert(INSERT,x)
        for x in data[2]:
            self.personalinfo_bonds_TBX_TXT.insert(INSERT,x)
        for x in data[3]:
            self.personalinfo_flaws_TBX_TXT.insert(INSERT,x)
        for x in data[4]:
            self.personalinfo_features_TBX_TXT.insert(INSERT,x)
    
    def set_ALL(self,data):
        self.set_charbase_name(data[0])
        self.set_primaryattributes(data[1])
        self.set_rollmod(data[2])
        self.set_Perception(data[3])
        self.set_inspiration(data[4])
        self.set_proficiencybonus(data[5])
        self.set_savingthrows(data[6])
        self.set_secondaryskills(data[7])
        self.set_hpmiscskills(data[8])
        self.set_diceandsavesmisc(data[9])
        self.set_attackplusspells(data[10])
        self.set_languageplusskills(data[11])
        self.set_equipmain(data[12])
        self.set_personalinfo_basic(data[13])
        #add txt boxes
        