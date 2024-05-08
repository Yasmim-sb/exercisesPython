numero = int(input('digite um numero: '))
conversao = int(input('escolha a base que quer converter, 1 para binário, 2 para octal, 3 para hexadecimal'))

if conversao == 1:
  nBinario = bin(numero)[2:]
  print(f'O numero {numero} em binário é: {nBinario}')
elif conversao == 2:
  nOctal = oct(numero)[2:]
  print(f'O numero {numero} em octal é: {nOctal}')
elif conversao == 3:
  nHex = hex(numero)[2:]
  print(f'O numero {numero} em binario é: {nHex}')
else:
  print('Opção inválida. Tente novamente.')