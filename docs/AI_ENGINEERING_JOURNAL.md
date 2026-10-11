# AI Engineering Journal

## Project Information

- **Project:** Student CGPA Performance Management System
- **Language:** Python
- **IDE:** Visual Studio Code
- **Version Control:** Git and GitHub
- **AI Assistant:** GitHub Copilot
- **Testing Tool:** Pytest
- **Code Quality Tool:** Ruff

## Entry 1: AI-Assisted Code Generation

- **Objective:** Generate CGPA calculation and validation logic.
- **Prompt:** Generate a CGPA calculation function with input validation and two-decimal rounding.
- **AI Suggestion:** Keep GPA validation separate from calculation. Reject nonnumeric, boolean, and out-of-range GPAs; reject an empty semester list; validate each GPA before calculating the arithmetic mean and rounding it to two decimal places.
- **Human Review:** Checked inclusive 0 and 10 boundaries, empty input, the arithmetic mean, and rounding behavior.
- **Validation:** Pytest coverage exercised valid values, invalid values, empty input, and rounded results. A later recorded `python -m pytest -v` run exited successfully.
- **Decision:** Accepted the separate validation and calculation structure and retained the focused validation rules. Added edge-case coverage as described in Entry 3.

## Entry 2: AI-Assisted Code Explanation

- **Objective:** Understand the calculation and validation functions.
- **Prompt:** Explain the CGPA calculation function line by line.
- **AI Suggestion:** Explained the empty-input guard, per-GPA validation, sum divided by the number of semesters, and rounding. Also noted linear time complexity and that the list type annotation is not enforced at runtime.
- **Human Review:** Compared the explanation with the source code and confirmed that validation completes before the mean is calculated.
- **Decision:** Accepted the explanation. The limitations around input types and floating-point rounding were kept in mind when interpreting behavior.

## Entry 3: AI-Assisted Test Generation

- **Objective:** Improve test coverage.
- **Prompt:** Generate pytest tests for valid and invalid GPAs, empty input, rounding and classification.
- **AI Suggestion:** Add checks for just-outside GPA bounds, nonnumeric and non-finite values, fractional GPA inputs, rounding in both directions, and values immediately below performance thresholds. The empty-list case was already covered.
- **Human Review:** Checked expected values against the implementation and retained the existing empty-list test rather than duplicating it.
- **Decision:** Accepted the additional boundary, invalid-input, fractional-value, rounding, and classification-threshold cases in `tests/test_student_performance.py`.

## Entry 4: AI-Assisted Debugging

- **Objective:** Identify and fix a division-by-zero defect.
- **Observed Error:** The calculator's return expression divided by the literal `0`, raising `ZeroDivisionError` for `[8, 9, 7]` after GPA validation succeeded.
- **AI Suggestion:** Divide the sum by `len(semester_gpas)`, the number of semesters.
- **Human Review:** Checked that this is the arithmetic-mean formula and that the earlier empty-input guard ensures a nonzero denominator.
- **Validation:** The failing call was reproduced. The existing calculation test asserts that `[8, 9, 7]` returns `8.0`; direct runtime checks passed once the denominator used the list length.
- **Decision:** Accepted the denominator correction and restored the intended arithmetic mean.

## Entry 5: AI-Assisted Refactoring

- **Objective:** Improve readability and maintainability.
- **Prompt:** Refactor the module without changing its public behavior.
- **AI Suggestion:** Introduce private constants for the valid GPA bounds and ordered performance thresholds, name the total and semester count in the mean calculation, and iterate over the threshold table in classification.
- **Human Review:** Compared the refactored behavior with the existing boundaries and classification categories. Public function names and signatures, validation behavior, exception messages, and return values were preserved.
- **Validation:** Runtime assertions covered averaging, rounding, invalid values, empty input, and classification thresholds; `py_compile` and editor diagnostics passed. The project terminal recorded `python -m ruff check .` exiting successfully. In a separate active Python environment, pytest and Ruff were unavailable, so the focused runtime checks were used there.
- **Decision:** Accepted the private constants, named calculation steps, and threshold table. No dependencies or public API changes were introduced.

## Security and Responsible AI

- No passwords, access tokens, private keys, or confidential student records were shared with the AI assistant.
- AI-generated code and tests were reviewed before integration.
- Automated tests, runtime checks, and linting were used where available to validate changes.
- Git provides a history for reviewing development changes; no commit was created by the AI assistant during this work.
- Human review remained the final authority for engineering decisions.

## Final Reflection

AI helped draft and explain the calculation, suggest targeted tests, identify the literal-zero denominator defect, and make a small readability refactor. The debugging suggestion was checked against the arithmetic-mean formula before the correct denominator was restored. Test coverage made boundary behavior and threshold transitions explicit, while runtime checks and Ruff added independent validation. Reviewing the source and keeping changes traceable in Git remain important because AI suggestions are starting points, not substitutes for engineering judgment.

