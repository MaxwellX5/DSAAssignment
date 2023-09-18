from Queue import Queue
from Student import Student
from StudRequest import StudRequest
from StudentCodes import display_students, add_student
from RequestCodes import display_requests_no, service_request, add_request, search_valid_admin_no
from Sorts import bubble_sort_admin_no, insertion_sort_pem_group, selection_sort_name, merge_sort_pem_group_admin_no


def populateStudentData():
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

'''Populate requests function (Use if you want to)'''
# def populateRequestData(students):
#     requestList = Queue()
#     #Testing the search_valid_admin_no function
#     print("Testing Admin number that doesnt exist in student list: 2212451D", search_valid_admin_no(students,"2212451D"))
#     print("Does admin number 2101252Y exist in students list?", search_valid_admin_no(students,"2101252Y"))
#     print(requestList.dequeue())
#     #Adding requests with admin numbers that exist in the student list
#     newRequest1 = StudRequest("2101252Y", "I need help with my assignment")
#     requestList.enqueue(newRequest1)
#     newRequest2 = StudRequest("2121613Y", "I need help with my project")
#     requestList.enqueue(newRequest2)
#     return requestList

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
            print("6. Sort students via Merge sort on PEM Group followed by Admin Number in ascending order. ")
            print("7. Enter Students' request.")
            print("8. Set number of records per row to display.")
            print("0. Exit.")
            print("9. Populate data")

        if requestmenu == False:
            choice = input("Enter your choice (0-9): ")
            if choice == '1':
                if len(students) == 0:
                    print("No student records to display.")
                else:
                    display_students(students, records_per_row)
            elif choice == '2':
                add_student(students)
            elif choice == '3':
                if len(students) == 0:
                    print("No student records to sort.")
                else:
                    bubble_sort_admin_no(students, records_per_row)
            elif choice == '4':
                if len(students) == 0:
                    print("No student records to sort.")
                else:
                    insertion_sort_pem_group(students, records_per_row)
            elif choice == '5':
                if len(students) == 0:
                    print("No student records to sort.")
                else:
                    selection_sort_name(students, records_per_row)
            elif choice == '6':
                if len(students) == 0:
                    print("No student records to sort.")
                else:
                    students = merge_sort_pem_group_admin_no(students)
                    display_students(students,records_per_row)
            elif choice == '7':
                requestmenu = True
            elif choice == '8':
                records_per_row = (input("Enter number of records per row to display: "))
                while records_per_row.isdigit() == False:
                    print("Please enter a valid number.")
                    records_per_row = (input("Enter number of records per row to display: "))
                records_per_row = int(records_per_row)
                #Prevents recursion error
                if records_per_row < 1:
                    records_per_row = 1

            elif choice == '0':
                print("Exiting the program.")
                break
            elif choice == '9':
                students = populateStudentData()
                #Uncomment if you want to use it (Uncomment the populateRequestData function too)
                #requests = populateRequestData(students)
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")

        else:
            choice = input("Enter your choice (0-3): ")
            if choice == '1':
                if len(students) == 0:
                    print("Cannot add requests if there are no students in records")
                else:
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
