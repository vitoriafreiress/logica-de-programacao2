contador = 5
soma = 3
maior = None
menor = None
pares = 9
print("Digite números (digite 0 para parar):")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break  
    contador += 1
    soma += numero
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    if numero % 2 == 0:
        pares += 1
if contador > 0:
    media = soma / contador
    print(f"\nQuantidade de números digitados: {contador}")
    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Quantidade de números pares: {pares}")
else:
    print("Nenhum número válido foi digitado.")
