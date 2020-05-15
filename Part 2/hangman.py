def play():
    print("* * * * * * * * * * * * * * * *")
    print("* Welcome to the Hangman Game *")
    print("* * * * * * * * * * * * * * * *")

    secret_word = ("banana").upper()

    hanged = False
    won = False

    while not won and not hanged:

        user_letter = input(print("What is your guess?: ")).upper()
        user_letter = user_letter.strip()

        index = 0
        for letter in secret_word:
            if letter == user_letter:
                print("Found {} in the position {}".format(user_letter,str(index)))
            index = index + 1

        print("Playing...")

    print("Game Over")


if (__name__ == "__main__"):
    play()