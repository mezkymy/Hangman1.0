import random

with open('words.txt') as words:
    word_list = words.read().splitlines()

answer = random.choice(word_list).lower()
chances = 9
guesses = []
correct = []
answer_letters = list(set(answer))

print("==============================================")
print("| Welcome to the Even Shittier Hangman (ESH) |")
print("|                (Version 1.0)               |")
print("|    Try to guess the name of the fruit      |")
print("==============================================")

while chances > 0:
    print(f"Chances left: {chances}")
    print("\nGuess which letter you think is in the answer (one letter each guess, not case sensitive)")
    print("If you are confident enough, type the answer directly! \n")

    word_list = [] #create empty list

    for ans in answer:
        if ans in correct:
            word_list.append(ans)
        else:
            word_list.append("_")

    the_word = " ".join(word_list)
    print(f"The word: {the_word}")

    letters_guessed = ", ".join(guesses)
    print(f"Words/Letters guessed: {letters_guessed}")

    guess = input("Your guess: ").lower() # make all letters in guess lowercase

    if guess in guesses:
        print(f"You already guessed '{guess}'") ## if guess is a repeat, chances are not reduced
    else:
        if guess in answer_letters: ## if guess is correct, add to correct & guesses
            correct.append(guess)
            guesses.append(guess)
            chances -= 1
        else:
            guesses.append(guess) ## if guess is wrong, add to guesses
            chances -= 1

    ## Win/Lose Conditions
    if len(correct) == len(answer_letters):
        print(f"\nThe answer is: {answer}")
        print("You win!")
        break
    elif guess == answer:
        print(f"\nThe answer is: {answer}")
        print("You win!")
        break
    elif chances == 0:
        print("You ran out of chances")
        print(f"\nThe answer is: {answer}")
        print("You lost!")

