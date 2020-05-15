def play():
    print("* * * * * * * * * * * * * * * *")
    print("* Welcome to the Hangman Game *")
    print("* * * * * * * * * * * * * * * *")

    secret_word = ("banana").upper()
    good_guesses = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    won = False
    all_guesses = []

    while not won and not hanged:

        user_letter = input("What is your guess?:")
        user_letter = user_letter.strip().upper()

        if user_letter not in all_guesses:
            all_guesses.append(user_letter)
        else:
            print("You already used this one. Try another letter")
            continue

        index = 0
        for letter in secret_word:
            if letter == user_letter:
                good_guesses[index] = letter
            index = index + 1

        print(good_guesses)

    print("Game Over")


if (__name__ == "__main__"):
    play()