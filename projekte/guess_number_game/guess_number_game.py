# Guess the number game
import random

# Functions
def user_round():
    print()
    print("The computer chooses a secret number between 1 and 100 ...")
    computer_number = random.randint(1, 100)
    guesses = 0
    guess = 0

    while guess != computer_number:
        user_input = input("Try to guess the number? > ")
        guesses += 1

        try:
            guess = int(user_input)
        except:
            print("Only number input, please.")


        if guess > computer_number:
            print("Your number is to high!")

        else:
            print("Your number is too low!")

    print(f"You guessed the number {guess} correct. You needed {guesses} guesses.")

    return guesses


def computer_round():
    print("Now think of a number between 0 and 100 the computer needs to guess... Press any key when you are ready. ")
    input()

    print("The computer will try to guess the secret number now. You can tell it if it guessed too 'l'ow or too 'h'igh or if it is 'c'orrect. 0 to quit the Program. ")
    guess = 0
    guesses = 0

    low = 1
    high = 100

    while True:
        guess = random.randint(low, high)

        user_input = input(f"Computer guess: {guess} | Is this correct?(l,h,c or 0) > ")

        if user_input == 'l':
            guesses += 1
            print("Computer guessed too low.")
            low = guess + 1
        elif user_input == 'h':
            guesses += 1
            print("Computer guessed too high.")
            high = guess - 1
        elif user_input == 'c':
            guesses += 1
            print("Computer guessed correct.")
            print(f"Number of guesses: {guesses}")
            return guesses
        elif user_input == '0':
            print("Out of here")
            quit()
        else:
            print("Invalid input.")



print()
print("Guess The Number Game".upper())
print("Can you guess a number between 1 and 100 in less turns then the computer?")

while True:
    print()
    print("MENU")
    print("0) End Program")
    print("1) Play the Game")
    print()

    user_input = input("Choose a MENU point >> ")

    try:
        user_input = int(user_input)

    except:
        print("User input must be a number.")


    if user_input == 0:
        print("Closing Program")
        quit()

    elif user_input == 1:
        print("First is your turn. The computer chooses a number between 1 and 100. You have to guess this number.")
        user_guesses = user_round()
        print(f"Your number of guesses: {user_guesses}")

        print()
        print("Now it is the computers turn. You need to choose a number between 1 and 100 and the computer needs to guess the correct number.")
        computer_guesses = computer_round()
        print(f"The computer number of guesses: {computer_guesses}")

        print()
        print(f"You had {user_guesses} guesses and the computer had {computer_guesses} guesses.")
        if user_guesses < computer_guesses:
            print("You won the game!!!")
        elif user_guesses == computer_guesses:
            print("It's a tie!")
        else:
            print("The computer won the game!!!")

    else:
        print("Not a valid option.")
