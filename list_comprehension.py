# a list of comprehension
cubes = [i**2 for i in range(10)]
print(cubes)

even = [i**2 for i in range(10) if i**2 % 2 == 0]
print(even)

# Trying to create a list in a very extensive range will result in a MemoryError.
# even = [2*i for i in range(10**100)]

