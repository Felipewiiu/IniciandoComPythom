import math

valor = float(input('Digite um valor: '))

print(f'Quadrado do número.....:  {math.pow(valor, 2)}')

print(f'Raíz quadrada do número...: {math.sqrt(valor)}')

print('*' * 60)

# Outra maneira de se importar funções especificas do math

from math import pow, sqrt

print(f'\n\nQuadrado do número.....:  {pow(valor, 2)}')

print(f'Raíz quadrada do número...: {sqrt(valor)}')


x = dir(math)

for e in x:
    print(f" essa é a função: {e}")

print(f"\n {x}")