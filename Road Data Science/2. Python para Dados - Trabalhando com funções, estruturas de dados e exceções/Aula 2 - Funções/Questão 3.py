#Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

mult_3 = []

def multiplo_3(lista: list) -> list:
    for i in range(len(lista)):
        if lista[i] % 3 == 0:
            mult_3.append(lista[i])
    return mult_3

mult_3 = multiplo_3(lista)
print(mult_3)
