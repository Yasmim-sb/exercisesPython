import time

print("bem-vindo a bytenopolis, onde tudo é mágico!")

print("Aqui você escolherá entre 3 caminhos que irão determinar seu rumo...")

escolha_caminho = int(input("deseja ir pelo caminho 1, 2 ou 3? "))


def caminho_um():
    tempo_espera = 1

    print("você acaba de entrar no caminho dos arco-iris, onde tudo é colorido e feliz")
    print("fique a vontade para beber um pouco da fonte de chocolate quente, é feito com os melhores ingredientes de todo o reino")
    print("...")
    time.sleep(tempo_espera)

    print("veja! os unicornios vieram lhe dar boas vindas!")
    time.sleep(tempo_espera)

    carinho = input("você pode fazer carinho neles se quiser, são muito docéis! (sim/nao)")

    if carinho == 'sim':
        montar = input("Ele parece ter gostado de você, esta te convidando para montar nele, voce tem coragem? (sim/nao)")
        if montar == 'sim':
            print("...")
            time.sleep(tempo_espera)
            print("UAU. Eu nunca tinha visto ele deixar alguém montar ele, ele gostou mesmo de você!")
        else:
            print("Tudo bem, vamos continuar o passeio, ainda tem muito para ver...")
    else:
        print("você é um pouco medroso ne? que bom que veio não escolheu o caminho errado...")
        print("bom, vamos! ainda tem muito para ver!")



def caminho_dois():
    tempo_espera = 2

    print("você acaba de entrar no caminho deserto, aqui não tem nada pra ver")
    time.sleep(tempo_espera)
    print("bom, tem areia...")
    time.sleep(tempo_espera)

    print("tudo que lhe resta é andar até achar a saida")
    print("ou não...")


def caminho_tres():
    tempo_espera = 1
    print("hmm. aquilo é uma mesa cheia de doces?")

    doces = input("você pode comer se quiser... (sim/nao)")

    if doces == 'sim':
        print("tava gostoso?")
        time.sleep(tempo_espera)
        print("eu espero que tenha valido a pena, porque o veneno que há nesses doces é brutal, então será sua ultima refeição...")
        time.sleep(tempo_espera)
        print("pobre coitado, tão ingenuo...")
        time.sleep(tempo_espera)

    else:
        print("bom, você é menos burro do que pensei.")
        time.sleep(tempo_espera)
        print("porque se comesse, morreria. :(")

    print("Ah. quase ia me esquecendo, bem-vindo ao caminho das trevas! :)")
    time.sleep(tempo_espera)


if escolha_caminho == 1:
    caminho_um()

if escolha_caminho == 2:
    caminho_dois()


if escolha_caminho == 3:
    caminho_tres()
