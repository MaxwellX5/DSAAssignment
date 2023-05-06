class Student:
    def __init__(self,admin_no,student_name,student_email,year_admitted,pem_group):
        self.admin_no = admin_no
        self.student_name = student_name
        self.student_email = student_email
        self.year_admitted = year_admitted
        self.pem_group = pem_group

    def get_admin_no(self):
        return self.admin_no

    def set_admin_no(self, admin_no):
        self.admin_no = admin_no

    def get_student_name(self):
        return self.student_name

    def set_student_name(self, student_name):
        self.student_name = student_name

    def get_student_email(self):
        return self.student_email

    def set_student_email(self, student_email):
        self.student_email = student_email

    def get_year_admitted(self):
        return self.year_admitted

    def set_year_admitted(self, year_admitted):
        self.year_admitted = year_admitted

    def get_pem_group(self):
        return self.pem_group

    def set_pem_group(self, pem_group):
        self.pem_group = pem_group

    def __str__(self):
        s = "AdminNo: {}, Student Name: {}, Student Email: {}, Year Admitted: {}, PEM Group: {}".format(self.get_admin_no(), self.get_student_name(), self.get_student_email(), self.get_year_admitted(), self.get_pem_group())
        return s
