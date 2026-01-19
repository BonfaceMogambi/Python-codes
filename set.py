thisset = {"apple", "banana", "cherry"} # Create a set --- note that sets are unordered collections of unique items
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"} # Duplicates are ignored in sets
print(thisset) # Output will be {'banana', 'cherry', 'apple'} --- order may vary

thisset = {"apple", "banana", "cherry", True, 1, 2} # True is treated as 1, so it is counted as a duplicate
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0} # False is treated as 0, so it is counted as a duplicate
print(thisset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #making a set from a tuple

thisset = {"apple", "banana", "cherry"}
for x in thisset: # loop through set and print values
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # check if an item exists in the set

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) # check if an item does not exist in the set


thisset = {"apple", "banana", "cherry"}
thisset.add("orange") # add an item to the set
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # add tropical items to thisset
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") # deletes banana
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() # Remove a random item
print(x)
print(thisset)

