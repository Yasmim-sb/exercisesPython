operacao= input("Escolha a operação que deseja realizar (adição, subtração, divisão, multiplicação) ")
n1= float(input("Digite o primeiro número: "))
n2= float(input("Digite o segundo número: "))

if operacao == "adição":
    resultado = n1 + n2
    print(f"Os números escolhidos foram {n1} e {n2}\n")
    print(f"E o resultado da operação é: {resultado}")
elif operacao == "subtração":
    resultado = n1 - n2
    print(f"Os números escolhidos foram {n1} e {n2}\n")
    print(f"E o resultado da operação é: {resultado}")
elif operacao == "divisão":
    resultado = n1 / n2
    print(f"Os números escolhidos foram {n1} e {n2}\n")
    print(f"E o resultado da operação é: {resultado}")
elif operacao == "multiplicação":
    resultado = n1 * n2
    print(f"Os números escolhidos foram {n1} e {n2}\n")
    print(f"E o resultado da operação é: {resultado}")
else:
    print("Escolha uma opção válida!")
