import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([
    [3, 4, 1],
    [3, 3, 1]
])
result = np.array([1, 1, -1])
print(result)
w = np.array([[0], [0]])
b = 0
eta = 1
# 退出循环
flag = np.array([True, True, True])

plt.plot(dataset[0], dataset[1], 'o', color='b')

while any(flag):
    for i in range(3):
        x = np.array([dataset[:, i]]).T
        y = result[i]
        if y * (w.T.dot(x) + b) <= 0:
            w = w + eta * y * x
            b = b + eta * y
            print("迭代中w:", w, "迭代中b:", b)
        else:
            flag[i] = False
print("结果w:", w, "结果b:", b)

draw_pointx = np.linspace(0, 5, 100)
draw_pointy = np.zeros(100)
for i in range(100):
    draw_pointy[i] = (-b - w[0] * draw_pointx[i]) / w[1]

plt.plot(draw_pointx, draw_pointy)
plt.show()
