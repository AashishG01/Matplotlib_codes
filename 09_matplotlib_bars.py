# now in this section we will create Bars using bar()
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.bar(x,y)
plt.show()

# now we will create a horizontal bar
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.barh(x,y)
plt.show()

# color of the bar() and barh()
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.bar(x,y, color="red")
plt.show()

# we can change the bar width
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.bar(x,y, width=0.5)
plt.show()

# for horizontal bar we will use height instead of width
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.barh(x,y, height=0.3)
plt.show()
