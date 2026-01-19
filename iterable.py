# iterable string example
# This code demonstrates how to create an iterator from a string and iterate through it.
myFruit = "mango"
myM = iter(myFruit)

print (next(myM))  # Output: m
print (next(myM))  # Output: a
print (next(myM))  # Output: n
print (next(myM))  # Output: g
print (next(myM))  # Output: o
