import random

def play_hangman():
    # Predefined list of 5 words
    word_list = ["python", "codealpha", "developer", "program", "internship"]
    
    # Randomly select a secret word and convert it to lowercase
    secret_word = random.choice(word_list)
    
    # Track correctly guessed letters and incorrect guesses
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("========================================")
    print("      WELCOME TO HANGMAN GAME!          ")
    print("========================================")
    print(f"Guess the hidden word. You have {max_incorrect} incorrect attempts allowed.\n")

    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Build the current word display (e.g., "p y t _ o n")
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        
        current_display = " ".join(display_word)
        print(f"Word: {current_display}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Check if player has guessed the complete word
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly:", secret_word)
            break

        # Get letter input from player
        guess = input("Guess a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.\n")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.\n")
            continue

        # Add the valid guess to set of guessed letters
        guessed_letters.add(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{guess}' is not in the word.\n")

    # Game over condition if max attempts reached
    if incorrect_guesses == max_incorrect:
        print("========================================")
        print("❌ GAME OVER!")
        print(f"You ran out of guesses. The word was: {secret_word}")
        print("========================================")

if __name__ == "__main__":
    play_hangman()
