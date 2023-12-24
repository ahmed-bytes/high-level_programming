"""A Hangman game."""
from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

word = choice(word_list)
length = len(word)

# A variable to hold blanks in place of the characters.
result = ["_" for _ in range(length)]
print(f"{' '.join(result)}")

# Keep prompting the user for a word to complete the sentence
gameEnd = False
counter = 5

while gameEnd == False:
    prompt = input("Guess a Letter: ").lower()

    if prompt in result:
        print("You've entered this Letter before!!")

    for i in range(length):
        if word[i] == prompt:
            result[i] = prompt
            print(f"{' '.join(result)}")

    if prompt not in word:
        print(stages[counter])
        print(f"The Letter '{prompt}' is not in the word, You lose a life :(")
        if counter == 0:
            print(f"The word you failed to guess is {word}")
            print("Game Over!!")
            gameEnd = True
        counter -= 1

    if "_" not in result:
        gameEnd = True
        print("Game Won!!")
