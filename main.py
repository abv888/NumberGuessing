import random


is_game_over = False


def game():
    global is_game_over

    number_of_attempts = 0
    print("Welcome to the Number Guessing game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        number_of_attempts = 5
    elif difficulty == "easy":
        number_of_attempts = 10
    else:
        print("You wrote the wrong answer!")
    generated_number = random.randint(1, 100)
    for i in range(number_of_attempts):
        print(f"You have {number_of_attempts - i} attempts remaining to guess the answer.")
        guess = int(input("Make a guess: "))
        if guess == generated_number:
            print(f"You got it! Answer was {generated_number}.")
            break
        elif guess > generated_number:
            print("Too high.")
            if i != (number_of_attempts - 1):
                print("Guess again")
        else:
            print("Too low.")
            if i != (number_of_attempts - 1):
                print("Guess again")


def final_question():
    global is_game_over
    question = input("This repl has exited, run again? Type 'y' or 'n': ")
    if question == "y":
        is_game_over = False
    else:
        is_game_over = True
        print("Good bye!")


while not is_game_over:
    game()
    final_question()
