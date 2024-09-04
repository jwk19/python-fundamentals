def reverse_string():
    """
    This function prompts the user to input a string and returns the reversed version of it.
    """
    # Prompt the user to input a string
    text = input("Enter a string to reverse: ")
    
    # Reverse the string
    reversed_text = text[::-1]
    
    # Print and return the reversed string
    print(f"The reversed string is: {reversed_text}")
    return reversed_text

