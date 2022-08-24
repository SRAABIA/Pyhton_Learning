def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x+5

print (apply_twice(add_five,10))

#pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.
def pure_Function(x,y):
    temp = x+2*y
    return temp/(2*x +y)

# Using pure functions has both advantages and disadvantages.
# Pure functions are:
# - easier to reason about and test.
# - more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
# - easier to run in parallel.

some_list = []

def impure_Function(arg):
    some_list.append(arg)
    #The function above is not pure, because it changed the state of some_list.