import numpy as np
file = open('uni.dat','r')
nwfile = open('v.dat','w')
data = file.readlines()
list = []
for i in data:
    list.append(float(i))
dt = np.array(list)
def fun(dt):
    v = -2*(np.log(1-dt))
    return v
v = fun(dt)
for i in v:
    nwfile.write(str(i))
    
file.close()
nwfile.close()
