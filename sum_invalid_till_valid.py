def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Get two valid numbers from the user
num1 = get_valid_number("Enter the first number: ")
num2 = get_valid_number("Enter the second number: ")

# Calculate and display the sum
total = num1 + num2
print("✅ The sum is:", total)