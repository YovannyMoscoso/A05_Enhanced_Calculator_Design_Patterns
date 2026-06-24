# A05 Enhanced Calculator Design Patterns

![Python Application](https://github.com/YovannyMoscoso/A05_Enhanced_Calculator_Design_Patterns/actions/workflows/python-app.yml/badge.svg)

## Overview

This project is an enhanced command-line calculator developed in Python for **IS 601 – Web Systems Development Using Python**.

The application demonstrates Object-Oriented Programming (OOP) principles, software design patterns, configuration management, data persistence, automated testing, and Continuous Integration using GitHub Actions.

The calculator supports mathematical operations, calculation history tracking, undo/redo functionality, CSV persistence, environment-based configuration, and automated test execution with coverage reporting.

---

## Features

* Command-Line (REPL) Calculator Interface
* Addition, Subtraction, Multiplication, and Division
* Power and Root Operations
* Calculation History Management
* Undo and Redo Functionality
* Persistent History Storage using CSV
* Configuration Management using Environment Variables
* Input Validation and Custom Exceptions
* Automated Unit Testing with Pytest
* Code Coverage Reporting
* Continuous Integration using GitHub Actions

---

## Design Patterns Implemented

### Strategy Pattern

Each mathematical operation is implemented as a separate strategy class. This allows operations to be selected and executed dynamically without modifying existing code.

### Factory Pattern

The OperationFactory creates operation objects dynamically and centralizes object creation logic.

### Facade Pattern

The Calculator class acts as a simplified interface that coordinates calculations, history management, configuration loading, and user interaction.

### Memento Pattern

Snapshots of calculator history are stored to support undo and redo functionality.

### Observer Pattern

Observers are notified whenever new calculations are added to the history.

---

## Project Structure

```text
A05_Enhanced_Calculator_Design_Patterns/
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   └── operations.py
│
├── tests/
│   ├── __init__.py
│   ├── test_calculations.py
│   ├── test_calculator.py
│   ├── test_history.py
│   └── test_operations.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone git@github.com:YovannyMoscoso/A05_Enhanced_Calculator_Design_Patterns.git
cd A05_Enhanced_Calculator_Design_Patterns
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root directory:

```env
HISTORY_PATH=history.csv
```

This file allows configuration values to be loaded through environment variables using Python Dotenv.

---

## Running the Application

Run the calculator:

```bash
python -m app.calculator
```

Example:

```text
Enter operation or command: add
Enter first number: 5
Enter second number: 3

Result: 8.0
```

---

## Running Tests

Execute all tests:

```bash
pytest -v
```

Run tests with coverage:

```bash
pytest --cov=app
```

Example output:

```text
21 passed
74% coverage
```

---

## Continuous Integration

This project uses GitHub Actions to automatically:

* Install project dependencies
* Run all unit tests
* Verify project integrity
* Generate test execution results on every push to the main branch

Workflow location:

```text
.github/workflows/python-app.yml
```

---

## Technologies Used

* Python 3.11+
* Pandas
* Pytest
* Pytest-Cov
* Python-Dotenv
* Git
* GitHub
* GitHub Actions

---

## Current Project Metrics

* 21 Unit Tests Passing
* 74% Code Coverage
* GitHub Actions Workflow Passing
* Multiple Design Patterns Implemented
* Environment Variable Configuration
* CSV Data Persistence

---

## Course Information

**Course:** IS 601 – Web Systems Development Using Python

**Institution:** New Jersey Institute of Technology (NJIT)

**Semester:** Summer 2026

---

## Author

**Yovanny Moscoso**

GitHub: https://github.com/YovannyMoscoso
