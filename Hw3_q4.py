import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('TkAgg')

lambda_exp=0.1
L=5
N=500

#Q4.2
M=1000 #10000,1000000
avg=[]
for m in range (0,M):
    W = np.zeros(N - L)
    X = np.zeros(N, float)
    for i in range(1, N):
        U = np.random.uniform(0, 1)
        X[i] = -1 * (1 / lambda_exp) * np.log(U)
    for i in range(0, N - L - 1):
        W[i] = X[i + 1]
        for l in range(2, L):
            W[i] = min(W[i], X[i + l])
    avg.append(np.sqrt(N/L)*((L/N)*np.sum(W[1:int(N/L)])-np.average(W[1])))

#matplotlib.use('TkAgg')
plt.plot(W)
plt.title("Wi=min{Xi+1,...,Xi+L}")
plt.xlabel("i")
plt.ylabel("Wi")

plt.hist(avg,density=True)
plt.title("Histogram")
plt.xlabel("m")
plt.ylabel("Average")