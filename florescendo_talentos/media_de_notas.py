def calcula_media(nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4)/4
    print("A média das suas notas é: ", (media))
    return media

def verificar_aprovacao(media):

    if media > 6:
        print("Você foi aprovado! ")
    elif media == 4 or media <= 6:
        print("Verificação suplementar")
    elif media < 4:
        print("Você foi reprovado!")

notas = []
posicao = 1
while len(notas) < 4:
   nova_nota = float(input(f"Digite sua nota {posicao}: "))
   notas.append(nova_nota)
   posicao +=1

media = calcula_media(notas[0], notas[1], notas[2], notas[3])

verificar_aprovacao(media)


