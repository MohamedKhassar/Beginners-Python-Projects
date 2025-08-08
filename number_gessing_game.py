from random import randint

def number_guessing_game():
    picked_number=randint(1,100)
    while True:
        try:
            answer=int(input("Guess a number between 1 and 100: "))
            if answer>picked_number:
                print("Too high!")
            elif answer < picked_number:
                print("Too low!")
            else:
                print("Congratulations! You guessed the number 🎉🎊.")
                break
        except Exception:
               print("Please enter a valid number")

                
number_guessing_game()