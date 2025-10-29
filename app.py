print("BEM VINDO AO PROJETO CALCULADORA\n")
while True:
    primeiro_numero = int(input("Digite o primeiro número:"))
    segundo_numero = int(input("Digite o segundo número:"))

    opcao = input("\n\nQual opção você deseja:\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n0 - Sair\nOpção: ")

    if opcao == "1":
        resultado = primeiro_numero + segundo_numero
        print(f"Resultado: {resultado}")
    elif opcao == "2":
        resultado = primeiro_numero - segundo_numero
        print(f"Resultado: {resultado}")
    elif opcao == "3":
        resultado = primeiro_numero * segundo_numero
        print(f"Resultado: {resultado}")
    elif opcao == "0":
        print("\nAté logo")
        break
    else:
        print("\nOpção inválida, tente novamente")
    print("\n")