arquivo_numeros = open("media.txt", "r")
soma = 0.0
quantidade_n = 0

for num in arquivo_numeros:
    num= float(num)
    soma+=num
    quantidade_n+=1

arquivo_numeros.close()

media = soma/quantidade_n
print(media)