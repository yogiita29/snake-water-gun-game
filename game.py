import random

def determine_winner(player1_choice, player2_choice):
    """Determine the winner between two players."""
    if player1_choice == player2_choice:
        return "Draw"
    elif (player1_choice == "Snake" and player2_choice == "Water") or \
         (player1_choice == "Water" and player2_choice == "Gun") or \
         (player1_choice == "Gun" and player2_choice == "Snake"):
        return "Player 1"
    else:
        return "Player 2"

def get_choice(player):
    """Prompt the player to input their choice."""
    while True:
        choice = input(f"{player}, enter your choice (Snake, Water, Gun): ").capitalize()
        if choice in ["Snake", "Water", "Gun"]:
            return choice
        print("Invalid choice. Please enter Snake, Water, or Gun.")

def multiplayer_mode():
    """Multiplayer mode for two players."""
    print("\nMultiplayer Mode")
    player1_score, player2_score = 0, 0

    for round_num in range(1, 6):  # Play 5 rounds
        print(f"\nRound {round_num}")
        player1_choice = get_choice("Player 1")
        player2_choice = get_choice("Player 2")

        winner = determine_winner(player1_choice, player2_choice)

        if winner == "Player 1":
            player1_score += 1
            print("Player 1 wins this round!")
        elif winner == "Player 2":
            player2_score += 1
            print("Player 2 wins this round!")
        else:
            print("This round is a draw!")

        print(f"Current Score: Player 1: {player1_score} | Player 2: {player2_score}")

    if player1_score > player2_score:
        print("\nPlayer 1 wins the game!")
    elif player2_score > player1_score:
        print("\nPlayer 2 wins the game!")
    else:
        print("\nThe game is a draw!")

def singleplayer_mode():
    """Single-player mode against the computer."""
    print("\nSingle Player Mode")
    player_score, computer_score = 0, 0

    for round_num in range(1, 6):  # Play 5 rounds
        print(f"\nRound {round_num}")
        player_choice = get_choice("Player")
        computer_choice = random.choice(["Snake", "Water", "Gun"])

        print(f"You chose {player_choice}, and the computer chose {computer_choice}.")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "Player 1":
            player_score += 1
            print("You win this round!")
        elif winner == "Player 2":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("This round is a draw!")

        print(f"Current Score: You: {player_score} | Computer: {computer_score}")

    if player_score > computer_score:
        print("\nYou win the game!")
    elif computer_score > player_score:
        print("\nThe computer wins the game!")
    else:
        print("\nThe game is a draw!")

def main():
    """Main function to run the game."""
    print("Welcome to the Snake Water Gun Game!")
    while True:
        mode = input("\nChoose mode: 1 for Single Player, 2 for Multiplayer, 0 to Exit: ").strip()
        if mode == "1":
            singleplayer_mode()
        elif mode == "2":
            multiplayer_mode()
        elif mode == "0":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
