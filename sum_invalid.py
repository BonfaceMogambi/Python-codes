try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2

    # Display the result
    print("The sum is:", total)

except ValueError:
    print(f"❌ Invalid input! Please enter numeric values only.")