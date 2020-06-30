import shelve


def save_shelve(list_students):
    with shelve.open("students_shelve") as st:
        st["lista"] = list_students


def load_shelve():
    with shelve.open("students_shelve") as st:
        list_students = st["lista"]
    return list_students


def update_shelve(name, nname=None, nemail=None, npass=None):
    ls = load_shelve()
    found = False
    for i, student in enumerate(ls):
        if student.get_name() == name:
            found = True
            if nname:
                student.set_name(nname)
            if nemail:
                student.set_email(nemail)
            if npass:
                student.set_pass(npass)
            break
    if found:
        save_shelve(ls)
    else:
        print("Estudiante {} no encontrado".format(name))
