import random

while True:
    Jogador = input("Escolha um movimento (Pedra, Papel, Tesoura): ")
    Opcoes = ["Pedra", "Papel", "Tesoura"]
    Computador = random.choice(Opcoes)
    print(f"\nVocê escolheu {Jogador}, cpu escolheu {Computador}.\n")

    if Jogador == Computador:
        print(f"Os dois escolheram {Jogador}. Deu empate!")
    elif Jogador == "Pedra":
        if Computador == "Tesoura":
            print("Pedra bate tesoura! Você venceu!")
        else:
            print("Papel vence pedra! Você Perdeu!.")
    elif Jogador == "Papel":
        if Computador == "Pedra":
            print("Papel cobre Pedra! Você venceu!")
        else:
            print("Tesoura corta Papel! Você perdeu.")
    elif Jogador == "Tesoura":
        if Computador == "Papel":
            print("Tesoura corta Papel! Você venceu!")
        else:
            print("Pedra bate Tesoura! Você perdeu.")

    Jogar_Novamente = input("Jogar de novo? (s/n): ")
    if Jogar_Novamente.lower() != "s":
        break