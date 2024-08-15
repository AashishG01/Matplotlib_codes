# linestyle or ls - is used to change the style of the plotted line
import matplotlib.pyplot as plt
import numpy as np

yp = np.array([3,8,1,10])
plt.plot(yp, linestyle = 'dashed')
plt.show()

# linestyle or ls anyone can we write both works

# line color - c
yp = np.array([3,8,1,10])
plt.plot(yp, color='r')
plt.show()

# line width or lw --- width of line
yp = np.array([3,8,1,10])
plt.plot(yp, linewidth = '20.5')
plt.show()

# example for multiple lines
xp = np.array([8,2,7,3])
yp = np.array([7,5,6,9])
plt.plot(xp)
plt.plot(yp)
plt.show()


