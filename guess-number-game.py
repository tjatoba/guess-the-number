print("********************************")
print("Bem-Vindo ao Jogo da Advinhação!")
print("********************************")

secret_number = 42

rounds = 3
round_number = 1

while round_number <= rounds:
    # print("Rodada", round_number, "de", rounds) -> maneira mais rudimentar
    print("Rodada {} de {}".format(round_number, rounds))
    user_guess_str = input("Digite seu número: ")
    print("Você digitou ", user_guess_str)
    user_guess = int(user_guess_str)

    right_choice = secret_number == user_guess
    higher = user_guess > secret_number
    lower = user_guess < secret_number

    if right_choice:
        print("Você Acertou")

    else:
        if higher:
            print("Foi quase... numero chutado é maior que o número secreto!")
        elif lower:
            print("Por pouco... seu número chutado foi menor que o número secreto!")

    round_number = round_number + 1

print("FIM DO JOGO!")