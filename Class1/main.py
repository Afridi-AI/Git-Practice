import random


   

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
