def sort_by_age(people):
    """
    This function takes a list of tuples where each tuple contains a name and an age.
    It returns the list sorted by age in ascending order.
    """
    # Sort the list by age (the second element in the tuple)
    return sorted(people, key=lambda person: person[1])

def get_people_input():
    """
    This function prompts the user to input names and ages, then returns a list of tuples.
    """
    people = []
    
    # Prompt user for the number of entries
    try:
        n = int(input("How many people do you want to enter? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Loop to get names and ages from the user
    for _ in range(n):
        name = input("Enter the person's name: ")
        try:
            age = int(input(f"Enter {name}'s age: "))
        except ValueError:
            print("Please enter a valid age.")
            return
        
        people.append((name, age))
    
    # Return the list of tuples
    return people

def main():
    """
    This function will run the program interactively.
    """
    # Get input from the user
    people = get_people_input()
    
    if people:  # Proceed only if the input is valid
        # Sort the list by age
        sorted_people = sort_by_age(people)
        
        # Print the sorted list
        print("\nPeople sorted by age (ascending):")
        for name, age in sorted_people:
            print(f"{name}: {age} years old")

