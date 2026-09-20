print("Welcome to the Student Data Organizer!")

students = []
student_data = {}

subjects_offered = {
    "Math",
    "Science",
    "English"
}

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEnter student details:")

        student_id = int(input("Student ID: "))

        if student_id in student_data:
            print("Student ID already exists!")
            continue

        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")

        print("\nAvailable Subjects:")
        print("1. Math")
        print("2. Science")
        print("3. English")

        subject_choice = input(
            "Enter subject numbers (comma-separated): "
        )

        selected_subjects = set()

        for number in subject_choice.split(","):
            number = number.strip()

            if number == "1":
                selected_subjects.add("Math")
            elif number == "2":
                selected_subjects.add("Science")
            elif number == "3":
                selected_subjects.add("English")
            else:
                print("Invalid subject selected!")
        
        if not selected_subjects:
            print("No valid subject selected!")
            continue

        student_identity = (student_id, dob)

        student = {
            "identity": student_identity,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": selected_subjects
        }

        students.append(student)

        student_data[student_id] = student

        print("Student added successfully!")

    elif choice == 2:
        if not students:
            print("No students found!")
        else:
            print("\n--- Display All Students ---")

            for student in students:
                student_id, dob = student["identity"]

                subject_list = ", ".join(
                    sorted(student["subjects"])
                )

                print(
                    f"Student ID: {student_id} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Grade: {student['grade']} | "
                    f"Date of Birth: {dob} | "
                    f"Subjects: {subject_list}"
                )

    elif choice == 3:
        student_id = int(
            input("Enter ID you want to update: ")
        )

        if student_id in student_data:
            student = student_data[student_id]

            name = input("Update name: ")
            age = int(input("Update age: "))
            grade = input("Update grade: ")

            student["name"] = name
            student["age"] = age
            student["grade"] = grade

            print("Student information updated successfully!")

        else:
            print("Student not found!")

    elif choice == 4:
        student_id = int(
            input("Enter student ID to delete: ")
        )

        if student_id in student_data:
            student = student_data[student_id]

            students.remove(student)

            del student_data[student_id]

            print("Student deleted successfully!")

        else:
            print("Student not found!")

    elif choice == 5:
        print("\nSubjects Offered:")

        for subject in sorted(subjects_offered):
            print(subject)

    elif choice == 6:
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")