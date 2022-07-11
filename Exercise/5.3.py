import matplotlib.pyplot as plt
import numpy as np
import pandas

a = int(1e6)
x = np.linspace(0, 1, a)
pf2=open("5.dat","r")
pf2=pf2.readlines()
y=[]
for i in pf2[0:1000000]:
        y.append(float(i))

plt.scatter(x,y, c ="blue")
 
# To show the plot
plt.show()
