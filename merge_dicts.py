def merge_dicts(dict1, dict2):
    """
    This function takes two dictionaries as input and merges them into a single dictionary.
    If there are common keys, their values are summed up.
    
    :param dict1: First dictionary
    :param dict2: Second dictionary
    :return: Merged dictionary with summed values for common keys
    """
    # Create a copy of dict1 to avoid modifying the original dictionary
    merged_dict = dict1.copy()
    
    # Iterate over dict2 and update the merged_dict
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key exists in both dictionaries, sum their values
            merged_dict[key] += value
        else:
            # Otherwise, add the new key-value pair to the merged dictionary
            merged_dict[key] = value
    
    return merged_dict

def get_dict_input(dict_num):
    """
    This function prompts the user to input key-value pairs for a dictionary.
    
    :param dict_num: Identifier for which dictionary is being input
    :return: A dictionary created from the user input
    """
    dictionary = {}
    try:
        n = int(input(f"How many key-value pairs do you want to add to dictionary {dict_num}? "))
    except ValueError:
        print("Invalid number, please enter an integer.")
        return dictionary
    
    for _ in range(n):
        key = input(f"Enter key (string) for dictionary {dict_num}: ")
        try:
            value = int(input(f"Enter value (integer) for key '{key}': "))
        except ValueError:
            print("Invalid value, please enter an integer.")
            return dictionary
        dictionary[key] = value
    
    return dictionary

def main():
    """
    Main function to merge two dictionaries interactively.
    """
    print("Input for the first dictionary:")
    dict1 = get_dict_input(1)
    
    print("\nInput for the second dictionary:")
    dict2 = get_dict_input(2)
    
    # Merge the dictionaries
    merged_dict = merge_dicts(dict1, dict2)
    
    # Print the result
    print("\nMerged dictionary:")
    print(merged_dict)