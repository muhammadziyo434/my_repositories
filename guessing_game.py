import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess and (number_to_guess - guess >= 10):
                print("Too low! Try again.")
            elif guess > number_to_guess and (guess-number_to_guess <= 10 ):
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                a=input("Do you want to continue (Y/N) :")
                if a.lower()=="yes" or a.lower()=='y' :
                    continue
                else :
                    print("Good bye 👋")
                    break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()