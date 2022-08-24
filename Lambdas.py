def my_function(func, arg):
    return func(arg)

print(my_function(lambda x: 2*x*x,5))

# Creating a function on the fly, without assigning it to some variable is done using Lambda suntax.
# Function created this way are called Anonymous.

#named function
def polynomial(x):
    return x**2+5*x+4
print(polynomial(-4))

#lambda
print((lambda x: x**2+5*x+4)(-4))

# What is the result of this code?
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))
