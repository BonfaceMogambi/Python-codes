# Read input
c0 = int(input("Enter a natural number: "))

steps = 0  # counter

# Collatz sequence
while c0 != 1:
    if c0 % 2 == 0:        # even
        c0 = c0 // 2
    else:                  # odd
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("Steps =", steps)
