# Add student
students = []

#Function to add a new student
def add_student():
    student_id = input("Enter the student_id >>")
    name = input("Enter the Student Name >>")
    Age = int(input("Enter the Student Age >>"))
    Course = input("Enter the student Course >>")

    # Creating a Student Dictionary
    student ={
        "ID":student_id,
        "Name":name,
        "Age":Age,
        "Course":Course
    }

    #Adding student to the list
    students.append(student)
    print(f"Student {name} added successfully")


# View Function
def View_student():
    if not students:
        print("No Student found")
        return
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student["ID"]}, Name: {student["Name"]}, Age: {student["Age"]}, Course: {student["Course"]}")

# Remove_Student function
def Remove_Student():
    student_id = input("Enter the student_id to Remove >>")
    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print(f"student {student["Name"]} removed Successfully.")
            return
    print("Student not found")


#upadate student function
def update_student():
    student_id = input("Enter student ID to Upadate >>")
    for student in students:
        if student["ID"] == student_id:
            print("1. Upadate Name >>")
            print("2. Upadate Age >>")
            print("3. Upadate Course >>")
            choice = input("Enter choice")

            if choice == "1":
                new_name = input("Enter the new name >>")
                student["Name"] = new_name

            elif choice == "2":
                new_age = input("Enter the new Age >>")
                student["Age"] = new_age

            elif choice == "3":
                new_course = input("Enter the new Course >>")
                student["Course"] = new_course

            else:
                print("Invalid choice:")
            print("Studen information upadted successfully")
            return
    print("Student not found")


# Search function
def Search_Student():
    student_id = input("Enter the student_id to Search >>")
    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print(f" Student Found: ID: {student["ID"]}, Name: {student["Name"]}, Age: {student["Age"]}, Course: {student["Course"]}")
            return
    print("Student not found")

# Main loop to run the program
def main():
    while True:
        print("\n-----Student Management System------")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Upadate Student Information")
        print("4. View all Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2" :
            Remove_Student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            View_student()

        elif choice == "5":
            Search_Student()

        elif choice == "6":
            print("Exiting the program")
            break
        
        else:
            print("Invalid choice ! please try again.")
main()