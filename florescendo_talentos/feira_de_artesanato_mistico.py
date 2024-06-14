import time

frutas = ['maça', 'pêra', 'uva', 'abacaxi']
vegetais= ['alface', 'brócolis', 'cebola', 'alho', 'anel de ruby']

def procurar_artefato(lista):
    artefato_encontrado = False

    for artefato in lista:
        if artefato == 'anel de ruby':
            print("Olhando item por item...")
            time.sleep(4)
            print("O artefato foi encontrado!\n"
                  "Precisaremos fazer algumas perguntas para que possamos concluir nossa investigação...")
            artefato_encontrado= True
            break
    if not artefato_encontrado:
        print("Olhando item por item...")
        time.sleep(4)
        print("A busca foi concluída com sucesso e nada foi encontrado!")


print("Estamos fazendo uma busca por uma artefato perdido que talvez se encontre em uma das barracas...\n"
      "Boa sorte, detetive!")
time.sleep(2)
interacao = input("você pode começar conversando com os proprietários das barracas.\n"
                  " vamos começar?(s/n) ")

if interacao == 's':
    print("olá, sou o proprietário da barraca de frutas, soube que está fazendo uma investigação"
                                " sobre um artefato!? bom, eu não vi nada de suspeito não...")
    proprietario_frutas= input("Quer fazer a procura na barraca de frutas mesmo assim,"
                               " ou quer passar para o próximo proprietário? (s/n) ")

    if proprietario_frutas == 's':
        procurar_artefato(frutas)
        print("Passando para o próximo! ")
        time.sleep(2)
    else:
        print("Passando para o próximo! ")


    print("olá, sou a proprietária da barraca de vegetais, se não ficou óbvio pela placa...\n"
          " E antes que pergunte, não. Não vi nada. Pode me dar licença agora?")
    proprietaria_vegetais = input("Quer fazer a procura na barraca de vegetais? (s/n) ")

    if proprietaria_vegetais == 's':
        procurar_artefato(vegetais)
    else:
        print("A investigação falhou, você não encontrou o artefato...")

elif interacao == 'n':
    print("OPS... Sabia que tinham escolhido a pessoa errada...")

else:
    print("opção inválida")
