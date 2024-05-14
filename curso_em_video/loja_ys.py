
produtos = {
    "televisão": 1500,
    "smartphone": 1000,
    "notebook": 3300,
    "videogame": 700
}

produto_escolhido = str(input(f'Os produtos disponiveis são: {produtos} \n'
                              f'Qual você quer? '))

forma_de_pagamento = int(input(f'Escolha sua forma de pagamento, tecle o numero' 
                               f' correspondente a forma de pagamento que você escolheu.\n'
                               f' 1 - à vista DINHEIRO/CHEQUE 10% de desconto\n'
                               f' 2 - à vista no CARTÃO: 5% de desconto\n'
                               f' 3 - em até 2x no cartão: preço normal\n'
                               f' 4 - até 12x no cartão: 20% de juros\n'))

def calcular_preco_final (produto, forma_de_pagamento):

    if produto not in produtos:
        return 'produto não encontrado'

    preco_base = produtos[produto]
    if forma_de_pagamento  == 1:
        preco_final = preco_base - (preco_base * 0.10)
        print(f'O preço final do produto {produto} com o desconto de 10% ficou R$ {preco_final}')
    elif forma_de_pagamento == 2:
        preco_final = preco_base - (preco_base * 0.5)
        print(f'O preço final do produto {produto} com o desconto de 5% ficou R$ {preco_final}')
    elif forma_de_pagamento == 3:
        parcelas = preco_base / 2
        print(f'O preço final do produto {produto} ficou R$ {preco_base}, sem desconto. Com parcelas de R$ {parcelas}')
    elif forma_de_pagamento == 4:
        preco_final = preco_base + (preco_base * 0.20)
        parcelas = int(input(' Em quantas parcelas você quer dividir? Dividimos em até 12x no cartão'))
        preco_parcelas = preco_final / parcelas
        print(f'O preço final do produto {produto} ficou R$ {preco_final}, com acréscimo de 20% de juros e parcelas de R$ {preco_parcelas} mensais')

calcular_preco_final(produto_escolhido, forma_de_pagamento)