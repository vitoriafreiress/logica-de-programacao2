A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
i = A
print(f"Números ímpares entre {A} e {B}:")
while i <= B:
    if i % 2 != 0:  
        print(i, end=" ")
    i += 1
