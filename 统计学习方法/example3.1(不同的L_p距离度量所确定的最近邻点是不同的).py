# 已知二维空间的3个点x_1 = (1,1)^T,x_2 = (5,1)^T,x_3=(4,4)^T,试求在p取不同值时,L_p距离下x_1的最近邻点

import numpy as np
import matplotlib.pyplot as plt


def get_distance(x, p):
    return (np.sqrt((x[0] - 1) ** 2) ** p + np.sqrt((x[1] - 1) ** 2) ** p) ** (1 / p)


num = np.arange(1, 10)
x2_distance = np.zeros(9)
x3_distance = np.zeros(9)
x2 = np.array([5, 1])
x3 = np.array([4, 4])
for i in num:
    x2_distance[i - 1] = get_distance(x2, i)
    x3_distance[i - 1] = get_distance(x3, i)

plt.plot(num, x2_distance)
plt.plot(num, x3_distance)
print(x2_distance, x3_distance)
plt.show()
