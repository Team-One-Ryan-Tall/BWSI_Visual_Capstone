import numpy as np
from CosineDists import cosine_distances
test1 = np.array([[3, 2, 1, 5]])
test2 = np.array([30, 20, -1, 5])
print(cosine_distances(test1, test2))