# Student Grade Calculator


def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"

def main():
    # Accept student details
    name = "srushti.b"
    department = "BCA"
    semester = 3

    marks = []
    sample_mark=[75,82,68]
    
    for i in range(len(sample_mark)):
        marks.append(sample_mark[i])
        
        avg = sum(marks) / len(marks)

    

    # Determine grade
    grade = calculate_grade(avg)

    # Display student details and grade
    print("\n--- Student Report ---")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Marks      : {marks}")
    print(f"Average    : {avg:.2f}")
    print(f"Grade      : {grade}")

if __name__ == "__main__":
    main()