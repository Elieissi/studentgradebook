"""
Student Gradebook Management Program

This Python program allows users to manage a gradebook with nested subject structures.
Users can add students, record grades across multiple categories, and calculate
class averages, individual grades, and top performers. All data is stored in nested dictionaries.

Features:
- Add/Remove students
- View all grades
- Calculate class average for a subject
- View a specific student’s grades
- Determine the top-performing student in a subject
- Compute overall average grade in a subject

Pseudocode for main structure:
1. Initialize gradebook with sample data
2. Show menu and prompt user for input
3. Use if/elif to call correct function
4. Functions manipulate gradebook as needed
5. Loop continues until user chooses to exit

Dictionary Structure:
{
  "StudentName": {
    "Subject": {
      "Subcategory": grade (int)
    }
  }
}
"""

def remove_student(gradebook):
    while True:
        student = input("Enter a student to remove: ").strip()
        if student in gradebook:
            del gradebook[student]
            print(f"{student} has been removed.")
            break
        else:
            print("Student not found. Try again.")


def view_all_grades(gradebook):
    for student, subjects in gradebook.items():
        print(f"\n{student}'s Grades:")
        for subject, subcategories in subjects.items():
            print(f"  {subject}:")
            for subcat, grade in subcategories.items():
                print(f"    {subcat}: {grade}")


def class_subject_avg(gradebook):
    subject = input("Enter a subject to average (e.g., Math): ").strip()
    total = 0
    count = 0
    for subjects in gradebook.values():
        if subject in subjects:
            for grade in subjects[subject].values():
                total += grade
                count += 1
    if count:
        print(f"Class average for {subject}: {total / count:.2f}")
    else:
        print("No grades found for that subject.")


def top_student_total(gradebook):
    category = input("Select a subject category (e.g., Math): ").strip()
    max_total = -1
    top_student = None
    for student, subjects in gradebook.items():
        if category in subjects:
            total = sum(subjects[category].values())
            if total > max_total:
                max_total = total
                top_student = student
    if top_student:
        print(f"Top student in {category}: {top_student} with total {max_total}")
    else:
        print("Invalid subject or no data.")


def avg_grade_total(gradebook):
    subject = input("Enter a subject name (e.g., Math): ").strip()
    total = 0
    count = 0
    for subjects in gradebook.values():
        if subject in subjects:
            for grade in subjects[subject].values():
                total += grade
                count += 1
    if count:
        print(f"Overall average in {subject}: {total / count:.2f}")
    else:
        print("Subject not found.")


def student_all_grades(gradebook):
    student = input("Enter the student's name: ").strip()
    if student in gradebook:
        for subject, subcategories in gradebook[student].items():
            print(f"{subject}:")
            for subcat, grade in subcategories.items():
                print(f"  {subcat}: {grade}")
    else:
        print("Student not found.")


def add_student(gradebook):
    student = input("Enter new student name: ").strip()
    try:
        stat = int(input("Statistics grade: "))
        calc = int(input("Calculus grade: "))
        read = int(input("Reading grade: "))
        write = int(input("Writing grade: "))
    except ValueError:
        print("Invalid grade input. Please enter integers.")
        return

    gradebook[student] = {
        "Math": {"Statistics": stat, "Calculus": calc},
        "English": {"Reading": read, "Writing": write}
    }
    print(f"{student} has been added.")


def main():
    gradebook = {
        "Alice": {
            "Math": {"Statistics": 91, "Calculus": 81},
            "English": {"Reading": 66, "Writing": 71}
        },
        "Antony": {
            "Math": {"Statistics": 42, "Calculus": 32},
            "English": {"Reading": 5, "Writing": 7}
        },
        "Elie": {
            "Math": {"Statistics": 100, "Calculus": 62},
            "English": {"Reading": 90, "Writing": 87}
        }
    }

    while True:
        print("\nGrade Book Menu:")
        print("1: Add a student")
        print("2: Remove a student")
        print("3: View all student grades")
        print("4: View class subject average")
        print("5: View a student's grades")
        print("6: View top student in subject")
        print("7: View overall subject average")
        print("8: Exit")

        command = input("Enter your choice: ").strip()

        if command == "1":
            add_student(gradebook)
        elif command == "2":
            remove_student(gradebook)
        elif command == "3":
            view_all_grades(gradebook)
        elif command == "4":
            class_subject_avg(gradebook)
        elif command == "5":
            student_all_grades(gradebook)
        elif command == "6":
            top_student_total(gradebook)
        elif command == "7":
            avg_grade_total(gradebook)
        elif command == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
