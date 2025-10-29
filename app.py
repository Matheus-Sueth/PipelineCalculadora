"""Projeto Calculadora.

Este módulo inicializa e executa a aplicação
"""
import functions.operacoes as func_operations

print("BEM VINDO AO PROJETO CALCULADORA\n")
while True:
    primeiro_numero = int(input("Digite o primeiro número:"))
    segundo_numero = int(input("Digite o segundo número:"))

    opcao = input("\n\nQual opção você deseja:\n" \
    "1 - Somar\n" \
    "2 - Subtrair\n" \
    "3 - Multiplicar\n" \
    "0 - Sair\nOpção: ")

    if opcao == "1":
        resultado = func_operations.somar(primeiro_numero, segundo_numero)
        print(f"Resultado: {resultado}")
    elif opcao == "2":
        resultado = func_operations.subtrair(primeiro_numero, segundo_numero)
        print(f"Resultado: {resultado}")
    elif opcao == "3":
        resultado = func_operations.multiplicar(primeiro_numero, segundo_numero)
        print(f"Resultado: {resultado}")
    elif opcao == "0":
        print("\nAté logo")
        break
    else:
        print("\nOpção inválida, tente novamente")
    print("\n")
