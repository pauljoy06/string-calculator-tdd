def add(numbers: str) -> int:
    """String calculator that adds numbers from a string."""
    if numbers == "":
        return 0
    parts = numbers.split(",")
    return sum(int(part) for part in parts)