import random

print("Welcome to my number guessing gaming challenge: ")
print("my chosen number is between 1 and 100")

# Pick a random number
number = random.randint(1, 100)
print(number)

# Difficulty

guess_Trial = 0

level = input("Choose a difficult, 'easy' or 'hard': ").lower()
playing = True

if level == 'easy':
    guess_Trial = 3
    print(f"YOU HAVE {guess_Trial} TRIAL ATTEMPTS")
elif level== 'hard':
    guess_Trial = 5
    print(f"YOU HAVE {guess_Trial} TRIAL ATTEMPTS")
else:
        print("Enter a valid choice")

while playing:

    # guessing
    choice = int(input("Guess a number: "))


    if choice == number:
        print("You Guessed The Correct Number🎉🎉")
        playing = False

    # Accuracy
    elif choice > number:
        print("Too high")
        guess_Trial -= 1
        print(f"you have {guess_Trial} chances left")
    
    elif choice < number:
        print("Too low")
        guess_Trial -= 1
        print(f"you have {guess_Trial} chances left")

    if guess_Trial == 0:
        print("SORRY, you loss\n, try again")
        playing = False

        