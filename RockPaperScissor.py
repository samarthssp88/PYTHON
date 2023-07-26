'''Write a program that allows the user to play a game of Rock Paper Scissors against the computer.
The program should prompt the user to enter their choice (Rock, Paper, or Scissors) and
then randomly generate a choice for the computer.
The program should then determine the winner based on the following rules:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock'''
#####################################

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().capitalize()
        if user_choice in {"Rock", "Paper", "Scissors"}:
            return user_choice
        print("Invalid input. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "Rock":
        return "You win!" if computer_choice == "Scissors" else "Computer wins!"
    elif user_choice == "Scissors":
        return "You win!" if computer_choice == "Paper" else "Computer wins!"
    else: #user_choice == "Paper"
        return "You win!" if computer_choice == "Rock" else "Computer wins!"

def main():
    print("Let's play Rock Paper Scissors against the computer!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
