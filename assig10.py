import numpy as np

# Create 1D array from 1 to 10
arr = np.array([1,2,3,4,5,6,7,8,9,10])

print("Original array:", arr)

# Slicing
print("Elements from index 1 to 5:", arr[1:5])
print("Elements from index 1 to 4:", arr[1:4])
print("Alternate elements:", arr[::2])

# Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
arr = arr + 5
print("Array after broadcasting:", arr)