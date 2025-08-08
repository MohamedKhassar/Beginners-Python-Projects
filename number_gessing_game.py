from random import randint

def number_guessing_game():
    limit_guesses=int(input("Number of guesses: "))
    while True:
        try:
            min=int(input("minimum value: "))
            max=int(input("maximum value: "))
            if min<max:
                picked_number=randint(min,max)
                break
            else:
                print("minimum value must less than maximum value")
        except Exception:
           print("Please enter a valid value")
            
    tries=0
    i=0
    while i<limit_guesses:
        try:
            answer=int(input(f"Guess a number between {min} and {max}: "))
            tries+=1 
            if answer>picked_number:
                print("Too high!")
            elif answer < picked_number:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the number {picked_number} in {tries} {"tries" if tries>1 else "try"} 🎉🎊.")
                break
            i+=1
        except Exception:
               print("Please enter a valid number")
    else:
        print("You've reached your limit guesses")

                
number_guessing_game()