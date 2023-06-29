#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201
class Student:
    def __init__(self,admin_no,student_name,student_email,year_admitted,pem_group):
        self.__admin_no = admin_no
        self.__student_name = student_name
        self.__student_email = student_email
        self.__year_admitted = year_admitted
        self.__pem_group = pem_group

    def get_admin_no(self):
        return self.__admin_no

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no

    def get_student_name(self):
        return self.__student_name

    def set_student_name(self, student_name):
        self.__student_name = student_name

    def get_student_email(self):
        return self.__student_email

    def set_student_email(self, student_email):
        self.__student_email = student_email

    def get_year_admitted(self):
        return self.__year_admitted

    def set_year_admitted(self, year_admitted):
        self.__year_admitted = year_admitted

    def get_pem_group(self):
        return self.__pem_group

    def set_pem_group(self, pem_group):
        self.__pem_group = pem_group

    def __str__(self):
        s = "-----------------------------\nAdmin No: {}\nStudent Name: {}\nStudent Email: {}\nYear Admitted: {}\nPEM Group: {}".format(self.get_admin_no(), self.get_student_name(), self.get_student_email(), self.get_year_admitted(), self.get_pem_group())
        return s
