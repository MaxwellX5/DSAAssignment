#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201


from StudRequest import StudRequest
from Queue import Queue

#Question 3a
def add_request(students, requests):
    admin_no = input("Enter Admin No: ")
    #Checks if the admin_no given is valid
    while search_valid_admin_no(students, admin_no) == False:
        print("Invalid Admin No. Please try again!")
        admin_no = input("Enter Admin No: ")
    request = input("Enter Request: ")
    #Checks if the request given is valid
    while request.strip() == "":
        print("Invalid Request. Please try again!")
        request = input("Enter Request: ")
    #Creates a request object and adds that object to the queue
    requests.enqueue(StudRequest(admin_no, request))
    print("Request added successfully!")

#Question 3a
#Sequential search to check if admin_no given exists in the list of students
def search_valid_admin_no(students, admin_no):
    last_index = len(students) - 1
    for i in range(len(students)):
        if students[i].get_admin_no() == admin_no or students[last_index-i].get_admin_no() == admin_no:
            return True
    return False

#Question 3c
#Sequential search to return the student object that belongs to the admin_no given
def search_student_by_admin_no(students, admin_no):
    last_index = len(students) - 1
    for i in range(len(students)):
        if students[i].get_admin_no() == admin_no:
            return students[i]
        elif students[last_index-1].get_admin_no() == admin_no:
            return students[last_index-1]
    return None

#Question 3b
def display_requests_no(requests):
    print("\nNumber of Requests: " + str(requests.size()))


#Question 3c
def service_request(students,requests):
    if requests.isEmpty():
        print("No requests entered yet")
    else:
        print("")
        print("Display Student's Request:")
        #Displays the student details of the student who made the request
        request = requests.dequeue()
        print(search_student_by_admin_no(students, request.get_admin_no()))
        print("-----------------------------")
        #Remove the request from the queue and displays the request
        print("Request: "+request.get_request())
        print("-----------------------------")
        print("\nRemaining requests: " + str(requests.size()))

    return requests
