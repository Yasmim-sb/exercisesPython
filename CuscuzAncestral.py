ingredientes =  ("milho", "farinha de milho"), ("Tomate", "Cebola","Pimentão","Coentro"),
("água","sal","azeite")

instrucoes = ("Misture o milho com a farinha de milho.", "Pique o tomate, cebola, pimentão e coentro e adicione à mistura."
            , "Acrescente água, sal e azeite.", "Coloque em uma cuscuzeira em fogo médio até a casa estiver com cheiro de cuscuz.")

def exibir_instrucoes(ingredientes, instrucoes):

    print("Instruções para a receita escolhida: ")
    for intrucao in instrucoes:
        print(intrucao)

print("Ingredientes disponíveis:",
      "1. Milho, Farinha de milho",
      "2. Tomate, Cebola, Pimentão, Coentro",
      "3. Água, Sal, Azeite")

while True :
    escolha = input("Escolha uma tupla de ingredientes (ou digite '0' para encerrar) :")

    if escolha == '0':
        print("Encerrando o programa.")
        break
    elif escolha == '1':
        exibir_instrucoes(ingredientes, instrucoes)
    else:
        print("Opção inválida. por favor, escolha outra opção.")
