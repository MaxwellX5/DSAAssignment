#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201


from Student import Student

#Question 4
def display_students(students,records_per_row):
    #Base case
    if not students:
        return
    #Recursive case
    else:
        #Split the list into 2 groups
        current_group = students[:records_per_row]
        remaining_group = students[records_per_row::]
        #Create lists to store the attributes of the students which will be displayed row by row
        admin_no_lst = []
        name_lst = []
        email_lst = []
        year_admitted_lst = []
        pem_lst = []
        #Populates the lists with the attributes of the students in the current group
        for student in current_group:
            admin_no_lst.append(student.get_admin_no())
            name_lst.append(student.get_student_name())
            email_lst.append(student.get_student_email())
            year_admitted_lst.append(student.get_year_admitted())
            pem_lst.append(student.get_pem_group())
        #Prints the attribute using python f string formatting
        print("")
        for no in admin_no_lst:
            print(f"Admin No: {no:<20}",end="")
        print("")

        for name in name_lst:
            print(f"Name: {name:<20}",end="    ")
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
        #Recursive call using the remaining group
        display_students(remaining_group,records_per_row)

#Part 1 of Assignment
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
