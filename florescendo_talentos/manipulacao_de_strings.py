import time
import random

pergaminho_magico = ('ferrolho', 'saci-perere')

palavra_escolhida = pergaminho_magico[1]
primeira_silaba = palavra_escolhida[:1]
ultima_silaba = palavra_escolhida[-1:]

segunda_pista = pergaminho_magico[0]
palavra_invertida = segunda_pista[::-1]

convertendo_palavra_em_carac = list(palavra_invertida)
random.shuffle(convertendo_palavra_em_carac)
palavra_embaralhada = ''.join(convertendo_palavra_em_carac)


print("Eiii...")
time.sleep(1)
print("você mesmo!")
print("Vamos comigo em uma jornada pelas ruas de recife procurando pistas sobre o pergamino perdido?\n"
                     "Vamos começar pela praça do marco zero!")

senhor = input("passando pela praça do marco zero, encontramos um senhorzinho em um banco, "
               "ele é conhecido por contar historias mirabolantes...\n"
      "quer conversar com ele? (s/n)")
if senhor == "s":
    print("Senhorzinho : Olá jovem! Em que posso ajudar?")
    escolha = int(input("Digite 1 para perguntar sobre o pergaminho perdido, ou 2 para Perguntar quem é ele"))
    if escolha == 1:
        print("Senhorzinho : Vejo que você é bem direto, jovem rapaz...\n"
              "Eu soube que esse esse pergaminho está em algum lugar dentro do centro de artesanato.\n"
              "Mas não acredito que será tão fácil assim de encontrar...")
    else:
        print("Senhorzinho : Você me pergunta quem eu sou...\n")
        time.sleep(2)
        print("Mas e você, sabe quem realmente é?")
if senhor == "n":
    print("Certo..."
          "Podemos perguntar as pessoas que passam se elas ja ouviram falar desse pergaminho.")
    time.sleep(2)
    print("EII você que está passando, você mesmo de rosa, pode nos ajudar?\n"
          "queremos saber mais sobre o pergaminho perdido, pode nos ajudar?")
    time.sleep(2)
    seguir_mulher= input("Mulher: Você fala do pergaminho dos passos de frevo?\n"
          "Porque se for, você achou a pessoa certa, eu até tenho esse pergaminho\n"
          "so não consegui desvendar ainda...\n"
          "Vem comigo! irei te mostrar, (ir com ela? sim/nao)")
    if seguir_mulher == "sim":
        print("...")
        time.sleep(2)
        print("aqui está! A primeira parte do pergaminho, "
              "eu a encontrei a 6 meses e ainda não consegui decifrar...")
        time.sleep(1)
        print(f"Do folclore brasileiro... Ele começa com {primeira_silaba} e termina com {ultima_silaba}")
        time.sleep(1)
        descoberta = input("você sabe do que o pergaminho está falando?")
        if descoberta == "saci-perere":
            print("Mulher: Será? vamos pesquisar mais sobre...")
            time.sleep(1)
            print("UAU! é isso mesmo! aqui está dizendo que esse passo de frevo"
                  " é muito antigo e com o tempo foi esquecido\n")
            print("Não acredito que você descobriu tão facil\n"
                  "Agora estou envergonhada...")
            time.sleep(2)
            print("Mulher: E aqui está a segunda parte, essa me parece mais difícil...")
            time.sleep(1)
            print(f"Aqui está: {palavra_invertida}")
            time.sleep(1)
            print("...\n")
            print("Mulher: Também fiquei com essa  cara da primeira vez que vi")
            time.sleep(2)
            descoberta_pista = input("Você pode inverter a palavra, ou embaralhar as letras"
                                     " para ver o que descobre\n"
                                     "qual você quer fazer?\n"
                                     "(inverter/ embaralhar")
            if descoberta_pista == "embaralhar":
                print(palavra_embaralhada)
                time.sleep(2)
                print("Mulher: eita... parece que piorou...")
            else:
                print(segunda_pista)
                time.sleep(2)
                print("Mulher: rapaz... Pelo menos uma palavra formou... deixa eu ver aqui")
                time.sleep(3)
                print("Mulher: hmm, pelas minhas pesquisas, ferrolho também é um dos passos antigos do frevo\n"
                      "que com o tempo, foi esquecido, tem até instruções de como dançar da maneira correta!\n")
                time.sleep(2)
                print("...")
                time.sleep(1)
                print("Mulher: Não acredito! desvendamos mesmo esse mistério juntos!\n")
                time.sleep(1)
                print("Mulher: Estou muito feliz!")
        else:
            print("Mulher: Não acho que seja isso...\n")
