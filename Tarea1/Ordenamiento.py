def Ordenamiento(lista):
    if tipos(lista):
        swap = True
        while swap:
            swap = False
            for i in reversed(range(1, len(lista))):
                if lista[i] < lista[i-1]:
                    lista[i], lista[i -1] = lista[i-1], lista[i]
                    swap = True
    return lista


def tipos(list):
    for x in list:
        if type(x) != type(list[0]):
            return False
    return True


if __name__ == "__main__":
    listanum = [4, 5, 2, 1, 3]
    listastr = ["Mia", "Alex", "Zara", "Pancho", "Rodrigo", "Paquito"]
    listafloat = [5.2, 2.4, 1.3, 9.8, 7.5, 3.4]

    listaordenada = Ordenamiento(listanum)
    print(listanum)

    listaordenada = Ordenamiento(listastr)
    print(listastr)

    listaordenada = Ordenamiento(listafloat)
    print(listafloat)
