import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,500)
F1=1000
F2=100
Fs=10000
s1=0.5*np.cos(2*np.pi*F1/Fs*n+np.pi/2)
s2=1.5*np.cos(2*np.pi*F1/Fs*n+np.pi/2)
s3=s1+s2
plt.subplot(311)
plt.plot(n,s3)
x=np.cos(2*np.pi*F1/Fs*n+np.pi/2)
y=np.cos(2*np.pi*F2/Fs*n+np.pi/2)
s4=x+y
plt.subplot(312)
plt.plot(n,s4)
a=np.cos(2*np.pi*F1/Fs*n+np.pi/2)
b=np.cos(2*np.pi*F1/Fs*n+np.pi/4)
s5=a+b
plt.subplot(313)
plt.plot(n,s5)
plt.show()

