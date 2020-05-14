import guess_number

def escolhe_jogo():
    print("*********************************")
    print("******* Choose your game! *******")
    print("*********************************")

    print("(1) Hangman (2) Guess the Number")

    jogo = int(input("Which game you want to play? "))

    if (jogo == 1):
        print("Game not implemented yet")

    elif (jogo == 2):
        print("Playing Guess the Number!")
        guess_number.play()

if (__name__ == "__main__"):
    escolhe_jogo()