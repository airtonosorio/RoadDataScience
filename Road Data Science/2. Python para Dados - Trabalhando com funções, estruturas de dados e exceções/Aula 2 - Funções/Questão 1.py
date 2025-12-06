#1. Escreva um código que lê a lista abaixo e faça:
#lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
#A leitura do tamanho da lista
#A leitura do maior e menor valor
#A soma dos valores da lista
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
tamanho = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)

print(f'A lista possui {tamanho}, o maior valor dela é {maior}, o menor valor é {menor} e a soma de todos os elementos é {soma}')