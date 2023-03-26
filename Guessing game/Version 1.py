import random


def guess_number():
    max_lives = 3
    min_lives = 0

    win_num = random.randint(1, 10)
    min_num = 1
    max_num = 10

    print("You can guess from 1 to 10.")

    while max_lives > min_lives:
        print("---------------------------")
        guessing_num = input("Guess a number: ")

        if not guessing_num.isdigit():
            print("Please, enter valid number.")
            continue

        guessing_num = int(guessing_num)

        if guessing_num > max_num or guessing_num < min_num:
            print("Please, enter a number from 1 to 10.")
            continue

        max_lives -= 1

        if guessing_num > win_num and max_lives > min_lives:
            print("Lower")
        elif guessing_num < win_num and max_lives > min_lives:
            print("Higher")
        elif guessing_num == win_num:
            print("Congrats! You win!")
            break

        print(f"Lives: {max_lives}")

    print(f"The winning number was: {win_num}")


guess_number()
