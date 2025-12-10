i = 1
soma_pares = 0
soma_impares = 0
while i <= 10:
    numero = int(input(f"Digite o {i}º número: "))
    if numero % 2 == 0:  
        soma_pares += numero
    else: 
        soma_impares += numero
    i += 1
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
