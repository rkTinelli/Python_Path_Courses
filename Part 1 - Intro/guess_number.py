print("* * * * * * * * * * * * * * * * * * * *")
print("* Welcome to the Guessing Number Game *")
print("* * * * * * * * * * * * * * * * * * * *")

secret_number = 42

max_n_tries = 3
round = 1

while (round <= max_n_tries):

    print("Round", round, "of", max_n_tries)
    guess_str = input("What is your number? ")
    print("Your guess was: ", guess_str)
    chute = int(guess_str)

    won = chute == secret_number
    bigger = chute > secret_number
    smaller = chute < secret_number

    if (won):
        print("You won!!")
        break
    else:

        if (bigger):
            print("You lost! Keep in mind that your guess was bigger than the secret number")
        elif (smaller):
            print("You lost! Keep in mind that your guess was smaller than the secret number")

    round += 1

print("Game Over")
