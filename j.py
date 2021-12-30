import numpy as np
import random

X_scaled = np.load("data_x_alpha2.npy")
y = [random.randrange(6) for i in range(640)]
# y = np.array(y)
# y = np.reshape(640,-1)
# print(y)
print(y)