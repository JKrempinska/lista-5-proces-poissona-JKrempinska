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

for i in range(10):
    x = poissons(5,1)
    y = np.arange(0, len(x))
    plt.step(x,y)

plt.show()
