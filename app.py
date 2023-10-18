#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
# Import the random module to generate computer's choice
import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#write 'Hello World' to the console
print("Hello World, let's play rock, paper, scissors!")

# Import the random module to generate computer's choice
import random

# Define a function to play the game
def play_game():
    # Define a list of valid options
    valid_options = ['rock', 'paper', 'scissors']
    
    # Initialize player's score, number of wins, and number of rounds
    player_score = 0
    num_wins = 0
    num_rounds = 0
    
    # Start the game loop
    while True:
        # Ask the player for their choice
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        
        # Validate the player's choice
        if player_choice not in valid_options:
            print("Invalid option. Please choose again.")
            continue
        
        # Generate computer's choice
        computer_choice = random.choice(valid_options)
        
        # Determine the winner
        if player_choice == computer_choice:
            print("Computer chose: {}. Tie!".format(computer_choice))
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("Computer chose: {}. You win!".format(computer_choice))
            player_score += 1
            num_wins += 1
        else:
            print("Computer chose: {}. You lose!".format(computer_choice))
        
        # Increment the number of rounds
        num_rounds += 1
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    # Print the final score, number of wins, and number of rounds
    print("Your score: {}".format(player_score))
    print("Number of wins: {}".format(num_wins))
    print("Number of rounds: {}".format(num_rounds))

# Call the play_game function to start the game
play_game()