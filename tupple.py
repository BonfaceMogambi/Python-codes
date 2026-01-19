mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #type of mytuple is <class 'tuple'>
# Accessing tuple items

thistuple = tuple(("jerry", "mango", "orange")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", 34 , "cherry", "apple", "cherry") # tuple with duplicate values
print(thistuple)

thistuple = ("apple",) # tuple with one item --- remember the comma
print(type(thistuple))

print(len(thistuple)) # length of tuple


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") # check if an item exists in the tuple


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits # unpacking a tuple --- the first two items are assigned to green and yellow, and the rest are assigned to red. Note that the asterisk (*) is used to collect the remaining items into a list.

print(green)
print(yellow)
print(red)