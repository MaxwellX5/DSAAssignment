#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201


from Student import Student
from RequestCodes import*
from Queue import Queue

def display_students(students,records_per_row):
    if not students:
        return
    else:
        current_group = students[:records_per_row]
        remaining_group = students[records_per_row::]
        admin_no_lst = []
        name_lst = []
        email_lst = []
        year_admitted_lst = []
        pem_lst = []
        for student in current_group:
            admin_no_lst.append(student.get_admin_no())
            name_lst.append(student.get_student_name())
            email_lst.append(student.get_student_email())
            year_admitted_lst.append(student.get_year_admitted())
            pem_lst.append(student.get_pem_group())
        for no in admin_no_lst:
            print(f"Admin No: {no:<20}",end="")
            # print(f"{attributes[i]:<20}{attribute_value:<20}", end="")
            # print("")
            # print("Admin No: ",no:<20)


        print("")
        for name in name_lst:
            print(f"Name: {name:<20}",end="    ")
            # print("Name: ",name,end="          ")
        print("")
        for email in email_lst:
            print(f"Email: {email:<20}",end="   ")
        print("")
        for year in year_admitted_lst:
            print(f"Year: {year:<20}",end="    ")
        print("")
        for pem in pem_lst:
            print(f"PEM: {pem:<20}",end="     ")
        print("")
        print("")
        display_students(remaining_group,records_per_row)


def print_student_record(student):
    print("Admin No:", student.get_admin_no())
    print("Name:", student.get_student_name())
    print("Email:", student.get_student_email())
    print("Year Admitted:", student.get_year_admitted())
    print("PEM:", student.get_pem_group())

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

def bubble_sort_admin_no(students,records_per_row):
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
        if swapmade == False and count == 1:
            print("Pass ",count)
            for student in students:
                print("AdminNum: ",student.get_admin_no())
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
    display_students(students,records_per_row)

def insertion_sort_pem_group(students,records_per_row):
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
    print("")
    print("Students sorted by PEM Group in ascending order")
    display_students(students, records_per_row)

def selection_sort_name(students,records_per_row):
    n = len(students)
    #Number of passes is n//2 and not n-1 as this is optimised selection sort
    for i in range(n//2):
        smallNdx = i
        largeNdx = i
        for j in range(i+1, n-1):
            if students[j].get_student_name() < students[smallNdx].get_student_name():
                smallNdx = j
            elif students[j].get_student_name() > students[largeNdx].get_student_name():
                largeNdx = j
        if smallNdx != i:
            students[i], students[smallNdx] = students[smallNdx], students[i]

        #Handles case where largeNdx was previously at i and the element at largeNdx was swapped with the element at smallNdx
        if largeNdx == i:
            largeNdx = smallNdx

        #Swap the last element in the list with the element at largeNdx if largeNdx is not already the last element in the loop
        if largeNdx != n-i-1:
            students[n-i-1], students[largeNdx] = students[largeNdx], students[n-i-1]

    display_students(students,records_per_row)

def merge_sort_pem_group_admin_no(students):
    if len(students) <= 1:
        return students
    else:
        mid = len(students) // 2
        left = merge_sort_pem_group_admin_no(students[:mid])
        right = merge_sort_pem_group_admin_no(students[mid:])
        newlst = mergelists(left, right)
        return newlst
def mergelists(left,right):
    lst = []
    while len(left) > 0 and len(right) > 0:
        if left[0].get_pem_group() < right[0].get_pem_group():
            lst.append(left[0])
            left.pop(0)
        elif right[0].get_pem_group() < left[0].get_pem_group():
            lst.append(right[0])
            right.pop(0)
        else:
            if left[0].get_admin_no() < right[0].get_admin_no():
                lst.append(left[0])
                left.pop(0)
            else:
                lst.append(right[0])
                right.pop(0)
    while len(left) > 0:
        lst.append(left[0])
        left.pop(0)
    while len(right) > 0:
        lst.append(right[0])
        right.pop(0)

    print("New List: ")
    print("---------------------")
    for student in lst:
        print(student.get_admin_no())
    print("---------------------")
    return lst


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
    requests = Queue()
    records_per_row = 1
    requestmenu = False
    while True:
        if requestmenu == True:
            print("")
            print("*******************************")
            print("Student's Request Page: ")
            print("1. Enter Student's Request.")
            print("2. View Number of Requests.")
            print("3. Service next in Queue.")
            print("0. Return to Main Menu.")

        elif requestmenu == False:
            print("")
            print("*******************************")
            print("Student Management System Menu:")
            print("1. Display all students.")
            print("2. Add a new student.")
            print("3. Sort students by AdminNo in descending order.")
            print("4. Sort students by PEM Group in ascending order.")
            print("5. Sort students by Name in ascending order.")
            print("6. Sort students via Merge sort on PEM Group follwed by Admin Number in ascending order. ")
            print("7. Enter Students' request.")
            print("8. Set number of records per row to display.")
            print("0. Exit.")
            print("9. Populate data")

        if requestmenu == False:
            choice = input("Enter your choice (0-9): ")
            if choice == '1':
                display_students(students, records_per_row)
            elif choice == '2':
                add_student(students)
            elif choice == '3':
                bubble_sort_admin_no(students, records_per_row)
            elif choice == '4':
                insertion_sort_pem_group(students, records_per_row)
            elif choice == '5':
                selection_sort_name(students, records_per_row)
            elif choice == '6':
                display_students(merge_sort_pem_group_admin_no(students), records_per_row)
            elif choice == '7':
                requestmenu = True
            elif choice == '8':
                records_per_row = (input("Enter number of records per row to display: "))
                while records_per_row.isdigit() == False:
                    records_per_row = (input("Enter number of records per row to display: "))
                records_per_row = int(records_per_row)

            elif choice == '0':
                print("Exiting the program.")
                break
            elif choice == '9':
                students = populateData()
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")

        else:
            choice = input("Enter your choice (0-3): ")
            if choice == '1':
                add_request(students,requests)
            elif choice == '2':
                display_requests_no(requests)
            elif choice == '3':
                service_request(students,requests)
            elif choice == '0':
                requestmenu = False
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")


if __name__ == '__main__':
    main()
