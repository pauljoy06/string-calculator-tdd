import re


def add(numbers: str) -> int:
    """String calculator that adds numbers from a string."""
    if numbers == "":
        return 0
    
    # Handle custom delimiter
    if numbers.startswith("//"):
        delimiter_line, number_string = numbers.split("\n", 1)
        delimiter_part = delimiter_line[2:]  # Remove "//"
        
        # Check if delimiter is in bracket format [delimiter] or multiple [delim1][delim2]
        if "[" in delimiter_part and "]" in delimiter_part:
            # Extract all delimiters between brackets
            delimiters = re.findall(r'\[([^\]]+)\]', delimiter_part)
            # Replace all delimiters with comma
            for delimiter in delimiters:
                number_string = number_string.replace(delimiter, ",")
        else:
            # Single delimiter without brackets
            number_string = number_string.replace(delimiter_part, ",")
        
        numbers = number_string
    
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    
    # Convert to integers and check for negative numbers
    number_list = [int(part) for part in parts]
    negatives = [num for num in number_list if num < 0]
    if negatives:
        negative_str = ",".join(str(n) for n in negatives)
        raise ValueError(f"negative numbers not allowed {negative_str}")
    
    # Ignore numbers bigger than 1000
    valid_numbers = [num for num in number_list if num <= 1000]
    
    return sum(valid_numbers)