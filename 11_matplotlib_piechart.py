import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])


# now we will provide label to pie chart
mylabels = ["apple", "magna", "banana", "cherry"]
plt.pie(y, labels=mylabels)
plt.show()

# startangle parameter = the default start angle is at the x axis but you can change the start angle by specifying
# startangle parameter

plt.pie(y, labels=mylabels, startangle=90)
plt.show()

# explode the pie chart by a value
y = np.array([35, 25, 25, 15])
ylabels = ["apple", "magna", "banana", "cherry"]
myexpode = [0.2, 0, 0, 0]
plt.pie(y, labels=mylabels, explode=myexpode)
plt.show()

# the shadow parameter
y = np.array([35, 25, 25, 15])
ylabels = ["apple", "magna", "banana", "cherry"]
myexpode = [0.2, 0, 0, 0]
plt.pie(y, labels=mylabels, explode=myexpode, shadow=True)
plt.show()

# we can also add the legend - list of explanantion
y = np.array([35, 25, 25, 15])
ylabels = ["apple", "magna", "banana", "cherry"]
myexpode = [0.2, 0, 0, 0]
plt.pie(y, labels=mylabels, explode=myexpode)
plt.legend()
plt.show()