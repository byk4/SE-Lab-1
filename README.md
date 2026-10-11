# Student CGPA Performance Management System

## Overview

A Python command-line application for collecting one student's semester GPAs, calculating a CGPA, and classifying academic performance. The calculation and validation functions are in `src/student_performance.py`; `src/main.py` provides the interactive command-line flow.

## Features

- Prompts for a non-empty student name and a positive number of semesters.
- Prompts for one GPA per semester and validates each value from 0 through 10, inclusive.
- Calculates the equally weighted arithmetic mean and rounds the result to two decimal places.
- Classifies the calculated CGPA as Excellent, Very Good, Good, Average, or Needs Improvement.
- Includes automated tests for the calculation and validation functions.

## Technology Stack

- Python 3 (Ruff is configured to target Python 3.11; a formal minimum supported Python version is not declared.)
- Visual Studio Code
- Git and GitHub
- Pytest
- Ruff
- GitHub Copilot

The application code uses only the Python standard library. Pytest and Ruff are development tools.

## Setup

Use Python 3.11 for the documented lint target. Create and activate a virtual environment, then install the development tools.

On Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest ruff
```

On macOS or Linux:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install pytest ruff
```

The project does not currently declare a separate runtime minimum or package dependency list in `pyproject.toml`.

## Run the Application

```bash
python src/main.py
```

The CLI asks for a student name, a positive semester count, and one GPA per semester. It reports invalid input in the terminal and prints the rounded CGPA and performance category when input is valid.

## Run Tests

```bash
python -m pytest -v
```

Pytest is configured to discover tests in `tests/` and to add the repository root to the import path. Current tests exercise `validate_gpa`, `calculate_cgpa`, and `classify_performance` directly; they do not automate the interactive CLI in `src/main.py`.

## Check Code Quality

```bash
python -m ruff check .
```

Ruff uses an 88-character line length, targets Python 3.11, and enables the `E`, `F`, and `I` rule families.

## Calculation And Classification

The application uses an equally weighted arithmetic mean:

$$
\mathrm{CGPA} = \frac{\sum_{i=1}^{n} \mathrm{GPA}_i}{n}
$$

The GPA range is inclusive: $0 \leq \mathrm{GPA} \leq 10$. The implementation accepts Python `int` and `float` values, rejects booleans and values outside the range, and raises `ValueError` for an empty semester list. Fractional float GPAs are supported; `decimal.Decimal` values are not accepted by the current validator. Non-finite floats such as NaN and infinity are rejected by the range check.

The rounded CGPA is classified using these lower bounds:

| CGPA | Classification |
| --- | --- |
| 9.00 and above | Excellent |
| 8.00 to below 9.00 | Very Good |
| 7.00 to below 8.00 | Good |
| 6.00 to below 7.00 | Average |
| Below 6.00 | Needs Improvement |

The CLI classifies the rounded result returned by `calculate_cgpa`. This is a demonstration formula; adapt it if institutional rules require credit weighting or different rounding and classification policies.

## AI Usage

GitHub Copilot was used for code generation, explanation, test design, debugging, and refactoring. Suggestions were reviewed by the developer and checked against the implementation and available automated checks.

## Security

Do not commit passwords, API keys, access tokens, confidential student records, or local environment files. The CLI displays the entered student name and resulting CGPA in the terminal; avoid entering real confidential student data on shared machines or in recorded terminal sessions.

## Limitations

This version does not store records permanently, use a database, transmit data to a service, or implement authentication and authorization. It handles one student per run, uses an equally weighted mean, and has no automated end-to-end tests for its interactive CLI. The project does not declare a formal minimum supported Python version.