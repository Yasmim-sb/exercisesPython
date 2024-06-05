
hamburguer = {'carne': 15.00, 'frango': 10.00, 'vegetariano': 15.00} #dicionario chave-valor

extras = {'molho branco': 5.00, 'bacon': 7.00, 'queijo': 4.00 } #dicionario chave-valor

bebidas = {'coca-cola': 5.00, 'água com gás': 2.00, 'rochedo tuti-fruti': 3.00} #dicionario chave-valor

escolhas = []

valor_total = 0

def mostrar_opcoes(produto): #função, o dicionario como parametro e percorre ele comn um for mostrando sua chave-valor
    for opcao, preco in produto.items():
        print("-", opcao, ":", preco)

def adicionar_escolhas(escolha_user):
    if escolha_user != 'não':
        escolhas.append(escolha_user)

def mostrar_escolhas_user():
    for escolha in escolhas :
        if escolha in hamburguer:
            print(f"Hambúrguer: {escolha}, Preço: R${hamburguer[escolha]:.2f}")
        elif escolha in bebidas:
            print(f"Bebidas: {escolha}, Preço: R${bebidas[escolha]:.2f}")
        elif escolha in extras:
            print(f"Extra: {escolha}, Preço: R${extras[escolha]:.2f}")



saudacao = input("Seja bem-vindo a nossa hamburgueria!\n"
                 "Deseja fazer um pedido? (sim/não)") # um input serve como entrada de dados pelo teclado

if saudacao == 'sim':
    mostrar_opcoes(hamburguer)
    escolha_hamburgues =input("Escolha uma das opções ou digite 'não' para sair. ")

    adicionar_escolhas(escolha_hamburgues)

    if escolha_hamburgues == 'não':
        print("Quem sabe da próxima vez!")
    else:
        valor_total += hamburguer.get(escolha_hamburgues,0)

        print("Aqui estão nossas opções de bebidas.\n")
        mostrar_opcoes(bebidas)
        escolha_bebidas = input("Digite qual bebida deseja adicionar ao pedido, ou digite 'não' para sair.\n")

        adicionar_escolhas(escolha_bebidas)

        if escolha_bebidas != 'não' :
            valor_total += bebidas.get(escolha_bebidas, 0)

        print("Aqui estão nossas opções de extra:\n")
        mostrar_opcoes(extras)
        escolha_extra = input("Digite qual extra irá querer ou digite 'não' para sair.\n" )
        adicionar_escolhas(escolha_extra)

        if escolha_extra != 'não' :
            valor_total += extras.get(escolha_extra, 0)
            print("Pedido encerrado. Muito obrigada pela preferência.\n"
                  f"O valor total do seu pedido foi de {valor_total}")
            print(f"Seu pedido: \n")
            mostrar_escolhas_user()

        else:
            print("Pedido encerrado. Muito obrigada pela preferência.\n"
                  f"O valor total do seu pedido foi de {valor_total}")
            print(f"Seu pedido: \n")
            mostrar_escolhas_user()



elif saudacao == 'não':
    print("Quem sabe da próxima vez! ")

else:
    print("Opção inválida. Tente novamente.")
