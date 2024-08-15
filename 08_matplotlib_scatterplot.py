# scatter - the scatter() function plots one dot for each observation.
import matplotlib.pyplot as plt
import numpy as np

x = np.array([23, 87, 45, 62, 14, 76, 91, 33, 58, 49])
y = np.array([7, 82, 29, 65, 41, 96, 53, 19, 71, 88])
plt.scatter(x,y)
plt.show()

# now we will compare 2 plots on same figure
x = np.array([23, 87, 45, 62, 14, 76, 91, 33, 58, 49])
y = np.array([7, 82, 29, 65, 41, 96, 53, 19, 71, 88])
plt.scatter(x,y)

x = np.array([47, 33, 68, 21, 84, 59, 10, 97, 42, 76, 63, 5, 87, 49, 38])
y = np.array([29, 94, 15, 82, 31, 61, 18, 85, 12, 70, 99, 24, 56, 9, 48])
plt.scatter(x,y)
plt.show()
# you can apply all the properties of marker

# to color each point different
x = np.array([23, 87, 45, 62, 14, 76, 91, 33, 58, 49])
y = np.array([7, 82, 29, 65, 41, 96, 53, 19, 71, 88])
colors = (["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "Cyan"])

plt.scatter(x,y, c=colors)
plt.show()

# now we will create a color array and specify a colormapin scatter plot
x = np.array([23, 87, 45, 62, 14, 76, 91, 33, 58, 49])
y = np.array([7, 82, 29, 65, 41, 96, 53, 19, 71, 88])
# colors = (["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "Cyan"])
colors = np.array([12, 55, 74, 28, 91, 47, 33, 68, 21, 84])
plt.scatter(x,y, c=colors, cmap='viridis')
#to include colorbar in the plot
plt.colorbar()
plt.show()

# to change size
x = np.array([23, 87, 45, 62, 14, 76, 91, 33, 58, 49])
y = np.array([7, 82, 29, 65, 41, 96, 53, 19, 71, 88])
sizes = np.array([59, 10, 97, 42, 76, 63, 5, 87, 49, 38])
plt.scatter(x,y, s = sizes)
plt.show()

# using command "alpha " you can control the transperancy of dots in plot  and alpha lies between 0 to 1

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10*np.random.randint(100, size=(100))
plt.scatter(x,y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()

