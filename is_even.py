def is_even():
    """
    This function prompts the user to input a number and returns True if the number is even,
    and False if it is odd.
    """
    try:
        # Prompt the user to input a number
        number = int(input("Enter a number: "))
        
        # Check if the number is even
        if number % 2 == 0:
            print(f"{number} is even.")
            return True
        else:
            print(f"{number} is odd.")
            return False
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return None
