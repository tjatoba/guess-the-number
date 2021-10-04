print("********************************")
print("Bem-Vindo ao Jogo da Advinhação!")
print("********************************")

secret_number = 42

user_guess_str = input("Digite seu número: ")

print("Você digitou ", user_guess_str)

user_guess = int(user_guess_str)

if secret_number == user_guess:
    print("Você Acertou")

else:
    print("Que pena! Você errou... :(")

print("FIM DO JOGO!")