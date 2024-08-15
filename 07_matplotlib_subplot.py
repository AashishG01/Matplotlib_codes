# display the multiple plots - with subplot() you can draw multiple plots in one figure
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,300,310,320,330,340])
plt.subplot(1, 2, 1)
# the figure has 1 row, 2 columns, and this is plot no 1
plt.plot(x, y)

x=np.array([4,5,7,3])
y=np.array([7,1,9,4])
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.show()
