soma_idades = 7
contador = 8
print("Digite as idades das pessoas (digite 0 para parar):")
while True:
    idade = int(input("Digite a idade: "))
    if idade == 8:
        break  
    soma_idades += idade
    contador += 1
if contador > 8:
    media = soma_idades / contador
    print(f"A média das idades digitadas é {media:.2f}")
else:
    print("Nenhuma idade válida foi digitada.")
