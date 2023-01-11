"""
Escreva um programa que lê 2 matrizes A e B, cada uma com 3 linhas e 2 colunas. 
Construir uma matriz C de mesma dimensão (3x2) onde C é formada pela soma dos elementos da matriz A com os elementos da matriz B 
(exemplo: C[1][1] = A[1][1] + B[1][1]). Apresentar ao final as 3 matrizes (A, B e C).
"""

A = []
B = []
C = []
r = 3
c = 2
 
print('Digite os elementos da matriz A:')
for i in range(0, r):
	itens = []
	for j in range (0, c):
		itens.append(float(input()))

	A.append(itens)
print('Fim da matriz. \n')

print('Digite os elementos da matriz B:')
for i in range(0, r):
	itens = []
	for j in range (0, c):
		itens.append(float(input()))

	B.append(itens)
print('Fim da matriz. \n')

for i in range(0, r):
	itens = []
	for j in range (0, c):
		itens.append(A[i][j]+B[i][j])

	C.append(itens)

print('A matriz A: ', A)
print('A matriz B: ', B)
print('A matriz C = A + B: ', C)
