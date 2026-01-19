def myfunc(n):
  return abs(n - 50) # Function to calculate the absolute difference from 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # Sort the list based on the absolute difference from 50
print(thislist)