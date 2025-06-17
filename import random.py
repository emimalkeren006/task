import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("\nWelcome to Rock-Paper-Scissors Game!")
    print("--------------------------------------")

    while True:
        print(f"\nRound {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if result == "win":
            print(" You win this round!")
            user_score += 1
        elif result == "lose":
            print(" You lose this round.")
            computer_score += 1
        else:
            print(" It's a tie!")

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again != 'yes':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        round_number += 1

if __name__ == "__main__":
    play_game()