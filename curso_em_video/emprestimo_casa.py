valor_casa = float(input('digite o valor da casa: R$ '))
salario_comprador = float(input('digite seu salario mensal: R$ '))
anos = int(input('em quantos anos você pretende pagar? '))
parcelas = valor_casa / (anos*12)
minimo = salario_comprador * 30 / 100

print(f'Para pagar uma casa no valor de R${valor_casa:.2f} em {anos} anos')
print(f'A prestação seria de R${parcelas:.2f}')

if parcelas > (minimo):
  print('seu empréstimo foi negado!')
else:
  print(f'seu empréstimo foi aprovado!')