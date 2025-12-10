while True:
    print("\nMenu:")
    print("1 - Somar dois números")
    print("2 - Subtrair dois números")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"A soma é: {a + b}")
    elif opcao == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"A subtração é: {a - b}")
    elif opcao == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
