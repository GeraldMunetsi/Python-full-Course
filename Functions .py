def split_string(string, delimiter):
    """
    Split a string into a list of substrings based on the specified delimiter.
    
    Args:
        string (str): The input string to be split.
        delimiter (str): The delimiter to split the string.
    
    Returns:
        list: A list of substrings.
    """
    return string.split(delimiter)
input_string = "Hello, world! How are you?"
delimiter = " "  # Split the string at every space character
result = split_string(input_string, delimiter)
print(result)

def count_vowels(string):
    """
    Count the number of vowels in a string.
    
    Args:
        string (str): The string to be analyzed.
    
    Returns:
        int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)
## strip function
#string.strip([characters])  whitespace removed from string, use characters to be specific