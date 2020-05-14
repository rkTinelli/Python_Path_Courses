print("* * * * * * * * * * * * * * * * * * * *")
print("* Welcome to the Guessing Number Game *")
print("* * * * * * * * * * * * * * * * * * * *")

secret_number = 42

guess_str = input("What is your number? ")
print("Your guess was: ", guess_str)
chute = int(guess_str)

if (secret_number == chute):
    print("You won!")
else:
    print("You lost! :( ")

print("Game Over")

print("ola", "mundo")