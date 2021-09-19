import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
color = np.arctan2(Y,X)
plt.scatter(X,Y,c=color,alpha=0.5,s=80)
plt.ylim(-1,1)
plt.xlim(-1,1)
plt.xticks([])
plt.yticks([])

