peso = float(input('informe seu peso: '))
altura = float(input('informe sua altura: '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Você está no peso ideal')
elif imc > 25 and imc <= 30:
    print('Você está em sobrepeso')
elif imc > 30 and imc <= 40:
    print('Você está obesidade.')
else:
    print('Obesidade mórbida! Cuidado')
