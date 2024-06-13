ingredientes = 0
recheios= []
while ingredientes<=4:
    pedido = input("Digite um ingrediente para adicionar a sua tapioca ou digite 'sair' para encerrar o pedido: ")
    if pedido != 'sair':
        ingredientes+=1
        recheios.append(pedido)
    else:
        break
print(f" A sua tapioca tem os recheios de: {','.join(recheios)}")