from Student import Student

def display_students(students):
    if len(students) == 0:
        print("No students entered yet")

    else:
        for student in students:
            print(student)

def add_student(students):
    admin_no = input("Enter AdminNo: ")
    duplicate_found = False
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
    count = 1

    for i in range(n-1,0,-1):
        swapmade = False
        for j in range(i):
            if students[j].get_admin_no() < students[j+1].get_admin_no():
                tmp = students[j]
                students[j] = students[j+1]
                students[j+1] = tmp
                swapmade = True
        if swapmade == False:
            break
        print(" ")
        print(" ")
        print("Pass ",count)
        count += 1
        print("**********************************")
        for student in students:
            print("AdminNum: ", student.get_admin_no())

    print("")
    print("**************************************")
    print("Students sorted by Admin Number in descending order: ")
    display_students(students)

def insertion_sort_pem_group(students):
    n = len(students)
    count = 1
    for i in range(1, n):
        value = students[i]
        pos = i
        while pos > 0 and value.get_pem_group() < students[pos - 1].get_pem_group():
            students[pos] = students[pos - 1]
            pos -= 1
        students[pos] = value
        print("Pass ",count)
        count += 1
        print("**********************************")
        for student in students:
            print("PEM Group: ",student.get_pem_group())
    print("Students sorted by PEM Group in ascending order")
    display_students(students)

def populateData():
    studList = []
    newStudA = Student("2101252Y", "steve", "steve@mail.com",
    "2021", "IT2101")
    studList.append(newStudA)
    newStudA = Student("2121613Y", "strange", "tony@mail.com",
    "2021", "IT2103")
    studList.append(newStudA)
    newStudA = Student("2101122A", "peter", "peter@mail.com",
    "2021", "IT2101")
    studList.append(newStudA)
    newStudA = Student("2121623Y", "tony", "tony@mail.com", "2021",
    "IT2103")
    studList.append(newStudA)
    newStudA = Student("2121523Y", "banner", "banner@mail.com",
    "2021", "IT2102")
    studList.append(newStudA)
    newStudA = Student("2121563H", "clark", "clark@mail.com",
    "2021", "IT2102")
    studList.append(newStudA)
    newStudA = Student("2111025C", "bruce", "bruce@mail.com",
    "2021", "IT2102")
    studList.append(newStudA)
    print("Data populated!\n")
    return studList

def main():
    students = []
    while True:
        print("")
        print("*******************************")
        print("Student Management System Menu:")
        print("1. Display all students.")
        print("2. Add a new student.")
        print("3. Sort students by AdminNo in descending order.")
        print("4. Sort students by PEM Group in ascending order.")
        print("5. Exit.")
        print("9. Populate data")

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
        elif choice == '9':
            students = populateData()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
