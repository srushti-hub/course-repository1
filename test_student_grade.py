import pytest
from student_grade import calculate_grade, main   # <-- replace student_grade with your filename

def test_calculate_grade_boundaries():
    # Grade S
    assert calculate_grade(90) == "S"
    assert calculate_grade(100) == "S"
    # Grade A
    assert calculate_grade(80) == "A"
    assert calculate_grade(89) == "A"
    # Grade B
    assert calculate_grade(65) == "B"
    assert calculate_grade(79) == "B"
    # Grade C
    assert calculate_grade(50) == "C"
    assert calculate_grade(64) == "C"
    # Grade D
    assert calculate_grade(40) == "D"
    assert calculate_grade(49) == "D"
    # Grade F
    assert calculate_grade(39) == "F"
    assert calculate_grade(0) == "F"

def test_main_output(capsys):
    # Run main() and capture output
    main()
    captured = capsys.readouterr()

    # Check that expected details are printed
    assert "--- Student Report ---" in captured.out
    assert "Name       : sri gouri" in captured.out
    assert "Department : BCA" in captured.out
    assert "Semester   : 3" in captured.out
    assert "Marks      : [75, 82, 68]" in captured.out
    # Average should be (75+82+68)/3 = 75.0
    assert "Average    : 75.00" in captured.out
    assert "Grade      : B" in captured.out
