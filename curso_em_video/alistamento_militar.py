from datetime import date

ano_nascimento = int(input('Qual o ano do seu nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 17:
    saldo = 18 - idade
    print(f'você ainda vai se alistar. você se alistará daqui há {saldo} anos')
    ano_alistamento =  ano_atual + saldo
    print(f'o ano do seu alistamento será {ano_alistamento}')
elif idade == 18:
    print('ja está na hora de se alistar!')
else:
    saldo = idade - 18
    print(f'passou do tempo de se alistar. você deveria ter se alistado há {saldo} anos')
    ano_alistamento =  ano_atual - saldo
    print(f'o ano do seu alistamento foi {ano_alistamento} ')
