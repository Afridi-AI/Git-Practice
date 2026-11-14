import random


def play_round() -> bool:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number from 1 to 100.")

    while True:
        guess_text = input("Your guess: ").strip()
        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Choose a number between 1 and 100.")
            continue

        attempts += 1
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"You got it in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            return input("Play again? (y/n): ").strip().lower() == "y"


def main() -> None:
    print("Number Guessing Game")
    while play_round():
        pass
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
