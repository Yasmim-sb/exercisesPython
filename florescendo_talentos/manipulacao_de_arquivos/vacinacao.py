import csv
with open('registro_vacinacao.csv') as file:
    ler_csv = csv.reader(file)
    for row in ler_csv:
        print(row)
