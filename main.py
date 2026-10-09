import random
import re
from collections import Counter
from pathlib import Path


def play_number_guessing_game():
    """Play a number guessing game and calculate a score."""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\n🎮 NUMBER GUESSING GAME")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        user_input = input(f"\nAttempt {attempts + 1}/{max_attempts} — Enter your guess: ").strip()
        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a whole number, such as 42.")
            continue

        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts += 1
        if guess == secret_number:
            score = (max_attempts - attempts + 1) * 10
            print(f"🎉 Correct! You guessed it in {attempts} attempt(s).")
            print(f"Your score: {score}")
            return
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    print(f"\nGame over! The number was {secret_number}.")
    print("Your score: 0")


def analyze_text_file():
    """Read a text file and display word, character, and frequency counts."""
    print("\n📝 WORD COUNTER")
    default_file = Path(__file__).parent / "sample.txt"
    entered_path = input(
        f"Enter a text file path (press Enter to use {default_file.name}): "
    ).strip()
    file_path = Path(entered_path).expanduser() if entered_path else default_file

    try:
        text = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        print("Check the path and try again.")
        return
    except (OSError, UnicodeError) as error:
        print(f"Could not read the file: {error}")
        return

    words = re.findall(r"\b[\w']+\b", text.lower(), flags=re.UNICODE)
    frequencies = Counter(words)

    print(f"\nFile: {file_path}")
    print(f"Total words: {len(words)}")
    print(f"Total characters (including spaces): {len(text)}")
    print(f"Unique words: {len(frequencies)}")
    if not frequencies:
        print("No words were found in this file.")
        return

    print("\nWord frequency:")
    for word, count in frequencies.most_common():
        print(f"  {word}: {count}")


def main():
    """Display the menu and run the selected feature."""
    while True:
        print("\n" + "=" * 38)
        print(" NUMBER GUESSING GAME & WORD COUNTER")
        print("=" * 38)
        print("1. Play Number Guessing Game")
        print("2. Analyze a Text File")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            play_number_guessing_game()
        elif choice == "2":
            analyze_text_file()
        elif choice == "3":
            print("Thanks for using the project. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
