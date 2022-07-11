import numpy as np
import mpmath as mp
from matplotlib import pyplot as plt
import scipy

b = np.loadtxt('ber.dat', dtype='double')
g = np.loadtxt('gau.dat', dtype='double')

def prac(a):
    y = a*b + g
    n0 = np.count_nonzero(b > 0)
    n1 = np.count_nonzero(b < 0)
    e0 = np.count_nonzero((y < 0) & (b > 0)) 
    e1 = np.count_nonzero((y > 0) & (b < 0))
    return 0.5*(e0/n0 + e1/n1)

err_vec = scipy.vectorize(prac, otypes=['double'])

def Q(x):
    return (0.5)*mp.erfc(x/np.sqrt(2))

q_vec = scipy.vectorize(Q, otypes=['double'])

A = np.linspace(0, 10, 100)
plt.plot(A, err_vec(A), '.')
plt.plot(A, q_vec(A))
plt.grid()
plt.xlabel('$A$ (dB)')
plt.ylabel('$P_e(A)$')
plt.show()
