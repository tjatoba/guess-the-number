print("********************************")
print("Bem-Vindo ao Jogo da Advinhação!")
print("********************************")

secret_number = 42

rounds = 3
round_number = 1

# while round_number <= rounds:
    # print("Rodada", round_number, "de", rounds) -> maneira mais rudimentar
for round_number in range(1, rounds + 1):
    print("Rodada {} de {}".format(round_number, rounds))
    # user_guess_str = input("Digite seu número: ")
    user_guess_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", user_guess_str)
    user_guess = int(user_guess_str)

    if user_guess < 1 or user_guess > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue

    right_choice = secret_number == user_guess
    higher = user_guess > secret_number
    lower = user_guess < secret_number

    if right_choice:
        print("Você Acertou")
        break

    else:
        if higher:
            print("Foi quase... numero chutado é maior que o número secreto!")
        elif lower:
            print("Por pouco... seu número chutado foi menor que o número secreto!")

    # round_number = round_number + 1 -> quando escrevo while

print("FIM DO JOGO!")
