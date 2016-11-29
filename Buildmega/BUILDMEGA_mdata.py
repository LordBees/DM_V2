import MEGA,os
def array2csv(array):##from beelib
        temp = ''
        for fl in array:
            #print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
def csv2array(csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
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

def readfile(fname):
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
    
os.chdir('Main_data')
m = MEGA.mega2('DATA.MEGA')
ford = readfile('MEGAORDER.txt')
##for y in range(len(ford)):
##    ford[y] = ford[y].strip('\n')
ford = ford[0].strip('\n')
print(ford)
ford = csv2array(ford)

for x in range(len(ford)):
    dat = readfile(ford[x])
    for y in range(len(dat)):
        dat[y] = dat[y].strip('\n')
    m.adddata([ford[x],dat])
m.save()

print('parsetest')
if input('press y').upper() == 'Y':
    for x in m.peek():
        print('\n\nfile|'+str(x))
        print(m.fetch(x))

print('reloadtest')
if input('press y').upper() == 'Y':
        m = None
        m = MEGA.mega2('DATA.MEGA')
        for x in m.peek():
                print('\n\nfile|'+str(x))
                print(m.fetch(x))

input('Press Enter To COntinue...')
        

