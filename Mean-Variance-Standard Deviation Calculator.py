import numpy as np

# Get input from the user
input_list = input("Enter 9 numbers separated by spaces: ").split()

# Convert input strings to integers
input_list = [int(x) for x in input_list]

# Check if the list has exactly 9 elements
if len(input_list) != 9:
    raise ValueError("List must contain nine numbers.")

# Convert the list into a 3x3 Numpy array
array = np.array(input_list).reshape(3, 3)

# Calculate statistics
calculations = {
    'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean().tolist()],
    'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var().tolist()],
    'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std().tolist()],
    'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max().tolist()],
    'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min().tolist()],
    'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum().tolist()]
}

# Print the result
print(calculations)
