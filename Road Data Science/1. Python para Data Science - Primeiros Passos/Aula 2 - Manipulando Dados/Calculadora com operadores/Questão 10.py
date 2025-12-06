'''Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.'''

num1 = 5
peso1 = 1

num2 = 12
peso2 =2

num3 = 20
peso3 = 3

num4 = 15
peso4 = 4

mediaf = (peso1 + peso2 + peso3 + peso4)

media = (num1*peso1 + num2*peso2 + num3*peso3 + num4*peso4) / mediaf
print(f'A média é {media}')