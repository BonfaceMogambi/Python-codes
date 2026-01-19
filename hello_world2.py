def get_string(prompt):
    while True:
        try:
            value = str(input(prompt))
            if value.strip() == "":
                raise ValueError("Input cannot be empty.")
            if not all(char.isalpha() or char.isspace() for char in value):
                raise ValueError("Input must contain only alphabetic characters and spaces.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
first_name = get_string("Enter your first name: ")
last_name = get_string("Enter your last name: ")
print(f"Hello, {first_name} {last_name}! Welcome to the course.")