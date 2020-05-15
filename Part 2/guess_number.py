import random

def play():
    print("* * * * * * * * * * * * * * * * * * * *")
    print("* Welcome to the Guessing Number Game *")
    print("* * * * * * * * * * * * * * * * * * * *")

    secret_number = random.randrange(1, 101)
    max_n_tries = 0
    points = 1000

    print("Level Settings: (1) Easy (2) Normal (3) Hard")
    level = int(input("Select your level: "))

    if (level == 1):
        max_n_tries = 20
    elif (level == 2):
        max_n_tries = 10
    else:
        max_n_tries = 5

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
            print("You won and got {}!!".format(points))
            break
        else:
            lost_points = secret_number - guess
            points = points - lost_points

            if (bigger):
                print("You lost! Keep in mind that your guess was bigger than the secret number")
            elif (smaller):
                print("You lost! Keep in mind that your guess was smaller than the secret number")

        round += 1
        if (round == max_n_tries+1):
            print("The secret number was {}. You scored {} points".format(secret_number, points))
            break

    print("Game Over")


if (__name__ == "__main__"):
    play()