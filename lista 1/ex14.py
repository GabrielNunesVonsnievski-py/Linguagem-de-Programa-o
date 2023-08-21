lista = ["Gabriel","Luan","Guilherme","Kleiton"]
print(lista)
a = input(f"Digite algo da lista: ")
if a in lista:
    print(f"Esse item tem na lista e esta no index",a.index(a))