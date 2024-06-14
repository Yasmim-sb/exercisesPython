import random

frutas = ["uva", "morango", "melancia"]

vegetais = ["beringela", "alface", "brocolis"]
def escolher_ganhador(array, categoria):
    elemento_sorteado = random.choice(array).upper()

    print(f"os nossos jurados escolheram, {elemento_sorteado} da categoria {categoria} como ganhador!")

categorias = [('FRUTAS',frutas), ('VEGETAIS',vegetais)]

for categoria, array in categorias:
    escolher_ganhador(array, categoria)


