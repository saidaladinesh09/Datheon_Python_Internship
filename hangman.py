
import random

with open("google-10000-english-no-swears.txt", "r", encoding="utf-8") as file:
    words = [
        word.strip().upper()
        for word in file
        if word.strip().isalpha() and 4 <= len(word.strip()) <= 10
    ]

hangman_stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

secret_word = random.choice(words)
guessed_letters = set()
wrong_attempts = 0
max_attempts = 6

print("===== HANGMAN WORD GUESSING GAME =====")

while wrong_attempts < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts:", wrong_attempts, "/", max_attempts)
    print(hangman_stages[wrong_attempts])

    if all(letter in guessed_letters for letter in secret_word):
        break

    guess = input("Guess a letter: ").upper().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

print("\n===== GAME RESULT =====")

if all(letter in guessed_letters for letter in secret_word):
    print("Congratulations! You Won!")
else:
    print(hangman_stages[6])
    print("Game Over! You Lost!")

print("Secret word was:", secret_word)
