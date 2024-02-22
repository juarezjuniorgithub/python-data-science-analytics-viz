import numpy as np

# Define a 2D array
my_2d_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]],
                       dtype=np.int64)

# Define a 3D array
my_3d_array = np.array([[[1, 2, 3, 4],
                         [5, 6, 7, 8]],
                        [[1, 2, 3, 4],
                         [9, 10, 11, 12]]],
                       dtype=np.int64)

# Print the 2D array
print("Printing my_2d_array:")
print(my_2d_array)

# Print the 3D array
print("Printing my_3d_array:")
print(my_3d_array)
