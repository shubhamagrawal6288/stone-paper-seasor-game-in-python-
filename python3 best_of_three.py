import random

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (stone, paper, scissors): ").lower()
    while user_input not in ['stone', 'paper', 'scissors']:
        print("Invalid choice, try again.")
        user_input = input("Enter your choice (stone, paper, scissors): ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return "user"
    else:
        return "computer"

def play_game():
    user_wins = 0
    computer_wins = 0
    rounds = 0

    while user_wins < 2 and computer_wins < 2:  # Best of 3, so first to 2 wins
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            user_wins += 1
            print("You win this round!\n")
        elif result == "computer":
            computer_wins += 1
            print("Computer wins this round!\n")
        else:
            print("This round is a tie!\n")

        rounds += 1
        print(f"Score: You {user_wins} - Computer {computer_wins}\n")

    if user_wins > computer_wins:
        print("Congratulations! You win the best of three!")
    else:
        print("Computer wins the best of three. Better luck next time!")

if __name__ == "__main__":
    play_game()
