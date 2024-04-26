import csv
with open('produtos.csv') as file:
    ler_csv = csv.reader(file, delimiter='/')
    for row in ler_csv:
        print(row)