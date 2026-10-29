def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter your mark for {subject} (0-100): "))

            if 0 <= mark <= 100:
                return mark

            print("Invalid mark! Please enter a mark between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def analyze_results():
    print("\n===== STUDENT MARKS ANALYZER =====")

    subjects = [
        "Mathematics",
        "Computer literacy",
        "Statistics",
        "Calculus",
        "Database Management"
    ]

    marks = {}

    for subject in subjects:
        marks[subject] = get_mark(subject)

    average = sum(marks.values()) / len(marks)

    highest = max(marks, key=marks.get)
    lowest = min(marks, key=marks.get)

    print("\n===== RESULTS SUMMARY =====")

    for subject, mark in marks.items():
        print(f"{subject}: {mark:.2f}%")

    print(f"\nAverage mark: {average:.2f}%")
    print(f"Highest mark: {highest} ({marks[highest]}%)")
    print(f"Lowest mark: {lowest} ({marks[lowest]}%)")

    if average >= 75:
        print("Overall performance: Distinction-level")
    elif average >= 50:
        print("Overall performance: Pass-level")
    else:
        print("Overall performance: Needs improvement")

    struggling = [
        subject for subject, mark in marks.items()
        if mark < 50
    ]

    if struggling:
        print("\nSubjects needing improvement:")
        for subject in struggling:
            print(f"- {subject}")
    else:
        print("\nCongratulations! You passed all five subjects.")


if __name__ == "__main__":
    analyze_results()
