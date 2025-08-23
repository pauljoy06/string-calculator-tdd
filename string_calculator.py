def add(numbers: str) -> int:
    """String calculator that adds numbers from a string."""
    if numbers == "":
        return 0
    
    # Handle custom delimiter
    if numbers.startswith("//"):
        delimiter_line, number_string = numbers.split("\n", 1)
        delimiter_part = delimiter_line[2:]  # Remove "//"
        
        # Check if delimiter is in bracket format [delimiter]
        if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
            custom_delimiter = delimiter_part[1:-1]  # Remove brackets
        else:
            custom_delimiter = delimiter_part
        
        number_string = number_string.replace(custom_delimiter, ",")
        numbers = number_string
    
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    
    # Convert to integers and check for negative numbers
    numbers = [int(part) for part in parts]
    negatives = [num for num in numbers if num < 0]
    if negatives:
        negative_str = ",".join(str(n) for n in negatives)
        raise ValueError(f"negative numbers not allowed {negative_str}")
    
    # Ignore numbers bigger than 1000
    valid_numbers = [num for num in numbers if num <= 1000]
    
    return sum(valid_numbers)