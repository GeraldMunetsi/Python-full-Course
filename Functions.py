


def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    """
    return length * width
    
 
 def reverse_string(string):
    """
    Reverse a string.
    
    Args:
        string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return string[::-1]  

def find_max(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float or int: The maximum value in the list.
    """
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
  
   