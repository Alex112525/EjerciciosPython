class Student:
    __name = ""
    __email = ""
    __password = ""

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_pass(self, password):
        self.__password = password

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_pass(self):
        return self.__password
