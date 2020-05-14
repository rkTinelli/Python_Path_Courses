import random

print("* * * * * * * * * * * * * * * * * * * *")
print("* Welcome to the Guessing Number Game *")
print("* * * * * * * * * * * * * * * * * * * *")

secret_number = random.randrange(1, 101)
max_n_tries = 3

for round in range(1, max_n_tries+1):
    print("Round {} of {}".format(round, max_n_tries))
    guess_str = input("What is your number? ")
    print("Your guess was: ", guess_str)
    guess = int(guess_str)

    if (guess < 1 or guess > 100):
        print("You must use a number between 1 and 100!")
        continue

    won = guess == secret_number
    bigger = guess > secret_number
    smaller = guess < secret_number

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
