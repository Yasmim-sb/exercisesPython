import csv
with open('file.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["id", "produto", "categoria",
                    "quantidade", "preço", "adicionando_em"])
   writer.writerow([1, "feijao", "comida", 20,100, "01-01-2020"])
   writer.writerow([2, "arroz", "comida", 20,130, "01-02-2020"])