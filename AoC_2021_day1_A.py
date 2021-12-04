import numpy as np
arr1 = np.loadtxt("day1_input.txt", dtype=int)
result = np.diff(arr1)
k = 0
count = len([i for i in result if i > k])
print(count)




