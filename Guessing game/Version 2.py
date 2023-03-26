import random


def computer_guess_num():
    possible_num = list(range(1, 11))

    max_lives = 4
    min_lives = 1

    feedback = ""
    guess = 0

    print("Think of a number between 1 and 10.")
    while max_lives > min_lives:

        max_lives -= 1

        if feedback == "c":
            print("Yey! I've guessed it!")
            return

        elif feedback == "l":
            possible_num = [num for num in possible_num if num < guess]

        elif feedback == "h":
            possible_num = [num for num in possible_num if num > guess]

        elif feedback == "":
            pass

        else:
            while feedback != "h" and feedback != "l" and feedback != "c":
                print("Please enter 'h' for Higher, 'l' for lower or 'c' for Correct.")
                print("-------------------------------------------------------------")
                feedback = input("Is it 'h' - Higher, 'l' - lower or 'c' - Correct: ")

        if len(possible_num) == 0:
            print("Not possible!")
            return

        guess = random.choice(possible_num)
        print(f"Lives: {max_lives}")
        print(f"Number: {guess}")

        if max_lives != 1:
            feedback = input("Is it 'h' - Higher, 'l' - lower or 'c' - Correct: ")

        print("-------------------------------------------------------------")

    else:
        if guess == 10 or guess == 1:
            print("Yay! Somehow I did win.")

        else:
            print("Oh, no! I've lost!")


computer_guess_num()
