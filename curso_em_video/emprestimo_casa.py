valor_casa = float(input('digite o valor da casa: '))
salario_comprador = float(input('digite seu salario mensal: '))
parcelas_em_anos = int(input('em quantos anos você pretende pagar? '))
parcelas = parcelas_em_anos/12

valor_mensal_da_parcela = valor_casa /  parcelas
if valor_mensal_da_parcela > (salario_comprador/0.30):
  print('seu emprestimo foi negado!')
else:
  print(f'seu emprestimo foi aprovado, as parcelas ficaram de {parcelas:.2f}')