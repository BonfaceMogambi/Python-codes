
x = lambda a: a*5
print(x(4))

temp =30

print(temp if temp < 25 else "Too cold" if temp < 15 else "Just calm"  if temp > 20 else "Too cold")

def myfunc(n):
  return lambda b : b * n

mydoubler = myfunc(2)

print(mydoubler(11))