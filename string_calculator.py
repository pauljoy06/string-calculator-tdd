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
    return sum(int(part) for part in parts)