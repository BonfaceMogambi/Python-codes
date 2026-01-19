y = 10

def validate_positive_number(value):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError("The number must be a positive integer or float.")
    return True
def validate_string(value):
    if not isinstance(value, str) or not value:
        raise ValueError("The value must be a non-empty string.")
    return True

while True:
    try:
        user_input = input("Please enter a positive number: ")
        number = float(user_input)
        validate_positive_number(number)
        print(f"You entered a valid positive number: {number}")
        break
    except ValueError as e:
        print(e)