# Number Analyzer

A Python program that analyzes user-provided numbers and calculates basic statistics.

## Features

- Checks whether numbers are even or odd
- Checks whether numbers are positive, negative, or zero
- Accepts multiple numbers at once
- Handles invalid input
- Calculates:
  - Number of even numbers
  - Number of odd numbers
  - Number of positive numbers
  - Number of negative numbers
  - Number of zeros
  - Sum
  - Average
- Allows the user to run the program multiple times

## Technologies

- Python 3
- `unittest`

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:

```bash
git clone https://github.com/A-mohamad-dev/number-analyzer.git
```

3. Open the project folder:

```bash
cd number-analyzer
```

4. Run the program:

```bash
python number_analyzer.py
```

## Testing

This project uses Python's built-in `unittest` framework for automated testing.

The tests cover:

- Even and odd numbers
- Positive and negative numbers
- Zero
- Statistical calculations
- Empty input

To run the tests, open a terminal in the project folder and run:

```bash
python -m unittest
```

## Example

```text
Enter numbers separated with spaces: 5 -8 0 13 24

========== Number Analyzer ==========

    5 is odd and positive
   -8 is even and negative
    0 is even and zero
   13 is odd and positive
   24 is even and positive

------------- Statistics ------------

Even:      3
Odd:       2
Positive:  3
Negative: 1
Zero:      1
Sum:       34
Average:   6.8

Do you want to analyze more numbers? (y/n):
```

## Project Structure

```text
number-analyzer/
├── number_analyzer.py
├── test_number_analyzer.py
├── README.md
└── .gitignore
```

## What I Learned

This project helped me practice:

- Functions
- Lists
- Loops
- Conditional statements
- Exception handling
- Dictionaries
- User input
- Basic statistics
- Function decomposition
- Returning data from functions
- Unit testing
- Git and GitHub

## Future Improvements

- Add more statistical calculations
- Improve input validation
- Add a graphical user interface