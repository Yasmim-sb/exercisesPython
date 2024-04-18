matriz = [[],[],[]]

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f"digite um número para posição [{l} {c}]: ")))

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]: ^4}]", end="")
    print()


soma_impares = 0
soma_primeira_coluna = 0
menor_terceira_linha = matriz[2][0]

for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 != 0:
            soma_impares += matriz[l][c]
        if c == 0:
            soma_primeira_coluna += matriz[l][c]
        if l == 2 and matriz[l][c] < menor_terceira_linha:
            menor_terceira_linha = matriz[l][c]


print(f"\nSoma dos valores ímpares: {soma_impares}")
print(f"Soma dos valores da primeira coluna: {soma_primeira_coluna}")
print(f"menor valor da terceira linha: {menor_terceira_linha}")