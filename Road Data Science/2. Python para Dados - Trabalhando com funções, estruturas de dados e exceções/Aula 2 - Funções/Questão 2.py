#Escreva uma função que gere a tabuada de um número inteiro de 1 a 10,
#de acordo com a escolha da pessoa usuária.
num = int(input("Digite um número inteiro de 1 a 10:"))

def tabuada(num: int):
  print(f'Tabuada do {num}:')
  for i in range(11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

tabuada(num)