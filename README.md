# String Calculator TDD Kata

A Test-Driven Development (TDD) implementation of a string calculator following the Red-Green-Refactor cycle.

## Requirements

Implement a method `add(numbers: str) -> int` that:

1. Returns 0 for empty string
2. Returns the number for single number input
3. Returns sum for comma-separated numbers
4. Handles any amount of numbers
5. Supports newline as separator
6. Supports custom delimiters
7. Throws exception for negative numbers

## How to Run

### Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run Tests
```bash
pytest test_string_calculator.py -v
```

### Run with Coverage
```bash
pytest test_string_calculator.py --cov=string_calculator --cov-report=html
```

## TDD Approach

This project follows strict Test-Driven Development:

1. **RED**: Write a failing test
2. **GREEN**: Write minimal code to make the test pass
3. **REFACTOR**: Improve code while keeping tests green

Each step is committed separately to show the TDD progression.

## Implementation Progress

- [x] Empty string returns 0
- [ ] Single number returns that number
- [ ] Two comma-separated numbers return sum
- [ ] Handle multiple comma-separated numbers
- [ ] Handle newlines as separators
- [ ] Support custom delimiters
- [ ] Validate negative numbers