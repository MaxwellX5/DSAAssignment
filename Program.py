from Student import Student
students = []
s1 = Student("220261J","bob","lol",1111,"IT2021")

s2 = Student("221261J","John","lol",1111,"DSF2001")
s3 = Student("223261J","Don","lol",1111,"IT2001")
s4 = Student("224261J","Don3","lol",1111,"DAAA2001")
s5 = Student("225261J","Bruh","lol",1111,"DSF2021")
s6 = Student("261261J","urmom","lol",1111,"CIP2001")
s7 = Student("227261J","zzzg","lol",1111,"DAAA2021")
s8 = Student("229261J","aaaaaaaaaa","lol",1111,"CIP2021")
s9 = Student("231261J","Fred","lol",1111,"DBFT2001")
s10 = Student("201261J","Luck","lol",1111,"DBFT2021")
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
    duplicate = False
    for student in students:
        if admin_no == student.get_admin_no():
            duplicate_found = True
    while admin_no.strip() == "" or admin_no[-1].isalpha() == False or admin_no[0:-1].isdigit() == False or len(admin_no) != 7 or duplicate_found == True:
        if duplicate_found == True:
            print("AdminNo already exists")
        else:
            print("Invalid AdminNo")
        admin_no = input("Enter AdminNo: ")
        # Check for duplicate AdminNo
        duplicate_found = False
        for student in students:
            if admin_no == student.get_admin_no():
                duplicate_found = True
                break
        if duplicate_found:
            continue
        # If AdminNo is valid and not a duplicate, proceed


    name = input("Enter Student Name: ")
    while name.strip() == "" and name.isalpha() == False:
        print("Invalid name")
        name = input("Enter Student Name:")
    email = input("Enter Student Email: ")
    while "@" not in email or "." not in email:
        print("Invalid email. Student Email should be a valid email address.")
        email = input("Enter Student Email: ")

    year_admitted = (input("Enter Year Admitted: "))
    while not year_admitted.isdigit():
        print("Invalid year. Year Admitted should be a numeric value.")
        year_admitted = input("Enter Year Admitted: ")
    year_admitted = int(year_admitted)

    pem_group = input("Enter PEM Group: ")
    while pem_group.isalnum() == False:
        print("Invalid PEM Group. PEM Group should only contain alphanumeric characters.")
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
        print("")
        print("*******************************")
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
