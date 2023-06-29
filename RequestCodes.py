#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201


from StudRequest import StudRequest
def add_request(students, requests):
    admin_no = input("Enter Admin No: ")
    while search_valid_admin_no(students, admin_no) == False:
        print("Invalid Admin No. Please try again!")
        admin_no = input("Enter Admin No: ")
    request = input("Enter Request: ")
    while request.strip() == "":
        print("Invalid Request. Please try again!")
        request = input("Enter Request: ")
    requests.append(StudRequest(admin_no, request))
    print("Request added successfully!.")

def search_valid_admin_no(students, admin_no):
    last_index = len(students) - 1
    for i in range(len(students)):
        if students[i].get_admin_no() == admin_no or students[last_index-i].get_admin_no() == admin_no:
            return True
    return False

def search_student_by_admin_no(students, admin_no):
    last_index = len(students) - 1
    for i in range(len(students)):
        if students[i].get_admin_no() == admin_no or students[last_index-i].get_admin_no() == admin_no:
            return students[i]
    return None

def display_requests_no(requests):
    print("\nNumber of Requests: " + str(len(requests)))

def service_request(students, requests):
    if len(requests) == 0:
        print("No requests entered yet")
    else:
        print("")
        print("Display Student's Request:\n")
        print(search_student_by_admin_no(students, requests[0].get_admin_no()))
        print("-----------------------------")
        print("Request: " + requests[0].get_request())
        print("-----------------------------")
        requests.pop(0)
        print("\nRemaning requests: " + str(len(requests)))

    return requests
