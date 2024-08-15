import matplotlib.pyplot as plt
# now the pyplot package can be reffered as plt

import numpy as np

# plotting x and y
# plot() function is used to draw points or markers in a diagram

# there are two parameters for specifiying points in a diagram x-axis and y-axis
xpoints = np.array([1,8])
ypoints = np.array([3,10])
# plt.plot(x axis, y axis)
plt.plot(xpoints, ypoints)
plt.show()

# the x-axis is horizontal
# the y-axis is vertical

# ploting without line
plt.plot(xpoints, ypoints, 'o')
plt.show()

xp = np.array([1,2,6,8])
yp = np.array([3,8,1,10])
plt.plot(xp, yp)
plt.show()

# defautl x points
# if we do not specify the points in x axis then the default values are 0,1,2,3 .. will apply

yp1 = np.array([3,8,1,10,5,7])
plt.plot(yp1)
plt.show()



