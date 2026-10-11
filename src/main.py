
"""Command-line application for student CGPA management."""

from student_performance import calculate_cgpa, classify_performance


def main() -> None:
    """Collect semester GPAs and display student performance."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        count = int(input("Enter number of semesters: "))

        if count <= 0:
            print("Number of semesters must be positive.")
            return

        semester_gpas = []

        for semester in range(1, count + 1):
            gpa = float(input(f"Enter GPA for semester {semester}: "))
            semester_gpas.append(gpa)

        cgpa = calculate_cgpa(semester_gpas)
        performance = classify_performance(cgpa)

        print(f"\nStudent: {name}")
        print(f"CGPA: {cgpa:.2f}")
        print(f"Performance: {performance}")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
