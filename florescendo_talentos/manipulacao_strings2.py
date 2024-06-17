passos_de_frevo = ('ferrolho', 'saci-perere', 'vassourinha')

def palavra_invertida(posicao):
    palavra = passos_de_frevo[posicao]
    inverso = palavra[::-1]
    return inverso

def palavra_embaralhada(posicao):
    palavra = passos_de_frevo[posicao]
    primeira_silaba = palavra[:2]
    ultima_silaba = palavra[-3:]
    return (f"A primeira sílaba dessa palavra é: {primeira_silaba},\n"
          f" e a última sílaba: {ultima_silaba}")

chamada= input("Olá, soube que você está a procura dos passos perdidos de frevo...\n"
      "Eu tenho o que quer, mas para que consiga, terá que desvendar alguns mistérios.\n"
      "Você está pronto?(s/n) ")
if chamada == 's':
    print("Você terá 3 desafios, cada um para desvendar um passo de frevo.\n"
          "Se você acertar todos, eu lhe passo as coreografias secretas.\n"
          "Caso não consiga... bom, acho que não preciso desenhar ne?")

    primeiro_desafio = input(f"O seu primeiro desafio está aqui: {palavra_invertida(0)}\n"
                             f"consegue adivinhar que palavra é essa? ")
    if primeiro_desafio == 'ferrolho':
        print("Como você acertou tão rápido?")
    else:
        print("Sabia que não conseguiria HAHAHA")

    segundo_desafio = input(f"O seu segundo desafio é esse: {palavra_invertida(1)}\n"
                            f"consegue adivinhar essa? ")
    if segundo_desafio == 'saci-perere':
        print("grr. não acredito que você acertou essa...\n"
              "bom, o melhor eu deixei para o fim. ")
    else:
        print("HAHAHA isso é tão divertido, não acha?")

    terceiro_desafio = input(f"O terceiro e último desafio é : {palavra_embaralhada(2)}\n"
                             f" boa sorte hahaha ")
    if terceiro_desafio == 'vassourinha':
        print("você fez parecer tão fácil!! COMO CONSEGUIU?\n"
              "Mas promessa é dívida, vou pegar o pergaminho com as coreografias...")
    else:
        print("hahaha foi tão bom ver você falhando desse jeito, realmente divertido.")
elif chamada == 'n':
    print("Ops... Acho que escolheram a pessoal errada KKKK")
else:
    print("Resposta inválida. tente novamente.")