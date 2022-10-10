#import the random module
import random

#Create a list of the options
options = ["rock", "paper", "scissos"]

#Randomly pick one
def get_computer_choice():
    pick_one = random.choice(options)
    return pick_one
  
    

#Let the user input thier choice
def get_user_choice():
    while True:
        choice = input("input your choice: ")
        if choice not in options:
            print("invalid choice, try again: ")
        else:
            return choice   
    
def get_winner(computer_choice, user_choice):

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

        return get_winner(computer_choice, user_choice)


def play():
    user = get_user_choice()
    computer = get_computer_choice()
    results = get_winner(computer, user)
    
play()   