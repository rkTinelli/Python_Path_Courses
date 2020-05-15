import random

def play():
    print("* * * * * * * * * * * * * * * *")
    print("* Welcome to the Hangman Game *")
    print("* * * * * * * * * * * * * * * *")

    file = open("words.txt", "r")
    words = []

    for lines in file:
        lines = lines.strip()
        words.append(lines)

    file.close()

    number_words = random.randrange(0, len(words))
    secret_word = words[number_words].upper()
    good_guesses = ["_" for letter in secret_word]

    hanged = False
    won = False
    failed_tries = 0
    all_guesses = []

    print(good_guesses)

    while not won and not hanged:

        user_letter = input("What is your guess?:")
        user_letter = user_letter.strip().upper()

        if user_letter not in all_guesses:
            all_guesses.append(user_letter)
        else:
            print("You already used this one. Try another letter")
            continue

        if user_letter in secret_word:
            index = 0
            for letter in secret_word:
                if letter == user_letter:
                    good_guesses[index] = letter
                index += 1
        else:
            failed_tries += 1

        if failed_tries == 6:
            break
        if "_" not in good_guesses:
            won = True
            break
        print(good_guesses)

    if won:
        print("You win!")
        print(good_guesses)
    else:
        print("You lost!")

    print("Game Over")


if (__name__ == "__main__"):
    play()