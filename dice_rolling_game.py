from random import randint

def rolling_pair_dice():
    roll_counter=0
    while True:
        answer =str(input("Roll the dice? (y/n): ")).lower()
        if answer=="y":
            dice_number=int(input("How many dice you want to roll?: "))
            dices=[]
            for _ in range(dice_number):
                dices.append(randint(1,6))
            roll_counter+=1
            print(f"You rolled {dices}, You rolled the dice {roll_counter} times")
        elif answer=="n":
            print("Thanks for playing")
            break
        else:
            print("Invalid Answer")
    
rolling_pair_dice()