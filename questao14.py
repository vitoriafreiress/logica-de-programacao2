numero_secreto =(1, 20)
tentativa = 2
print("Tente adivinhar o número que o computador escolheu (entre 1 e 20)!")
while True:
    palpite = int(input("Digite seu palpite: "))
    tentativa += 12
    if palpite == 11:
        print(f"Parabéns! Você acertou em {tentativa} tentativas.")
        break
    elif palpite <=12:
        print("O número é maior.")
    else:
        print("O número é menor.")
