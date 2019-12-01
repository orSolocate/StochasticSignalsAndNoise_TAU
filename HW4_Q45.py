import matplotlib.pyplot as plt
import numpy as np

N=1000
X=np.zeros((N,N),float)
for i in range(1, N):
    X[0] = np.random.uniform(-0.5*np.pi,0.5*np.pi,N)
    X[1][i] = np.sin(X[0][i])

plt.figure(1)
plt.scatter(X[0],X[1])
plt.show()

for i in range(1, N):
    X[0] = np.random.uniform(-1,1,N)
    X[1] = np.random.uniform(-0.2, 0.2, N)
plt.figure(2)
plt.scatter(X[0],X[1])
plt.show()

M=7
teta=np.zeros(M,float)
for k in range(0,M):
    teta[k]=(k*np.pi)/12
print teta

R=np.zeros((M,2,2,N),float)
W=np.zeros((M,2,N),float)
ro=[]
plt.figure(3)
for i in range(0,M):
    for j in range(0,N):
        R[i,:,:,j]=np.array([[np.cos(teta[i]),-1*np.sin(teta[i])],[np.sin(teta[i]),np.cos(teta[i])]])
        W[i,:,j] = R[i,:,:,j].dot([X[0,j],X[1,j]])
    cov = np.cov(W[i,0],W[i,1])
    ro_temp=cov[0][1]/np.sqrt(cov[0][0]*cov[1][1])
    ro.append(ro_temp)
    plt.ion()
    plt.scatter(W[i,0],W[i,1])
    plt.show()

print ("teta maximum ro: {0}\n teta minimum ro: {1}".format(teta[ro.index(max(ro))],teta[ro.index(min(ro))]))



