from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

N=200
g=np.zeros((N,N))
y=np.linspace(-10,10,num=200)
for i in range(1, N):
    g[i] = (norm.cdf(y[i]-1)-2*norm.cdf(y[i])+norm.cdf(y[i]+1))/((norm.cdf(y[i]-1))-norm.cdf(y[i]+1))

plt.figure(6)
plt.plot(y,g)
plt.show()
