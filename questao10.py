i = 1
numero = int(input("Digite o 1º número: "))
maior = numero
menor = numero
while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    i += 1
print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")
