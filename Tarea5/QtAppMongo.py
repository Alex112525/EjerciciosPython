from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot
from Tarea5.StudentWindow import Ui_MainWindow
from Tarea4.Estudiantes import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle('StudentApp')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Updatecombobox()

        self.ui.Add_student.clicked.connect(self.add_student)
        self.ui.Del_student.clicked.connect(self.del_student)
        self.ui.Show_student.clicked.connect(self.show_student)
        self.ui.Up_student.clicked.connect(self.update_student)

    @Slot()
    def update_student(self):
        self.ui.Text.clear()
        name = self.ui.Student_list.currentText()
        nname=self.ui.Name_edit.text()
        email=self.ui.Email_edit.text()
        password=self.ui.Pass_edit.text()
        if name:
            if nname and email and password:
                student = readStudent(name)
                self.ui.Text.append(student.__str__())
                nstudent = updateStudent(name, nname, email, password)
                self.ui.Text.append("Estudiante Actualizado a: ")
                self.ui.Text.append(nstudent.__str__())
                self.Updatecombobox()
            else:
                self.ui.Text.append("Llene los campos a actualizar")


    @Slot()
    def show_student(self):
        self.ui.Text.clear()
        name = self.ui.Student_list.currentText()
        student = readStudent(name)
        self.ui.Text.append(student.__str__())

    @Slot()
    def del_student(self):
        self.ui.Text.clear()
        name = self.ui.Student_list.currentText()
        if name:
            student = readStudent(name)
            self.ui.Text.append("Estudiante Eliminado: ")
            self.ui.Text.append(student.__str__())
            deleteStudent(name)
            self.Updatecombobox()

    @Slot()
    def add_student(self):
        self.ui.Text.clear()
        name=self.ui.Name_edit.text()
        email=self.ui.Email_edit.text()
        password=self.ui.Pass_edit.text()
        if name and email and password:
            student = Student(name=name, email=email, password=password)
            print(student)
            addStudent(student)
            self.ui.Text.append("Estudiante Añadido: ")
            self.ui.Text.append(student.__str__())
            self.Updatecombobox()
        else:
            self.ui.Text.append("Llene todos los campos")

    def Updatecombobox(self):
        self.ui.Student_list.clear()
        list_students = getAll()
        for st in list_students:
            self.ui.Student_list.addItem(st.getName())


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()
