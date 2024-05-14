import time

pergaminho_magico = ('ferrolho', 'parafuso', 'saci-perere')

print("Eiii...")
time.sleep(1)
print("você mesmo!")
print("Vamos comigo em uma jornada pelas ruas de recife procurando pistas sobre o pergamino perdido?\n"
                     "Vamos começar pela praça do marco zero!")

senhor = input("passando pela praça do marco zero, encontramos um senhorzinho em um banco, ele é conhecido por contar historias mirabolantes...\n"
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
    print("Mulher: Você fala do pergaminho dos passos de frevo?")

