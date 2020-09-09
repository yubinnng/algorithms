import numpy as np

a = [1, 1, 1, 1, 1, 0, 0, 0]

b = [1, 1, 1, 1, 1]

c = np.array([
    [1, 2],
    [3, 4]
])
print(c.shape)
print(c.T)


import uuid
print(str(uuid.uuid1()).replace('-', ''))
# print(uuid.uuid3())
# print(uuid.uuid4())
# print(uuid.uuid5())

