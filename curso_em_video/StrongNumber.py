import random


def verificar_strong(strong):
    sum_factorial = 0

    for char in strong:
        num = int(char)
        factorial = calcula_fatorial(num)
        sum_factorial += factorial

        print("o fatorial do número", num, "! é:", factorial)

    if int(strong) == sum_factorial:
        print("O número", strong, "é um NUMBER STRONG!")
        print("Pois a soma dos fatoriais dos dígitos de", strong, "é:", sum_factorial)
    else:
        print("O número", strong, "NÃO É STRONG! pois a soma dos fatoriais dos seus dígitos não é igual a", strong)


def calcula_fatorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def number_random(n):
    lista_string = []
    for i in range(n):
        numero_aleatorio = random.randint(0, 600)
        lista_string.append(str(numero_aleatorio))
    return lista_string


def main():
    num_random = number_random(10)

    input_strong = input("Digite um número positivo para saber se ele é forte: ")
    verificar_strong(input_strong)


if __name__ == "__main__":
    main()
