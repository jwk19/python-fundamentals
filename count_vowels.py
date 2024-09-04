def count_vowels():
    """
    This function prompts the user to input a string and returns the count of vowels
    (a, e, i, o, u) in the string, ignoring case sensitivity.
    """
    # Prompt the user to input a string
    text = input("Enter a string: ")
    
    # Define the set of vowels
    vowels = set('aeiou')
    
    # Convert the text to lowercase and count the vowels
    count = sum(1 for char in text.lower() if char in vowels)
    
    # Print and return the result
    print(f"The number of vowels in the string is: {count}")
    return count

