def add(numbers: str) -> int:
    """String calculator that adds numbers from a string."""
    if numbers == "":
        return 0
    
    # Handle custom delimiter
    if numbers.startswith("//"):
        delimiter_line, number_string = numbers.split("\n", 1)
        custom_delimiter = delimiter_line[2:]  # Remove "//"
        number_string = number_string.replace(custom_delimiter, ",")
        numbers = number_string
    
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    
    # Check for negative numbers
    negatives = [int(part) for part in parts if int(part) < 0]
    if negatives:
        negative_str = ",".join(str(n) for n in negatives)
        raise ValueError(f"negative numbers not allowed {negative_str}")
    
    return sum(int(part) for part in parts)