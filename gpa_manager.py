import json
import os

def calculate_gpa(grades):
    if not grades:
        return 0.0
    return sum(grades.values()) / len(grades)

def main():
    print("--- UBIT Student GPA Manager ---")
    data_file = 'student_data.json'
    
    # Load existing data
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            student_records = json.load(f)
    else:
        student_records = {}

    while True:
        print("\n1. Add Course & Grade")
        print("2. View All Grades & GPA")
        print("3. Save and Exit")
        
        choice = input("Select an option (1-3): ")

        if choice == '1':
            course = input("Enter course name: ")
            try:
                grade = float(input("Enter grade (e.g. 3.5): "))
                student_records[course] = grade
                print(f"Successfully added {course}!")
            except ValueError:
                print("Invalid input. Please enter a number for the grade.")

        elif choice == '2':
            if not student_records:
                print("No records found.")
            else:
                print("\n--- Current Transcript ---")
                for course, grade in student_records.items():
                    print(f"{course}: {grade}")
                gpa = calculate_gpa(student_records)
                print(f"Current GPA: {gpa:.2f}")

        elif choice == '3':
            with open(data_file, 'w') as f:
                json.dump(student_records, f)
            print("Data saved. Good luck with your studies!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()