from Ejercicio3 import Estudiantes as st
from random import random
from Tarea3.StudentIO import TPickle as Pic
from Tarea3.StudentIO import TShelve as Shel

names = ["Alex", "Alina", "Lalo", "Gaby", "Manu"]
emails = [x+"@scinvestav.com" for x in names]
passwords = [x+str(int(random()*10000)) for x in names]
students_list = list()

for n, e, p in zip(names, emails, passwords):
    students_list.append(st.Student(n, e, p))

Pic.save_pickle(students_list)
Shel.save_shelve(students_list)

Pic.update_pickle("Alina", "Pancha", "pancha2@gmail.com")
Pic.update_pickle("Pancho")

Shel.update_shelve("Alina", "Panchita", "panchita2@gmail.com")

stshelve = Shel.load_shelve()
stpickle = Pic.load_pickle()

