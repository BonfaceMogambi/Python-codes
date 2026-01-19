set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena", "apple"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4) # join multiple sets
print(myset) # no duplicates

myset = set1 | set2 | set3 |set4 # join multiple sets using the pipe operator
print(myset)

set5 = set3.intersection(set4) # keeps duplicates
print(set5) 

set6 = set3 & set4 # keeps duplicates using the ampersand operator
print(set6)


set7 = {"apple", "banana", "cherry"}
set8 = {"google", "microsoft", "apple"}
set9 = set7.difference(set8)
print(set9) # items in set7 but not in set8


set9 = set7 - set8
print(set9) # items in set7 but not in set8 using the minus operator


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) # items in set1 or set2 but not both

set3 = set1 ^ set2
print(set3) # items in set1 or set2 but not both using the caret operator