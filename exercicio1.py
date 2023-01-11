"""
Faça um programa que preencha um vetor com 6 valores distintos digitados pelo usuário. 
Em seguida, exiba o maior e o menor valor do vetor, indicando em qual posição eles se encontram. 
Depois, imprima os itens no vetor em ordem crescente.
"""

print('Digite os 06 números para preencher o vetor:')
vet = []

n = 6 
  
for i in range(0, n):
    elem = float(input())
    vet.append(elem)

print('Fim do vetor. \n')

min_val = min(vet)
pos_min = vet.index(min_val)
max_val = max(vet)
pos_max = vet.index(max_val)
lst_ord = sorted(vet)

print(f'O menor valor do vetor é {min_val}, encontrado na posição {pos_min}.')
print(f'O maior valor do vetor é {max_val}, encontrado na posição {pos_max}.')
print('Itens no vetor em ordem crescente:', lst_ord)
 
