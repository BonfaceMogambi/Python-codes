def greet():
    print("Hello, World!")
# This function prints a greeting message.
# It can be called to display the message.
greet()
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
print(add(3, 5))  # Example usage of the add function
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b
print(multiply(4, 7))  # Example usage of the multiply function
def greet(name="Member"):
    print(f"Hello, {name}!")

greet()          # Hello, Member!
greet("Alice")