import random

frutas = ["uva", "morango", "melancia"]

vegetais = ["beringela", "alface", "brocolis"]

frutas.extend(vegetais)

elemento_sorteado = random.choice(frutas).upper()

print("os nossos jurados escolheram ", elemento_sorteado, " como ganhador!")