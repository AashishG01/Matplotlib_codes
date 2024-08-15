import matplotlib.pyplot as plt
import numpy as np

# you can use marker to emphasize each point with specified marker

# yp = np.array([3,8,1,10])
# plt.plot(yp, marker = '+')
# plt.show()

# format string "fmt" - marker|line|color
yp = np.array([3,8,1,10])
plt.plot(yp, 'o:r')
plt.show()

# line refrence
# - solid line
# : dotted line
# -- dashed line
# -, dashline/dotted line

# color refernce
# r red
# g green
# b blue
# c cyan
# m magenta
# y yellow
# k black
# w white

# marker size - ms
yp = np.array([3,8,1,10])
plt.plot(yp, marker = 'o', ms=20)
plt.show()

# marker edge color - mec
yp = np.array([3,8,1,10])
plt.plot(yp, marker = 'o', ms=20, mec='r')
plt.show()

# marker face color - mfc
yp = np.array([3,8,1,10])
plt.plot(yp, marker = 'o', ms=20, mec='y', mfc='r' )
plt.show()


