
import random

GUI_WINDOW_TITLE = "Rock-Paper-Scissors"
WELCOME_MESSAGE = "Pershendetje mirsevini ne lojen time"
GUI_PROMPT_MESSAGE = "Ju lutem Zgjidhni nje opsion:"

WIN_MESSAGE = "Ju lumte Ju fituat!"
LOSE_MESSAGE = "Oh, Kompjuteri fitoj. Por ska Problem."
TIE_MESSAGE = "Barazim Provoni Perseri."

def random_choice(options=["rock", "paper", "scissors"]):
    return random.choice(options)

def determine_winner(choice1, choice2):
 

    if choice1 == choice2:
        winner = None 
    else:
        choices = [choice1, choice2]
        choices.sort() 

        if choices == ["paper", "rock"]:
            winner = "paper"
        elif choices == ["paper", "scissors"]:
            winner = "scissors"
        elif choices == ["rock", "scissors"]:
            winner = "rock"
        else:
            raise ValueError("OOPS, SOMETHING WENT WRONG")

    winners = {
        "rock":{
            "rock": None, 
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, 
        },
    }

    
    winner = winners[choice1][choice2]

    return winner

if __name__ == "__main__":

    print("-------------------")
    print("Launching the game...")
    print("-------------------")

    options = ["rock", "paper", "scissors"]

    user_choice = input("Ju lutem Zgjidhni 'rock', 'paper', or 'scissors': ")

    if user_choice in options:
        print("Ti zgjodhe:", user_choice)
    else:
        print("Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again.")
        exit()

    computer_choice = random_choice(options)
    print("Kompjuteri zgjodhi:", computer_choice)
    print("-------------------")

    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            print(WIN_MESSAGE)
        elif winning_choice == computer_choice:
            print(LOSE_MESSAGE)
    else:
        print(TIE_MESSAGE)

    print("Faleminderit qe luajtet, Ju lutem Luani Perseri!")
