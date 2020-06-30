from Tarea4 import Estudiantes as st
from random import random

names = ["Alex", "Alina", "Lalo", "Gaby", "Manu"]
emails = [x+"@scinvestav.com" for x in names]
passwords = [x+str(int(random()*10000)) for x in names]

for n, e, p in  zip(names, emails, passwords):
    student = st.Student(name=n, email=e, password=p)
    st.addStudent(student)

st1 = st.readStudent("Alina")
print(st1)

st.updateStudent("Manu", "Mani", "Mani@cinvestav.com", "Mani1234")

listst= st.deleteStudent("Lalo")
for st in listst:
    print(st)


