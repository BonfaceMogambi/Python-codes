thislist = ["Apple", 34, "Banana", "Cherry"]
members = ["Bonface", "Mango", "John", "Doe"]

thislist.append("Bonface")# Appends "Bonface" to the end of thislist
thislist.insert(1, "Mango")# Inserts "Mango" at index 1 of thislist
print (len(thislist))# Prints the length of thislist
print(thislist)# Prints items in thislist

thislist.extend(members)# Extends the list by adding members to thislist
members.remove("Bonface")# Removes "Bonface" from members
thislist.pop(2)# Removes the item at index 2 from thislist
print(members)# Prints items in members

print((type(thislist)))

a = float((input("Enter the first number: ")))
b = float((input("Enter the second number: ")))

def sum(a, b):
    return a + b
result = sum(a, b)
print(f"The sum of {a} and {b} is: {result}")

