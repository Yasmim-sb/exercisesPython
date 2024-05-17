def adicionar_arquivo():
    with open("registro_vacinacao.csv", "a") as arquivo:
        nome = input("Qual seu nome? ")
        idade = input("Quantos anos você tem? ")
        vacinacao = input("Você foi vacinado? ")
        arquivo.write(nome + ", " + idade + " anos,"+ "Foi vacinado(a)? " + vacinacao+"\n")

        print("você foi registrado com sucesso!")
def mostrar_arquivo():
    with open("registro_vacinacao.csv", "r") as arquivo:
       for linha in arquivo:
           print(linha.strip())

while True:
    print("-------Menu-------\n")
    print("1 - registrar arquivos\n")
    print("2 - mostrar arquivos\n")
    print("3 - encerrar execução\n")

    menu = int(input("Qual opção acima você quer escolher? "))

    if menu == 1:
        adicionar_arquivo()
    elif menu == 2:
        mostrar_arquivo()
    elif menu == 3:
        print("execução encerrada!")
        break
