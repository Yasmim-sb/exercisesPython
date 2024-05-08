numero = int(input('digite um numero: '))
conversao = str(input('escolha a base que quer converter, 1 para binário, 2 para octal, 3 para hexadecimal'))

if conversao == 1:
  nBinario = bin(numero)[2:]
  print(f'O numero {numero} em binário é: {nBinario}')
if conversao == 2:
  nOctal = oct(numero)[2:]
  print(f'O numero {numero} em binario é: {nOctal}')
else:
  nHex = hex(numero)[2:]
  print(f'O numero {numero} em binario é: {nHex}')