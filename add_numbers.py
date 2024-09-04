def add_numbers():
    """
    This function prompts the user to input two numbers,
    then returns and prints their sum.
    """
    try:
        # Prompt the user to input the first number
        num1 = float(input("Enter the first number: "))
        
        # Prompt the user to input the second number
        num2 = float(input("Enter the second number: "))
        
        # Calculate the sum of the two numbers
        result = num1 + num2
        
        # Print and return the result
        print(f"The sum of {num1} and {num2} is {result}.")
        return result
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return None

