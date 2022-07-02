#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
from scipy.stats import norm 
import matplotlib.pyplot as plt


maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);

randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

rv = norm(0, 1)
plt.plot(x,err,'bo',color="green")
plt.plot(x, rv.cdf(x),color='orange')
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical", "Theory"])
#plt.savefig('../figs/gau_cdf.png')

plt.show()
