import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please choose rock, paper, or scissors: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def play_again():
    play_more = input("Do you want to play another round? (yes/no): ").strip().lower()
    return play_more == "yes"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        display_result(user_choice, computer_choice, result)
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
