# student_grade.py
# Program to calculate student grade based on average marks

import sys


def calculate_grade(avg):
    """Return grade based on average marks."""
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    print("=== Student Grade Calculator ===")

    try:
        if len(sys.argv) == 7:
            # Case 1: Arguments passed (CLI / Jenkins)
            name = sys.argv[1]
            dept = sys.argv[2]
            semester = sys.argv[3]
            m1 = float(sys.argv[4])
            m2 = float(sys.argv[5])
            m3 = float(sys.argv[6])
        else:
            # Case 2: Console input
            name = input("Enter student name: ")
            dept = input("Enter department: ")
            semester = input("Enter semester: ")
            m1 = float(input("Enter marks for Subject 1: "))
            m2 = float(input("Enter marks for Subject 2: "))
            m3 = float(input("Enter marks for Subject 3: "))

        average = (m1 + m2 + m3) / 3
        grade = calculate_grade(average)

        print("\n=== Student Details ===")
        print("Name       :", name)
        print("Department :", dept)
        print("Semester   :", semester)
        print("Marks      :", m1, m2, m3)
        print(f"Average    : {average:.2f}")
        print("Grade      :", grade)

    except ValueError:
        print("Invalid input! Please enter valid numeric marks.")
