a = 0
b = 1
i = 1
print("Os 10 primeiros termos da sequência de Fibonacci são:")
while i <= 10:
    print(a, end=" ")
    proximo = a + b
    a = b
    b = proximo
    i += 1
