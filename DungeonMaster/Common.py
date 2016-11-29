##functions that are shared throughout windows that dont fit into beelib are put here

##mega file save prep
##Common.internal_prepsave
def internal_prepsave(self,GotData):##handles conversion for data to save in megafile
    ##doublecheck this vs
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
    print(len(Fn))
    print(Fn,'\n')
    dat2rt = ['']*20
    temp = []
        
    ##1
    print(GotData[0])
    for x in range(len(GotData[0])):
        GotData[0][x] = GotData[0][x].strip('\n')
        if GotData[0][x] == '':##add spaces for csvising 
            GotData[0][x] = ' '
    dat2rt[0] = [Fn[0],[self.array2csv(GotData[0])]]
    print(dat2rt[0])
        
    ##2
    print(GotData[1])
    for x in range(len(GotData[1])):
        print(GotData[1][x])
        if GotData[1][x] == '':
            GotData[1][x] = ' '
    dat2rt[1] = [Fn[1],[self.array2csv(GotData[1])]]
    print(dat2rt[1])
        
    #3
    print(GotData[2])
    for x in range(len(GotData[2])):
        if GotData[2][x] == '':
            GotData[2][x] = ' ' 
    dat2rt[2] = [Fn[2],[self.array2csv(GotData[2])]]
        
##        #4,5,6
##        #temp = [GotData[3],GotData[5],GotData[6]]
##        dat2rt[3] = [Fn[3],[self.array2csv(temp)]]
##        temp = []

    #4
    print(GotData[3])
    if GotData[3] == '':
        GotData[3] = ' '
    dat2rt[3] = [Fn[3],[self.array2csv([GotData[3]])]]

    #5
    if GotData[4] == '':
        GotData[4] = ' '
    dat2rt[4] = [Fn[4],[self.array2csv([GotData[4]])]]

    #6
    if GotData[5] == '':
        GotData[5] = ' '
    dat2rt[5] = [Fn[5],[self.array2csv([GotData[5]])]]
        
    #7
    for x in range(len(GotData[6])):#checkbox value is always 1 or 0 so can just apppend as string
        if GotData[6][1] == '':
            GotData[6][1] = ' '
        temp.append(str(GotData[6][x][0])+str(GotData[6][x][1]))
    dat2rt[6] = [Fn[6],[self.array2csv(temp)]]
    temp = []
        
    #8 a,b
    for x in range(len(GotData[7][1])):##convert 8b to str from int
        if GotData[7][0][x] == '':##put here because checkbox list is the same size
            GotData[7][0][x] = ' '
        GotData[7][1][x] = str(GotData[7][1][x])
    dat2rt[7] = [Fn[7],[self.array2csv(GotData[7][0]),self.array2csv(GotData[7][1])]]
        
    #9
    for x in range(len(GotData[8])):##could function this
        if GotData[8][x] == '':
            GotData[8][x] = ' ' 
    dat2rt[8] = [Fn[8],[self.array2csv(GotData[8])]]
        
    #10
    for x in range(len(GotData[9])):
        GotData[9][x] = str(GotData[9][x])
        if GotData[9][x] == '':
            GotData[9][x] = ' ' 
    dat2rt[9] = [Fn[9],[self.array2csv(GotData[9])]]
        
    #11
    print(GotData[10])
    for x in range(len(GotData[10][0])):#always same entries length for block
        if GotData[10][0][0][x] == '':
            GotData[10][0][0][x] = ' '
                
        if GotData[10][0][1][x] == '':
            GotData[10][0][1][x] = ' '
                
        if GotData[10][0][2][x] == '':
            GotData[10][0][2][x] = ' '
    dat2rt[10] = [Fn[10], [self.array2csv(GotData[10][0][0]),self.array2csv(GotData[10][0][1]),self.array2csv(GotData[10][0][2])] ]
        
    #12
##              for x in range(len(GotData[7][2])-1):
##                  if GotData[7][2][x] == '\\'
        
    if GotData[10][1] == '':
            GotData[10][1] = ' '
    dat2rt[11] = [Fn[11],GotData[10][1].split('\n')]
        
    #13
    if GotData[11] == '':
            GotData[11] = ' '
    dat2rt[12] = [Fn[12],GotData[11].split('\n')]
        
    #14
    if GotData[12] == '':
            GotData[12] = ' '
    dat2rt[13] = [Fn[13],GotData[12].split('\n')]
        
    #15
    for x in range(len(GotData[13])):##does all 5 below as in a list together
        if GotData[13][x] == '':
            GotData[13][x] = ' '
    dat2rt[14] = [Fn[14],GotData[13][0].split('\n')]
        
    #16
    print('\n\n')
    print(Fn[16],'\n')
    print(GotData[13][1].split('\n'))
    dat2rt[15] = [Fn[15],GotData[13][1].split('\n')]
        
    #17
    dat2rt[16] = [Fn[16],GotData[13][2].split('\n')]
        
    #18
    dat2rt[17] = [Fn[17],GotData[13][3].split('\n')]

    #19
    dat2rt[18] = [Fn[18],GotData[13][4].split('\n')]
        
    return dat2rt#GotData#dat2rt