from random import choice

choices = {"r": "🪨", "p": "📃", "s": "✂️"}


def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    while True:
        computer_choice = choice(list(choices.keys()))
        player_choice = str(input("Rock, paper, or scissors? (r/p/s): "))
        if player_choice in list(choices.keys()):
            print(f"""
            You chose {choices[player_choice]}
            Computer chose: {choices[computer_choice]}
            """)
            if (computer_choice == "r" and player_choice == "s") or (computer_choice == "p" and player_choice == "r") or (computer_choice == "s" and player_choice == "p"):
                print("You lost 😥")
                computer_score += 1
            elif computer_choice==player_choice:
                print("Draw 🤝")
            else:
                print("You Won 🎉")
                player_score += 1
            print(f"""
            computer {computer_score} - {player_score} player
            """)
            while True:
                ask_to_continue = input(
                    "Do you want to continue? (y/n): ").lower()
                if ask_to_continue == "y":
                    break
                elif ask_to_continue == "n":
                    print("Thanks for playing!")
                    return 0
                else:
                    print("Invalid Answer!")
        else:
            print("Invalid Choice!")


rock_paper_scissors()
