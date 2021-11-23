import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])

plt.plot(dataset[:,0],dataset[:,1],'o')
# for i in range(6):
#     plt.plot(dataset[i][0], dataset[i][1])
plt.plot(3,4.5,'o')
plt.show()
