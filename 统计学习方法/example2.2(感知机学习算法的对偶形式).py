import numpy as np

dataset = np.array([[3, 3], [4, 3], [1, 1]])
result = np.array([1, 1, -1])
# 计算Gram matrix
gram = dataset.dot(dataset.T)
alpha = np.array([0, 0, 0])
w = np.array([0, 0])
b = 0
eta = 1
flag = [True, True, True]

while any(flag):
    for i in range(3):
        temp_sum = 0
        for j in range(3):
            temp_sum += alpha[j] * result[j] * gram[j, i]

        temp_sum += b
        if result[i] * temp_sum <= 0:
            alpha[i] = alpha[i] + eta
            b = b + eta * result[i]
            print(alpha, b)
        else:
            flag[i] = False
for i in range(3):
    w += alpha[i] * result[i] * dataset[i]

print(w, b)
