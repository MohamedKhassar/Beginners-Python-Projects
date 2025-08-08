from random import choice

choices = {"r": "🪨", "p": "📃", "s": "✂️"}
computer_score = 0
player_score = 0


def ask_to_play():
    while True:
        player_choice = str(input("Rock, paper, or scissors? (r/p/s): "))
        if player_choice not in choices:
            print("Invalid choice! Please choose r, p, or s.")
            continue
        else:
            return player_choice


def print_choices(player_choice, computer_choice):
    print(f"""
    You chose: {choices[player_choice]}
    Computer chose: {choices[computer_choice]}
    """)


def check_winner(player_choice, computer_choice):
    global player_score
    global computer_score
    if (computer_choice == "r" and player_choice == "s") \
            or (computer_choice == "p" and player_choice == "r")\
            or (computer_choice == "s" and player_choice == "p"):

        # Computer wins
        print("You lost 😥")

        # Increment computer score
        computer_score += 1

    # Check if draw
    elif computer_choice == player_choice:
        print("Draw 🤝")

    # Check if the player wins
    else:
        # Player wins
        print("You Won 🎉")
        # Increment player score
        player_score += 1

    # Print scores
    print_scores(computer_score, player_score)


def print_scores(computer_score, player_score):
    print(f"""
    Computer {computer_score} - {player_score} Player
    """)


def rock_paper_scissors():
    while True:

        # Computer choice
        computer_choice = choice(list(choices.keys()))

        #  Player choice
        player_choice = ask_to_play()

        # Print choices
        print_choices(player_choice, computer_choice)

        # Check if the computer wins
        check_winner(player_choice, computer_choice)

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


rock_paper_scissors()
