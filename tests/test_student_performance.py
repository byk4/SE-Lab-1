
"""Automated tests for student performance utilities."""

import pytest

from src.student_performance import (
    calculate_cgpa,
    classify_performance,
    validate_gpa,
)


@pytest.mark.parametrize("gpa", [0, 5.5, 10])
def test_validate_gpa_accepts_valid_values(gpa):
    validate_gpa(gpa)


@pytest.mark.parametrize(
    "gpa",
    [
        -1,
        -0.01,
        10.01,
        10.1,
        "8",
        True,
        None,
        float("nan"),
        float("inf"),
        float("-inf"),
    ],
)
def test_validate_gpa_rejects_invalid_values(gpa):
    with pytest.raises(ValueError):
        validate_gpa(gpa)


def test_calculate_cgpa():
    assert calculate_cgpa([8, 9, 7]) == 8.0


def test_calculate_cgpa_rounds_to_two_decimal_places():
    assert calculate_cgpa([8, 9, 8]) == 8.33


@pytest.mark.parametrize(
    ("semester_gpas", "expected"),
    [([8.344, 8.344], 8.34), ([8.346, 8.346], 8.35)],
)
def test_calculate_cgpa_rounds_down_and_up(semester_gpas, expected):
    assert calculate_cgpa(semester_gpas) == expected


def test_calculate_cgpa_accepts_fractional_gpas():
    assert calculate_cgpa([8.25, 9.75]) == 9.0


def test_calculate_cgpa_accepts_boundary_values():
    assert calculate_cgpa([0, 10]) == 5.0


def test_calculate_cgpa_rejects_empty_list():
    with pytest.raises(ValueError):
        calculate_cgpa([])


@pytest.mark.parametrize(
    "gpa",
    [-0.01, 10.01, "8", True, None, float("nan"), float("inf")],
)
def test_calculate_cgpa_rejects_invalid_gpa(gpa):
    with pytest.raises(ValueError):
        calculate_cgpa([8, gpa])


@pytest.mark.parametrize(
    ("cgpa", "expected"),
    [
        (9, "Excellent"),
        (8, "Very Good"),
        (7, "Good"),
        (6, "Average"),
        (5, "Needs Improvement"),
    ],
)
def test_classify_performance(cgpa, expected):
    assert classify_performance(cgpa) == expected


@pytest.mark.parametrize(
    ("cgpa", "expected"),
    [
        (8.99, "Very Good"),
        (7.99, "Good"),
        (6.99, "Average"),
        (5.99, "Needs Improvement"),
    ],
)
def test_classify_performance_just_below_thresholds(cgpa, expected):
    assert classify_performance(cgpa) == expected
