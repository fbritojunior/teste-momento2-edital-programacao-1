"""
Escreva um programa que lê 2 matrizes A e B, cada uma com 3 linhas e 2 colunas. 
Construir uma matriz C de mesma dimensão (3x2) onde C é formada pela soma dos elementos da matriz A com os elementos da matriz B 
(exemplo: C[1][1] = A[1][1] + B[1][1]). Apresentar ao final as 3 matrizes (A, B e C).
"""
import numpy as np 

A = np.array(np.zeros((3, 2)))
B = np.array(np.zeros((3, 2)))
C = np.array(np.zeros((3, 2)))

x, y = np.shape(C)

print(f"Digite a matriz A. ")
for l in range(x):
    for c in range(y):
        print(f"Digite o valor do elemento na linha {l+1} e coluna {c+1}: ")
        A[l, c] = input()

print(f"\nDigite a matriz B. ")
for l in range(x):
    for c in range(y):
        print(f"Digite o valor do elemento na linha {l+1} e coluna {c+1}: ")
        B[l, c] = input()

for l in range(x):
    for c in range(y):
        C[l, c] = A[l, c] + B[l, c]

print("A matriz A é: \n",A)
print("A matriz B é: \n",B)
print("A matriz C = A + B é: \n",C)
