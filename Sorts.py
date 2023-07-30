from StudentCodes import display_students

#Part 1 of Assignment
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

#Part 1 of Assignment
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

#Question 1
#Adapted from https://www.geeksforgeeks.org/sorting-algorithm-slightly-improves-selection-sort/
#Adapted by using a for loop instead of a while loop. The original code loops until the counter at the front and back meet.
#Mine will loop for half the length of the list (Same as reaching middle)
#As 2 elements are sorted in the list per pass (Unless the elements are already in the correct place), the number of passes is n//2
def selection_sort_name(students,records_per_row):
    n = len(students)
    #Number of passes is n//2 and not n-1 as this is optimised selection sort
    for i in range(n//2):
        smallNdx = i
        largeNdx = i
        for j in range(i+1, n-i):
            if students[j].get_student_name() < students[smallNdx].get_student_name():
                smallNdx = j
            if students[j].get_student_name() > students[largeNdx].get_student_name():
                largeNdx = j
        if smallNdx != i:
            students[i], students[smallNdx] = students[smallNdx], students[i]

        #Handles case where largeNdx was previously at i and the element at largeNdx was swapped with the element at smallNdx
        if largeNdx == i:
            largeNdx = smallNdx

        #Swap the last element in the list with the element at largeNdx if largeNdx is not already the last element in the loop
        if largeNdx != n-i-1:
            students[n-i-1], students[largeNdx] = students[largeNdx], students[n-i-1]
        print("**********************************")
        print("Pass ",i+1)
        print("**********************************")
        for student in students:
            print("Name: ",student.get_student_name())

    display_students(students,records_per_row)

#Question 2
#Optimised merge sort (See below)
def merge_sort_pem_group_admin_no(students):
    #Base case
    if len(students) <= 1:
        return students
    #Recursive case
    else:
        #Find the midpoint of the list to divide the list into two halves
        mid = len(students) // 2
        #Call the function again for the left and right halves to divide the list into smaller lists until the base case is reached
        left = merge_sort_pem_group_admin_no(students[:mid])
        right = merge_sort_pem_group_admin_no(students[mid:])

        '''
        https://www.geeksforgeeks.org/make-mergesort-perform-comparisons-best-case/
        Makes the time complexity for best case O(n) compared to  O(n log n) for the normal implementation of merge sort.
        The mergelists function will only be called when the left list and right list of that particular call of merge_sort_pem_group_admin_no are not sorted.
        This reduces the number of calls for mergelists making the code more efficient.
        For example, when doing merge sort for [1,2,3,4,8,7,6,5], the mergelists function wont get called for the left half.
        '''

        #Call mergelists function to merge the lists if the lists are not sorted
        if left[-1].get_pem_group() > right[0].get_pem_group():
            newlst = mergelists(left, right)
            return newlst

        #Call mergelists function to merge the lists if the lists are not sorted when pem group is the same but admin_no is not sorted
        elif left[-1].get_pem_group() == right[0].get_pem_group() and left[-1].get_admin_no() > right[0].get_admin_no():
            newlst = mergelists(left, right)
            return newlst
        #Skips the need to call the mergelists function as it is already sorted
        else:
            return left + right

def mergelists(left,right):
    #Create a new list to store the merged list
    lst = list()
    leftpointer = 0
    rightpointer = 0
    #Loop through the lists and compare the first element of each list. Loops until either list is empty
    while leftpointer < len(left) and rightpointer < len(right):
        #Compares the pem group of the first element of the 2 lists.

        #If the pem group of the leftpointer'th element of the left list is smaller than the rightpointer'th element of the right list,
        #append the leftpointer'th element of the left list to the new list and increase the leftpointer by 1
        if left[leftpointer].get_pem_group() < right[rightpointer].get_pem_group():
            lst.append(left[leftpointer])
            leftpointer += 1
        #If the pem group of the rightpointer'th element of the right list is smaller than the leftpointer'th element of the left list,
        #append the rightpointer'th element of the right list to the new list and increase the rightpointer by 1
        elif right[rightpointer].get_pem_group() < left[leftpointer].get_pem_group():
            lst.append(right[rightpointer])
            rightpointer += 1
        #If the pem group of the first element of both lists are the same,
        #compare the admin number of the leftpointer'th element of the left lists and the rightpointer'th element of the right list
        #Increase the counter of whichever counter's element is smaller by 1 and append that element to the new list
        else:
            if left[leftpointer].get_admin_no() < right[rightpointer].get_admin_no():
                lst.append(left[leftpointer])
                leftpointer += 1
            else:
                lst.append(right[rightpointer])
                rightpointer += 1

    #Append the remaining elements of the list that is not empty to the new list
    while leftpointer < len(left):
        lst.append(left[leftpointer])
        leftpointer += 1
    while rightpointer < len(right):
        lst.append(right[rightpointer])
        rightpointer += 1

    print("New List: ")
    print("---------------------")
    for student in lst:
        print(student.get_admin_no(),student.get_pem_group())
    print("---------------------")
    return lst
