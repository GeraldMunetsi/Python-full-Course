#arrays and Numpy
#Multidimensional arra
import numpy as np

# Create a 1-dimensional array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a 2-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Perform mathematical operations on arrays
result = np.sin(arr1) + np.sqrt(arr2)

print(result)

#linspace creates equaly spaced valuea over a range
import numpy as np


###using the np.zeros(shape)
import numpy as np
# Create a 1D array filled with zeros
zeros_arr = np.zeros(5)
print(zeros_arr)
# Output: [0. 0. 0. 0. 0.]

# Create a 2D array filled with zeros
zeros_matrix = np.zeros((3, 4))
print(zeros_matrix)
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]

###np.ones(shape)
import numpy as np

# Create a 1D array filled with ones
ones_arr = np.ones(5)
print(ones_arr)
# Output: [1. 1. 1. 1. 1.]

# Create a 2D array filled with ones
ones_matrix = np.ones((2, 3))
print(ones_matrix)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]
