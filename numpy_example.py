import numpy as np  # Import numpy and give it an alias "np" for convenience

# Create numpy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Perform array operations
sum_result = array1 + array2  # Element-wise addition
product_result = array1 * array2  # Element-wise multiplication
mean_result = np.mean(array1)  # Calculate the mean of array1

# Print the results
print("Array 1:", array1)
print("Array 2:", array2)
print("Sum of arrays:", sum_result)
print("Product of arrays:", product_result)
print("Mean of array1:", mean_result)
