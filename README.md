# A05 Enhanced Calculator Design Patterns

## Overview

This project is an enhanced command-line calculator developed in Python for IS 601. The application demonstrates advanced Object-Oriented Programming concepts, design patterns, data persistence, and automated testing.

## Features

- REPL (Read-Eval-Print Loop) interface
- Addition, subtraction, multiplication, division, power, and root operations
- Strategy Pattern
- Factory Pattern
- Observer Pattern
- Memento Pattern
- Facade Pattern
- Configuration management using environment variables
- Calculation history management with pandas
- CSV persistence
- Undo and redo functionality
- Input validation and error handling
- Automated testing with pytest
- Continuous Integration with GitHub Actions

## Project Structure

```text
app/
├── calculator.py
├── calculation.py
├── calculator_config.py
├── calculator_memento.py
├── exceptions.py
├── history.py
├── input_validators.py
└── operations.py

tests/
├── test_calculations.py
├── test_calculator.py
├── test_history.py
└── test_operations.py
```

## Requirements

- Python 3.x
- pandas
- pytest
- pytest-cov
- python-dotenv

## Installation

```bash
git clone <repository-url>
cd A05_Enhanced_Calculator_Design_Patterns

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Running the Application

```bash
python app/calculator.py
```

## Running Tests

```bash
pytest
```

## Author

Yovanny Moscoso

Course: IS 601 - Web Systems Development Using Python