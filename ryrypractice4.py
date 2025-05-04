# Create a program that allows the user to try and guess a random number. The program should generate a random number,
# and allow the user to enter in guesses through the command line argument. The user gets unlimited number of guesses
# until they are within 50 digits of the actual answer, then they get a prompt saying they have 5 guesses left. If they
# do not get within 10 digits of the actual answer they lose. If they get within 10 digits of the actual answer, then
# they get another message saying their guesses are renewed, and they get 3 more guesses. If they do not guess the
# answer they lose, otherwise they win.


#0 - 1000
#print if higher or lower after every guess

import random
import sys

rng_num = random.randint(0,1000)
game_running = True

def numGuesser(rng_num:int, game_running:bool) -> str:
    """
    This program takes input from the user and compares it to the RNG value for a mini-game.
    """
    guesses_renewed = False
    guesses = 5
    within_10 = False

    while game_running == True:
        user_input = int(input("Give me your guess from 0 --> 1000:\n"))
        #print(f"For testing purposes, the rng_num is {rng_num}")
        if guesses > 0:
            if user_input > rng_num:
                print(f"Your guess is more than the number.\nGuesses remaining: {guesses}\n")
            elif user_input < rng_num:
                print(f"Your guess is less than the number.\nGuesses remaining: {guesses}\n")
            elif user_input == rng_num:
                print(f"You win you punk ass bitch.")
                game_running = False

            if (user_input >= (rng_num - 10) and user_input <= rng_num) or (user_input <= (rng_num + 10) and user_input >= rng_num):
                within_10 = True
                if guesses_renewed == False:
                    guesses += 3
                    print(f"You are within 10 digits of the actual answer.\n")
                    print(f"Your guesses are renewed. \nYou get 3 more guesses.\n\nGuesses remaining: {guesses}\n")
                    guesses_renewed = True

            if (user_input >= (rng_num - 50) and user_input <= rng_num) or (user_input <= (rng_num + 50) and user_input >= rng_num):
                if within_10 == True:
                    guesses = guesses - 1
                    continue
                print(f"You are within 50 digits of the actual answer.\nGuesses remaining: {guesses}\n")
                guesses = guesses - 1
        elif guesses <= 0:
            str(f"You lost. The number was {rng_num}. Git gud tbh.\n")
            game_running = False

    if game_running == False:
        return str(f"Exit function because game ended.\n")
    
numGuesser(rng_num, game_running)