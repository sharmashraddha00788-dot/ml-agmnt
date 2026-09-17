# # NumPy Implementation Notebook
# 
# Three simple implementations/demonstrations for each required NumPy function.

import numpy as np


# ## 1. Array Creation & Reshaping

# np.array() - Implementation 1
a1 = np.array([1, 2, 3, 4])
print(a1)

# np.array() - Implementation 2
a2 = np.array([[1, 2], [3, 4]])
print(a2)

# np.array() - Implementation 3
a3 = np.array((5, 6, 7))
print(a3)


# np.zeros() - Implementation 1
print(np.zeros(5))

# Implementation 2
print(np.zeros((2, 3)))

# Implementation 3
print(np.zeros((2, 2), dtype=int))


# np.ones() - Implementation 1
print(np.ones(4))

# Implementation 2
print(np.ones((2, 3)))

# Implementation 3
print(np.ones((2, 2), dtype=int))


# np.arange() - Implementation 1
print(np.arange(5))

# Implementation 2
print(np.arange(2, 10, 2))

# Implementation 3
print(np.arange(10, 0, -2))


# np.linspace() - Implementation 1
print(np.linspace(0, 10, 5))

# Implementation 2
print(np.linspace(1, 2, 4))

# Implementation 3
print(np.linspace(-1, 1, 5))


# np.reshape() - Implementation 1
a = np.arange(6)
print(a.reshape(2, 3))

# Implementation 2
b = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(b.reshape(4, 2))

# Implementation 3
c = np.arange(12)
print(np.reshape(c, (3, 4)))


# ## 2. Array Manipulation & Math

# np.concatenate() - Implementation 1
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate((a, b)))

# Implementation 2
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))

# Implementation 3
p = np.array([[1], [2]])
q = np.array([[3], [4]])
print(np.concatenate((p, q), axis=1))


# np.transpose() - Implementation 1
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.transpose(a))

# Implementation 2
print(a.T)

# Implementation 3
b = np.array([[7, 8], [9, 10]])
print(np.transpose(b))


# np.sum() - Implementation 1
a = np.array([1, 2, 3, 4])
print(np.sum(a))

# Implementation 2
b = np.array([[1, 2], [3, 4]])
print(np.sum(b, axis=0))

# Implementation 3
print(np.sum(b, axis=1))


# np.mean() - Implementation 1
a = np.array([10, 20, 30])
print(np.mean(a))

# Implementation 2
b = np.array([[1, 2], [3, 4]])
print(np.mean(b))

# Implementation 3
print(np.mean(b, axis=0))


# np.where() - Implementation 1
a = np.array([1, 5, 8, 2])
print(np.where(a > 4))

# Implementation 2
print(np.where(a % 2 == 0, "Even", "Odd"))

# Implementation 3
b = np.array([10, 20, 30])
print(np.where(b > 15, b, 0))


# np.argmax() - Implementation 1
a = np.array([4, 9, 2, 7])
print(np.argmax(a))

# Implementation 2
b = np.array([[1, 8], [6, 3]])
print(np.argmax(b))

# Implementation 3
print(np.argmax(b, axis=0))


# np.argmax() - Implementation 3 with a row-wise check
c = np.array([[5, 2, 9], [7, 8, 1]])
print(np.argmax(c, axis=1))


# ## Quick Practice

numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)
print("Matrix:")
print(matrix)
print("Total:", np.sum(matrix))
print("Average:", np.mean(matrix))
print("Largest value index:", np.argmax(matrix))

