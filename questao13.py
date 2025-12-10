n = int(input("Digite um número inteiro: "))
if n < 2:
    print(f"{n} não é um número primo.")
else:
    i = 2
    primo = True
    while i < n:
        if n % i == 0:
            primo = False
            break  
        i += 1
    if primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")
