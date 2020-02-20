import random
import matplotlib.pyplot as plt
import math
import numpy as np

# single game
def w():
    toss=random.randint(1,2)
    if toss==1: return 1
    if toss==2: return -1


def wn(n=1):
    result=[]
    for i in range(0,n):
        result.append(w())
    return result

#n = input("Enter game number 'n' : ")
#n=int(n)
n=25
N=1000
X25=[]
for i in range (N):
    x25=0
    W = wn(n)
    x0=np.random.normal(5,10)
    for k in range(1,25):
        x25=x25+math.pow(0.5,25-k)*W[k-1]
        #x25=x25+math.pow(0.5,25)*x0 #for (a) leave this commented out
    X25.append(x25)
plt.figure(1)
plt.plot(X25)
plt.title("X25 as a function on iteration")
plt.show()


