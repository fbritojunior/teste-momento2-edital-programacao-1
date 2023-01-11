"""
Escreva um programa que, dada uma matrix 3x3, armazena em cada posição da matriz, 
a soma dos valores da linha e coluna que definem a posição. 
Por exemplo, na posição [1][2] você deverá armazenar o valor 1+2 = 3 e assim por diante. 
Imprima a matriz na tela.
"""

import numpy as np

mat = np.array(np.zeros((3, 3), dtype=int))

"""
for l in range(1, 4):
    for c in range(1, 4):
        mat[l-1, c-1] = l + c
"""

for l in range(1, 4):
    for c in range(1, 4):
        mat[l-1, c-1] = l + c

print(mat, sep=",")