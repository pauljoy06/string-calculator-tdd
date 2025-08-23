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

### Core Requirements
- [x] Empty string returns 0
- [x] Single number returns that number
- [x] Two comma-separated numbers return sum
- [x] Handle multiple comma-separated numbers
- [x] Handle newlines as separators
- [x] Support custom delimiters
- [x] Validate negative numbers

### Extended Requirements
- [x] Numbers bigger than 1000 are ignored
- [x] Delimiters of any length with bracket format `//[delimiter]\n`
- [x] Multiple delimiters with format `//[delim1][delim2]\n`
- [x] Multiple delimiters with length longer than one char

## Test Results

All 11 requirements have been successfully implemented using strict TDD methodology. Each feature was developed following the Red-Green-Refactor cycle with meaningful commit messages showing the progression.

**Final Test Suite**: 11 tests passing, comprehensive coverage of all features and edge cases.

