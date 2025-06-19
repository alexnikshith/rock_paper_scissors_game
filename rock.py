import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

options = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(options)

def get_user_choice():
    while True:
        choice = input(Fore.YELLOW + "Enter your choice (rock, paper, scissors): ").lower()
        if choice in options:
            return choice
        print(Fore.RED + "Invalid choice! Please try again.")

def animate_countdown():
    for word in ["Rock...", "Paper...", "Scissors...", "Shoot!"]:
        print(Fore.CYAN + word)
        time.sleep(0.5)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    print(Fore.MAGENTA + "\n🎮 Welcome to Rock-Paper-Scissors!")
    
    rounds = int(input(Fore.YELLOW + "How many rounds do you want to play? "))
    player_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(Fore.BLUE + f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        animate_countdown()
        print(f"You chose: {Fore.GREEN + user_choice}")
        print(f"Computer chose: {Fore.RED + computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print(Fore.CYAN + "It's a tie!")
        elif winner == "player":
            print(Fore.GREEN + "You win this round!")
            player_score += 1
        else:
            print(Fore.RED + "Computer wins this round!")
            computer_score += 1

    # Game summary
    print(Fore.MAGENTA + "\n=== Game Over ===")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")

    if player_score > computer_score:
        print(Fore.GREEN + "🎉 Congratulations! You won the game!")
    elif computer_score > player_score:
        print(Fore.RED + "💻 Computer wins the game!")
    else:
        print(Fore.CYAN + "It's a tie overall!")

# Start the game
play_game()
