import numpy as np
import math


def error_0(a):
   x = np.loadtxt("ber.dat",dtype = "double")

   n = np.loadtxt("gau.dat",dtype = "double")
   y = a*x + n
   x_0 = np.count_nonzero(x>0)
   y_0 = np.count_nonzero((y<0) & (x>0))
   
   return y_0/x_0

def error_1(a):
   x = np.loadtxt("ber.dat",dtype = "double")

   n = np.loadtxt("gau.dat",dtype = "double")
   y = a*x + n
   x_1 = np.count_nonzero(x<0)
   y_1 = np.count_nonzero((y>0) & (x<0))
   
   return y_1/x_1  
     

  
 
def Q(x):
	return (math.erfc(x/math.sqrt(2)))/2.0

A = 5

print("p_{e|0}",1-Q(-A))
print("p_{e|1}",Q(A))

print("p_{e|0}_num:",error_0(A))
print("p_{e|1}_num:",error_1(A))
