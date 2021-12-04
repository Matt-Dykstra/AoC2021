import numpy as np

arr1 = np.loadtxt("day1_input.txt", dtype=int)

#found tips on np.convolve at https://stackoverflow.com/questions/38507672/summing-elements-in-a-sliding-window-numpy
#could also do this using sliding_window_view
arr2 = np.convolve(arr1, np.ones(3, dtype=int), 'valid')

result = result = np.diff(arr2)

k = 0
count = len([i for i in result if i > k])
print(count)



