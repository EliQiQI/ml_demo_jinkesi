import numpy as np


def sign(x):
    return 1 * (x >= 0) - 1 * (x < 0)


print(sign(1))
