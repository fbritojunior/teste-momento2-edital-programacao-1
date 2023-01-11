"""
Escreva um programa que, dada uma matrix 3x3, armazena em cada posição da matriz, 
a soma dos valores da linha e coluna que definem a posição. 
Por exemplo, na posição [1][2] você deverá armazenar o valor 1+2 = 3 e assim por diante. 
Imprima a matriz na tela.
"""

mat = []
n = 3
  
for row in range(1, n+1):
	itens = []
	for col in range (1, n+1):
		itens.append(row + col)

	mat.append(itens)

print('A matriz 3 x 3: ', mat, end='')
