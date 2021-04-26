import random
from time import sleep

print("\nBem vindo ao \'pedra, papel ou tesoura\'!")

sleep(2)
while True:
    print("")

    possible_choices = ["pedra", "papel", "tesoura"]
    computer = random.choice(possible_choices)
    # computer = random.choice(["pedra", "papel", "tesoura"]
    player = str(input("Escolhe pedra, papel ou tesoura: "))

    player = player.lower()

    sleep(0.5)
    print(f"\nTu escolheste: {player} \nPC escolheu:   {computer}")

    sleep(1.5)
    print("")
    if player == computer:
        print(f"Ambos escolheram {player}, é um empate!")
    elif player == "pedra":
        if computer == "papel":
            print("Papel cobre a pedra, perdeste!")
        else:
            print("Pedra parte a tesoura, ganhaste!")
    elif player == "papel":
        if computer == "tesoura":
            print("Tesoura corta o papel, perdeste!")
        else:
            print("Papel cobre a pedra, ganhaste!")
    elif player == "tesoura":
        if computer == "pedra":
            print("Pedra parte a tesoura, perdeste!")
        else:
            print("Tesoura corta o papel, ganhaste!")
    else:
        print("O que inseriste é inválido")

    sleep(1)
    play_again = str(input("\nJogar novamente? (s/n)\n"))
    if play_again.lower() != "s":
        break

