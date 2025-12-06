'''Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores.
 Deixe claro que o valor do denominador não pode ser 0.'''

num1 = int(input('Digite um número para ser o númerador da divisão: '))
num2 = int(input('Digite um número para o denominador da divisão (não pode ser 0): '))
if (num2 == 0) :
    print('Não pode ser igual a 0')
rest = num1 % num2
print(f'O resto da divisão é {rest}')