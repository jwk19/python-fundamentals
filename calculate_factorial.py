def calculate_factorial():
    """
    This function prompts the user to input a non-negative integer
    and returns the factorial of that number.
    """
    try:
        # Prompt the user for input
        n = int(input("Enter a non-negative integer: "))
        
        # Ensure the input is non-negative
        if n < 0:
            raise ValueError("The number must be non-negative.")
        
        # Base case: 0! = 1
        if n == 0:
            print(f"The factorial of {n} is 1.")
            return 1
        
        # Calculate the factorial using a loop
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        
        # Print and return the factorial
        print(f"The factorial of {n} is {factorial}.")
        return factorial
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")


