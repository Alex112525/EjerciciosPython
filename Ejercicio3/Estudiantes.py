class Student:
    __name = ""
    __email = ""
    __password = ""

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

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

    def __str__(self):
        return f"Nombre: {self.__name}\n" \
               f"Email: {self.__email}\n" \
               f"Pasword: {self.__password}"
