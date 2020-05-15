import random


def display_intro_msg():
    print("* * * * * * * * * * * * * * * *")
    print("* Welcome to the Hangman Game *")
    print("* * * * * * * * * * * * * * * *")


def load_secret_word(file):
    words = []
    file = open("words.txt", "r")
    for lines in file:
        lines = lines.strip()
        words.append(lines)
    file.close()
    number_words = random.randrange(0, len(words))
    return words[number_words].upper()


def check_letter_used(user_letter, all_guesses):
    if user_letter not in all_guesses:
        all_guesses.append(user_letter)
        return False
    else:
        print("You already used this one. Try another letter")
        return True


def get_user_guess():
    user_guess = input("What is your guess?:")
    user_guess = user_guess.strip().upper()
    return user_guess


def winning_message():
    print("Congrats! You won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def defeat_message(secret_word):
    print("You just got HANGED!")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def play():
    display_intro_msg()
    secret_word = load_secret_word("words.txt")
    good_guesses = ["_" for letter in secret_word]

    hanged = False
    won = False
    failed_tries = 0
    all_guesses = []
    print(good_guesses)

    while not won and not hanged:

        user_letter = get_user_guess()

        if check_letter_used(user_letter, all_guesses):
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
        winning_message()
    else:
        defeat_message(secret_word)


if (__name__ == "__main__"):
    play()
