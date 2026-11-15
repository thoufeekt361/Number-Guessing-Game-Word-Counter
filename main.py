import random
import string
from collections import Counter

def number_guessing_game():
    best_score = 0
    while True:
        print("\n========== NUMBER GUESSING GAME ==========")
        print("Guess a number between 1 and 100!")
        print("You have 7 attempts.")
        print("Scoring: 100 points - 10 points per wrong guess.")
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        score = 0
        won = False
        while attempts < max_attempts:
            try:
                guess = int(input("\nEnter your guess: "))

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue
            attempts += 1
            if guess == secret_number:
                print("\nCongratulations! You guessed correctly!")
                won = True
                score = max(0, 100 - (attempts - 1) * 10)
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            print("Attempts remaining:", max_attempts - attempts)
        if not won:
            print("\nGame over! You have used all your attempts.")
            print("The correct number was:", secret_number)
            score = 0
        print("\n---------- GAME RESULTS ----------")
        print("Total attempts:", attempts)
        print("Your score:", score)
        if score > best_score:
            best_score = score
        print("Best score:", best_score)
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again not in ["yes", "y"]:
            print("\nThanks for playing!")
            break

def count_words(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("\nFile not found:", path)
        print("Please make sure sample.txt exists in the project folder.")
        return None
    except OSError as error:
        print("\nError reading file:", error)
        return None
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    words = text.split()
    word_counts = Counter(words)
    return word_counts

def word_counter():
    print("\n========== WORD COUNTER ==========")
    file_path = input("Enter text file name (default: sample.txt): ").strip()
    if not file_path:
        file_path = "sample.txt"
    counts = count_words(file_path)
    if counts is None:
        return
    total_words = sum(counts.values())
    unique_words = len(counts)
    print("\n========== WORD COUNT RESULTS ==========")
    print("Total words:", total_words)
    print("Unique words:", unique_words)
    print("\n---------- TOP 10 MOST COMMON WORDS ----------")
    if not counts:
        print("The file is empty. No words found.")
        return
    print(f"{'Word':<20}{'Frequency':>10}")
    print("-" * 30)
    for word, frequency in counts.most_common(10):
        print(f"{word:<20}{frequency:>10}")

def main():
    while True:
        print("\n====================================")
        print("       PYTHON PROGRAMMING PROJECT")
        print("====================================")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Quit")
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("\nThank you for using this program!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()