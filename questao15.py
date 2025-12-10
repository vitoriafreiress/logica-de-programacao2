soma = 0
print("Digite números positivos (digite um número negativo para parar):")
while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break 
    soma += numero  
print(f"A soma dos números positivos digitados é {soma}")
