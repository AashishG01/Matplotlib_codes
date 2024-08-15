import matplotlib.pyplot as plt
import numpy as np
# adding grid lines to plot via "grid()"
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,300,310,320,330,340])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}
plt.plot(x, y)
plt.title("google hello", fontdict=font1)
plt.xlabel("calories", fontdict=font2)
plt.ylabel("avg oxygen", fontdict=font2)
plt.grid()
plt.show()

# now we will define which grid lines to display via x axis and y axis. leagal values are x and y and both default value is both
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,300,310,320,330,340])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}
plt.plot(x, y)
plt.title("google hello", fontdict=font1)
plt.xlabel("calories", fontdict=font2)
plt.ylabel("avg oxygen", fontdict=font2)
plt.grid(axis='x')
plt.show()

# setting of gridlines properties
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,300,310,320,330,340])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}
plt.plot(x, y)
plt.title("google hello", fontdict=font1)
plt.xlabel("calories", fontdict=font2)
plt.ylabel("avg oxygen", fontdict=font2)
plt.grid(color='green', linestyle='dashed')
plt.show()

