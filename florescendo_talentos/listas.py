nomes = ['Maria', 'José', 'Fernanda']

habilidades = ['Passos marcados, Giro rápido', 'Saltos acrobáticos, Girar o par', 'Coreogrtafias elaboradas']

preferencia = ['Forró pé de serra', 'Xote', 'Baião']

def mostrar_listas(indice):
    print(f"Nome: {nomes[indice]}")
    print(f"Habilitates: {habilidades[indice]}")
    print(f"Preferências: {preferencia[indice]}")

for i in range (len(nomes)):
    mostrar_listas(i)
    print("-" * 45)