"""Student CGPA calculation and performance utilities."""

_MIN_GPA = 0
_MAX_GPA = 10
_PERFORMANCE_THRESHOLDS = (
    (9, "Excellent"),
    (8, "Very Good"),
    (7, "Good"),
    (6, "Average"),
)


def validate_gpa(gpa: float) -> None:
    """Raise ValueError when a GPA is outside the 0–10 range."""
    if not isinstance(gpa, (int, float)) or isinstance(gpa, bool):
        raise ValueError("GPA must be a number.")

    if not _MIN_GPA <= gpa <= _MAX_GPA:
        raise ValueError("GPA must be between 0 and 10.")


def calculate_cgpa(semester_gpas: list[float]) -> float:
    """Calculate the arithmetic mean of semester GPAs."""
    if not semester_gpas:
        raise ValueError("At least one semester GPA is required.")

    for gpa in semester_gpas:
        validate_gpa(gpa)

    total_gpa = sum(semester_gpas)
    semester_count = len(semester_gpas)
    return round(total_gpa / semester_count, 2)


def classify_performance(cgpa: float) -> str:
    """Return a descriptive performance category."""
    validate_gpa(cgpa)

    for threshold, category in _PERFORMANCE_THRESHOLDS:
        if cgpa >= threshold:
            return category

    return "Needs Improvement"
