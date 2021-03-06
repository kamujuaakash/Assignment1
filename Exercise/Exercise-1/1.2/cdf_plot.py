

#Importing numpy, scipy, mpmath and pyplot

import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex

import scipy
#end if
def cdf(x):
    if x<0.0:
        return 0.0
    elif x>1.0:
        return 1.0		
    else :
        return x	   


x = np.linspace(-4,4,100)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
err1 = []
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,100):
    err_ind = np.nonzero(randvar < x[i]) #checking probability condition
    err_n = np.size(err_ind) #computing the probability
    err.append(err_n/simlen) #storing the probability values in a list

uni_cdf = scipy.vectorize(cdf)
    
plt.plot(x.T,err,"o")#plotting the CDF
plt.plot(x.T,uni_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theoretical"])
#if using termux
plt.savefig('figs/uni_cdf.png')
# plt.savefig('./figs/uni_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
