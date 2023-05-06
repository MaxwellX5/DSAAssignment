from Student import Student
students = []

def display_students(students):
    for student in students:
        print(student)

def add_student(students):
    admin_no = input("Enter AdminNo: ")
    name = input("Enter Student Name: ")
    email = input("Enter Student Email: ")
    year_admitted = int(input("Enter Year Admitted: "))
    pem_group = input("Enter PEM Group: ")
    student = Student(admin_no,name,email,year_admitted,pem_group)
    students.append(student)

def bubble_sort_admin_no(students):
    n = len(students)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if students[j].get_admin_no() < students[j+1].get_admin_no():
                tmp = students[j]
                students[j] = students[j+1]
                students[j+1] = tmp
    print("Students sorted by Admin Number in descending order: ")
    display_students(students)

def main():
    while True:
        print("Student Management System Menu:")
        print("1. Display all students.")
        print("2. Add a new student.")
        print("3. Sort students by AdminNo in descending order.")
        print("4. Sort students by PEM Group in ascending order.")
        print("5. Exit.")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_students(students)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            bubble_sort_admin_no(students)
        elif choice == '4':
            sort_by_pem_group(students)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
