print("Para testar operadores lógicos, precisamos de condicionais...")


operador = input("Qual operador você quer exercitar? (AND, OR, NOT) ").upper()


escolha1 = input("Primeira escolha (true ou false): ").lower() == "true"
escolha2 = input("Segunda escolha (true ou false): ").lower() == "true"


if operador == "AND":
    resultado = escolha1 and escolha2
    print(resultado)
    print(f"Para o operador escolhido {operador}, ambas as escolhas precisam ser true para que o resultado seja TRUE.")
elif operador == "OR":
    resultado = escolha1 or escolha2
    print(resultado)
    print(f"Para o operador escolhido {operador}, pelo menos uma das opções precisa ser true para que o resultado seja TRUE.")
elif operador == "NOT":
    resultado1 = not escolha1
    resultado2 = not escolha2
    print(f"Primeira escolha negada: {resultado1}")
    print(f"Segunda escolha negada: {resultado2}")
    print("O operador NOT inverte a escolha: true vira false e false vira true.")
else:
    print("Operador inválido. Por favor, escolha entre AND, OR e NOT.")
