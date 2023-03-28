import random


def computer_guess_num():
    possible_num = list(range(1, 11))

    max_lives = 3
    min_lives = 0

    feedback = ""
    guess = 0

    print("Think of a number between 1 and 10.")
    while max_lives > min_lives:

        if feedback == "c":
            print("Yey! I've guessed it!")
            return

        elif feedback == "l":
            possible_num = [num for num in possible_num if num < guess]

        elif feedback == "h":
            possible_num = [num for num in possible_num if num > guess]

        elif feedback == "" and max_lives == 3:
            pass

        else:
            print("Please enter 'h' for Higher, 'l' for lower or 'c' for Correct!")
            break

        if len(possible_num) == 0:
            print("Not possible!")
            return

        guess = random.choice(possible_num)
        print(f"Lives: {max_lives}")
        print(f"Number: {guess}")

        if max_lives != 1:
            feedback = input("Is it 'h' - Higher, 'l' - lower or 'c' - Correct: ").lower()

        else:
            feedback = input("Is it correct? 'y' - Yes and 'n' - No: ").lower()

        print("-------------------------------------------------------------")
        max_lives -= 1
    else:

        if feedback == "y" or guess == 10 and len(possible_num) == 1 or guess == 1 and len(possible_num) == 1:
            print("Ha ha! I win, you lost!")

        elif feedback == "n":
            print("Oh, no! I've lost!")

        else:
            print("Please enter 'y' for Yes and 'n' for No!")


computer_guess_num()
