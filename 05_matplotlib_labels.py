import matplotlib.pyplot as plt
import numpy as np

# create labels for plot

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,300,310,320,330,340])
plt.plot(x, y)
plt.title("google hello")
plt.xlabel("calories")
plt.ylabel("avg oxygen")
plt.show()

# font properties for title and label
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,300,310,320,330,340])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}
plt.plot(x, y)
plt.title("google hello", fontdict=font1)
plt.xlabel("calories", fontdict=font2)
plt.ylabel("avg oxygen", fontdict=font2)
plt.show()


# you can change the side of title and label using command loc
font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}
plt.plot(x, y)
plt.title("google hello", fontdict=font1, loc='left')
plt.xlabel("calories", fontdict=font2)
plt.ylabel("avg oxygen", fontdict=font2)
plt.show()