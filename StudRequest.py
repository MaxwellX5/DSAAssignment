#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201

class StudRequest():
    def __init__(self,admin_no, request):
        self.__admin_no = admin_no
        self.__request = request
    def get_admin_no(self):
        return self.__admin_no

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no

    def get_request(self):
        return self.__request

    def set_request(self, request):
        self.__request = request
