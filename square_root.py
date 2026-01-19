
a = float(input("Enter a number to find its square root: "))
try:
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    square_root = a ** 0.5
    print(f"The square root of {a} is {square_root}.")
except ValueError as ve:
    print(ve)