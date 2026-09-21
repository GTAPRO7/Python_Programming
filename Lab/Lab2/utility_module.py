# utility_module.py

def get_valid_string(prompt):
    """Ensures the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")

def get_valid_float(prompt, min_value=0.0):
    """Ensures the user enters a valid float greater than min_value."""
    while True:
        try:
            value = float(input(prompt))
            if value <= min_value:
                print("Error: Value must be greater than {}.".format(min_value))
            else:
                return value
        except ValueError:
            print("Error: Invalid number format. Please enter digits.")

def get_alphanumeric_string(prompt, exact_length):
    """Ensures the user enters an alphanumeric string of an exact length."""
    while True:
        value = input(prompt).strip()
        if len(value) == exact_length and value.isalnum():
            return value.upper()
        print("Error: Input must be exactly {} alphanumeric characters.".format(exact_length))

def print_header(title, width=50):
    """Domain-independent reporting utility to print standard headers."""
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)

def get_unique_alphanumeric(prompt, exact_length, existing_keys):
    """Ensures the user enters a unique alphanumeric string of an exact length."""
    while True:
        value = input(prompt).strip()
        
        # Check length and alphanumeric format first
        if len(value) != exact_length or not value.isalnum():
            print("Error: Input must be exactly {} alphanumeric characters.".format(exact_length))
            continue
            
        value = value.upper()
        
        # Check for uniqueness
        if value in existing_keys:
            print("Error: This ID is already registered. Please enter a different one.")
        else:
            return value