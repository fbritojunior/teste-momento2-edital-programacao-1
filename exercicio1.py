"""
Faça um programa que preencha um vetor com 6 valores distintos digitados pelo usuário. 
Em seguida, exiba o maior e o menor valor do vetor, indicando em qual posição eles se encontram. 
Depois, imprima os itens no vetor em ordem crescente.
"""
import numpy as np

vet = np.array(np.zeros(6))

print("Nota: Devem ser digitados seis (06) valores inteiros ou com (.) como separação decimal.")

while True:
    try:
        for e in range(6):
            print(f"Digite o valor do {e + 1}º elemento: ")
            vet[e] = input()
        break
    except ValueError:
        print("Erro! Digite números válidos.")
        continue

print(vet)

min_val = np.min(vet)
min_index = np.argmin(vet) + 1
print(f"\nO valor mínimo encontrado no vetor é {min_val} na posição {min_index}.")

max_val = np.max(vet)
max_index = np.argmax(vet) + 1
print(f"O valor máximmo encontrado no vetor é {max_val} na posição {max_index}.")

orr_vet =  np.sort(vet)
print("\nO vetor ordenado:")
print(orr_vet)

 