idade = int(input("Qual é a sua idade? "))

if idade < 16:
    print("Você ainda não pode votar.")
elif idade == 16 or idade == 17:
    print("VOTO FACULTATIVO! Significa que você pode votar se quiser, mas é algo opcional.")
elif idade >= 18 and idade < 70:
    print("VOTO OBRIGATÓRIO!")
else:
    print("VOTO FACULTATIVO! Significa que você pode votar se quiser, mas é algo opcional.")