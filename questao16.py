i = 1
contador_positivos = 0
while i <= 10:
    numero = int(input(f"Digite o {i}º número: "))
    if numero > 0:
        contador_positivos += 1 
    i += 1
print(f"Quantidade de números positivos digitados: {contador_positivos}")
