import pickle


def save_pickle(list_students):
    file = open("Students.txt", 'wb')
    pickle.Pickler(file).dump(list_students)
    file.close()


def load_pickle():
    file = open("Students.txt", 'rb')
    list_students = pickle.Unpickler(file)
    list_s = list_students.load()
    file.close()
    return list_s


def update_pickle(name, nname=None, nemail=None, npass=None):
    ls = load_pickle()
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
        save_pickle(ls)
    else:
        print("Estudiante {} no encontrado".format(name))

