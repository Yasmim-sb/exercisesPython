
hamburguer = {'de carne' : 15.00, 'de frango' : 10.00, 'vegetariano' : 15.00}

extras = {'molho branco': 5.00, 'bacon' : 7.00, 'queijo': 4.00 }

saudacao = str(input("Olá! quer fazer seu pedido?  (sim/não): "))


if saudacao == "sim":
    print("O cardapio de hoje é hamburguer, as opções são: ")

    for opcao, preco in hamburguer.items():
        print("-", opcao, ":", preco)

    pedidoHamburguer = input("Qual opção você deseja? ")

    valor_total = hamburguer.get(pedidoHamburguer, 0)

    add_extras = input("Deseja acrescentar extras? (sim/não) ")
    if add_extras == "sim":
        for opcao, preco in extras.items():
            print("-", opcao, ":", preco)
        pedidoExtra = input(" Qual extra você deseja acrescentar? ")
        valor_extra = extras.get(pedidoExtra, 0)
        valor_total += valor_extra
        print("pedido total: ", valor_total)
    elif add_extras == 'não':
        print("Muito obrigada pela confiança e até a próxima!")
    else:
        print("opção inválida. Tente novamente.")

elif saudacao == 'não':
    print("Quem sabe uma próxima vez :)")
else:
    print("Opcão inválida! Tente novamente")



