import os
os.system("cls")
arquivo = open("dados.txt", "r")
dados = arquivo.read()
palavras = dados.split()

print("dados dos arquivos: \n", dados)
print("\nQuantidade de caracteres: ", len(dados))
print("\nQuantidade de palavras: ", len(palavras))

print(len(dados))