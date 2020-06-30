from mongoengine import *
connect("padts")

class Student(Document):
    name = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50)
    password = StringField(required=True,max_length=10)

    def getName(self):
        return self.name

    def __str__(self):
        return f"Nombre: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Pasword: {self.password}"


def addStudent(student):
    student.save()


def readStudent(name):
    for st in Student.objects:
        if st.name == name:
            return st
    return False


def updateStudent(name, nname=None, email=None, password=None):
    ust = readStudent(name)
    if ust:
        if nname != None:
            ust.name = nname
        if email != None:
            ust.email = email
        if password != None:
            ust.password = password
        ust.save()
        return ust
    else:
        return "El estudiante no esta en la base de datos "


def deleteStudent(name):
    dst = readStudent(name)
    if dst:
        dst.delete()
    else:
        print("Estudiante no encontrado")

    return Student.objects


def getAll():
    return Student.objects
