import numpy as np
import matplotlib.pyplot as plt

def poissons(T, lamb):
    S = []
    t = 0
    while t < T:
        u = np.random.uniform()
        t = t - (1/lamb)*np.log(u)
        if t < T:
            S.append(t)
    return S


for i in range(20):
    x = poissons(100,1)
    y = np.arange(0, len(x))
    plt.step(x,y)
plt.show()


def nt_value(t, lamb):
    return lamb * t

ts = np.zeros(1000)
for i in range(1000):
    p = poissons(100,1)
    ts[i] = p[3]

plt.boxplot(ts)
r, l = plt.xlim()
plt.hlines(nt_value(3,1),xmin=r, xmax=l)
#plt.hist(ts, bins=20)
plt.show()



