'''Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.'''

frase = str(input('Digite uma frase para ser retirada o espaço em branco no início e no fim, e além disso também seja totalmente em minúsculo: '))
frase.strip().lower()