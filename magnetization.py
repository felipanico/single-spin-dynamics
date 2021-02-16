import numpy as np
import math
import sys
from matplotlib import pyplot as plt


n = 1000
h = 0.01

def giromagneticRatio():
	#k = 1.76*10**(11)
	#u0 = 1.2566*10**(-6)

	k = 1
	u0 = 1

	return k*u0

def derivate(S,H):
	return -giromagneticRatio()*(np.cross(S,H))

mx = np.zeros([n])
my = np.zeros([n])
mz = np.zeros([n])
dt = np.zeros([n])
m = np.zeros([n])

position = 1.0 / np.sqrt(3.0)

S0 = np.array([position,position,position])  
H = np.array([0,0,1])
S = S0

mx[0] = position
my[0] = position 
mz[0] = position

for t in range(n-1):
	result = derivate(S,H)
	mx[t+1] = mx[t] + h*result[0]
	my[t+1] = my[t] + h*result[1]
	mz[t+1] = mz[t] + h*result[2]
	S = np.array([mx[t+1], my[t+1], mz[t+1]])
	dt[t] = t

plt.plot(mx, label = 'sx')
plt.plot(my, label = 'sy')
plt.plot(mz, label = 'sz')
plt.title('Single Spin')
plt.show()
