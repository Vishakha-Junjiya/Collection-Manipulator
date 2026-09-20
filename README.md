# ⭐ Student Data Organizer

[svg](https://github.com/Vishakha-Junjiya/student-management/blob/main/README.md#-student-data-organizer)

## 📌 Project Overview

[svg](https://github.com/Vishakha-Junjiya/student-management/blob/main/README.md#-project-overview)

The Student Data Organizer is a beginner-friendly Python project used to manage student information through a menu-driven program.

This project allows users to add, display, update, and delete student records. It also displays the subjects offered by the course.

The project demonstrates the practical use of Python fundamentals, including lists, dictionaries, loops, conditional statements, match-case, user input, type casting, and data manipulation.

## ✨ Features

[svg](https://github.com/Vishakha-Junjiya/student-management/blob/main/README.md#-features)

- 👨‍🎓 Add new student information.
- 📋 Display all student records.
- ✏️ Update student information.
- 🗑️ Delete student information.
- 📚 Display subjects offered.
- ⌨️ Take input from the user through the terminal.
- 🔄 Use a menu-driven program.
- 🚪 Exit the program when the user selects the exit option.

## 🐍 Python Concepts Used

[svg](https://github.com/Vishakha-Junjiya/student-management/blob/main/README.md#-python-concepts-used)

### 1. 📋 List

[svg](https://github.com/Vishakha-Junjiya/student-management/blob/main/README.md#1--list)

A list is used to store multiple student records in one place.

In this project, the `students` list stores student dictionaries.

```python
students = []

Student records are added to the list using the append() method.

students.append(student)
2. 📖 Dictionary

A dictionary stores data in key-value pairs.

In this project, each student record is stored as a dictionary.

student = {
    "id": student_id,
    "name": name,
    "age": age
}

The dictionary makes it easy to access student information using keys.

3. 🔁 While Loop

A while loop is used to repeatedly display the menu.

The menu continues until the user selects the exit option.

while True:
    print("1. Add student")
    print("2. Display all student")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")
4. 🔀 Match-Case Statement

The match-case statement is used to execute different blocks of code based on the user's choice.

match choice:
    case 1:
        print("Add student")
    case 2:
        print("Display all student")
    case 6:
        print("Exit")
5. ⌨️ User Input

The input() function is used to take information from the user.

This project takes student ID, name, age, and menu choice as input.

name = input("Enter student name: ")
6. 🔢 Type Casting

Type casting is used to convert input data from one data type to another.

In this project, student ID, age, and menu choice are converted into integers.

student_id = int(input("Enter student ID: "))
age = int(input("Enter student age: "))
7. ➕ Append Method

The append() method adds a new item to the end of a list.

In this project, it is used to add new student records.

students.append(student)
8. 🔍 Searching Data

Searching is used to find a particular student record from the list.

The program checks the student name or student ID to find the required record.

for student in students:
    if student["name"] == name:
        print(student)
9. ✏️ Updating Data

Updating means changing existing information.

In this project, the student ID, name, or age can be updated.

student["age"] = new_age
10. 🗑️ Deleting Data

Deleting means removing an existing student record from the list.

The remove() method can be used to delete a student dictionary.

students.remove(student)
11. 📚 List of Subjects

A list is also used to store the subjects offered by the course.

subjects = [
    "Math",
    "Science",
    "English",

]
📁 Project Structure

svg

project_3/
│
├── Collection-Manipulator.py
├── student_management.png
└── README.md
Collection-Manipulator.py – Main Python program used to manage student records.
student_management.png – Output screenshot of the program.
README.md – Project documentation and information.
🔄 Program Workflow

svg

👋 Display the welcome message.
📋 Display the menu.
👨‍🎓 Add student information.
📄 Display all student records.
✏️ Update student information.
🗑️ Delete student information.
📚 Display the subjects offered.
🚪 Exit the program when the user selects option 6.
👨‍🎓 Adding Student Information

The user enters the student ID, name, and age.

The program stores the information in a dictionary and adds it to the students list.

Example:

Enter student ID: 101
Enter student name: Vishakha
Enter student age: 20

Student added successfully.
📋 Displaying Student Information

The program displays all student records stored in the list.

Example:

Student ID: 101
Student Name: Vishakha
Student Age: 20
✏️ Updating Student Information

The update option allows the user to change existing student information.

For example, the student age can be updated from 20 to 21.

Enter student name: Vishakha
Enter new age: 21

Student information updated successfully.
🗑️ Deleting Student Information

The delete option removes a student record from the list.

Enter student name: Vishakha

Student deleted successfully.
📚 Display Subjects Offered

The program displays the subjects offered by the course.

Example:

Subjects Offered:

1.Math
2.Science
3.English

💻 Example Output
Welcome to the Student Data Organizer!

1. Add student
2. Display all student
3. Update student information
4. Delete student
5. Display subjects offered
6. Exit

Enter your choice: 1

Enter student ID: 101
Enter student name: Vishakha
Enter student age: 20

Student added successfully.

Enter your choice: 2

Student ID: 101
Student Name: Vishakha
Student Age: 20

Enter your choice: 5

Subjects Offered:
Math
Science
English


Enter your choice: 6

Exiting the program...
🎓 Learning Outcomes

After completing this project, I learned how to:

📋 Store multiple records using lists.
📖 Store structured data using dictionaries.
🔁 Use while loops.
🔀 Use match-case statements.
⌨️ Take input from the user.
🔢 Convert input using type casting.
✏️ Update existing records.
🗑️ Delete records from a list.
🔍 Search for specific student information.
📚 Store and display subjects.
💻 Build a menu-driven Python program.
🛠️ Technologies Used
🐍 Python 3
💻 Visual Studio Code
🐙 GitHub
👩‍💻 Author

Vishakha Junjiya

🎓 BCA Student | 🐍 Python Learner

📂 Project Information

Project Name: Student Data Organizer

Language: Python

Level: Beginner

Purpose: Python Fundamentals Practice

Project Type: Menu-Driven Program

🖼️ Project Output

Student Data Organizer Output

🏁 Conclusion

This project helped me understand how to manage student records using Python lists and dictionaries.

It also improved my understanding of loops, match-case statements, user input, type casting, updating, and deleting data.

The Student Data Organizer is part of my Python learning journey and portfolio.
The Student Data Organizer is part of my Python learning journey and portfolio.
