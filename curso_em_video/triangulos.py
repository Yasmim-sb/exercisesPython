r1 = float(input('digite o valor do primeiro segmento: '))
r2 = float(input('digite o valor do segundo segmento: '))
r3 = float(input('digite o valor do terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 :
    print('Os segmentos acima PODEM FORMAR um triângulo!')

    if r1 == r2 and r3 == r1:
        print('O triângulo é EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triângulo é ISÓSCELES')
    else:
        print(' O triângulo é ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
