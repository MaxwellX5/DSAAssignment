from Student import Student
students = []
s1 = Student(1,"bob","lol",1111,"IT2021")

s2 = Student(4,"John","lol",1111,"DSF2001")
s3 = Student(2,"Don","lol",1111,"IT2001")
s4 = Student(9,"Don3","lol",1111,"DAAA2001")
s5 = Student(7,"Bruh","lol",1111,"DSF2021")
s6 = Student(10,"urmom","lol",1111,"CIP2001")
s7 = Student(5,"Ben","lol",1111,"DAAA2021")
s8 = Student(8,"Matt","lol",1111,"CIP2021")
s9 = Student(3,"Fred","lol",1111,"DBFT2001")
s10 = Student(6,"Luck","lol",1111,"DBFT2021")
students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)
students.append(s5)
students.append(s6)
students.append(s7)
students.append(s8)
students.append(s9)
students.append(s10)

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
    for i in range(n-1,0,-1):
        for j in range(i):
            if students[j].get_admin_no() < students[j+1].get_admin_no():
                tmp = students[j]
                students[j] = students[j+1]
                students[j+1] = tmp
    print("Students sorted by Admin Number in descending order: ")
    display_students(students)

def insertion_sort_pem_group(students):
    n = len(students)
    for i in range(1, n):
        value = students[i]
        pos = i
        while pos > 0 and value.get_pem_group() < students[pos - 1].get_pem_group():
            students[pos] = students[pos - 1]
            pos -= 1
        students[pos] = value
    print("Students sorted by PEM Group in ascending order")
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
            insertion_sort_pem_group(students)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
