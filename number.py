#!/usr/bin/python3

import random

class GuessNumber:
    def __init__(self):
        self.attempts_list = []
        self.attempts = 0

    @staticmethod
    def get_player_name():
        print("Hello traveller! Welcome to the game of guesses!")
        player_name = input("Enter your name: ")
        welcome = print("Hi, {}".format(player_name))
        return welcome

    @staticmethod
    def get_player_permission():
        wanna_play = input("Would you like to play the guessing game? (Enter Yes/No) ")
        return wanna_play

    @staticmethod
    def check_player_permission():
        if ((GuessNumber.get_player_permission().lower()) or (GuessNumber.get_player_play_again().lower()) in ("yes", "y")):
            GuessNumber.get_player_guess()
        else:
            print("That's cool, have a good one!")

    @staticmethod
    def get_player_guess():
        guess = int(input("Pick a number between 1 and 10\n"))
        if GuessNumber.is_validate_guess(guess) is True:
            return guess

    @staticmethod
    def is_validate_guess(guess):
        if guess < 1 or guess > 10:
            raise ValueError("Please guess a number within the given range")
        else:
            return True

    @staticmethod
    def get_player_play_again():
        play_again = input("Would you like to play again? (Enter Yes/No) ")
        return play_again

    def play_game():
        guessed_number = GuessNumber.get_player_guess()
        random_number = int(random.randint(1, 10))
        if guessed_number == random_number: print("Nice! You got it!")
        elif guessed_number > random_number: print("{} is higher than {}".format(guessed_number, random_number))
        else: print("{} is lower than {}".format(guessed_number, random_number))

    def continue_game():
        GuessNumber.get_player_play_again()
        GuessNumber.check_player_permission()
        GuessNumber.play_game()
        GuessNumber.continue_game()

    def main():
        GuessNumber.get_player_name()
        GuessNumber.check_player_permission()
        GuessNumber.play_game()
        GuessNumber.continue_game()

if __name__ == "__main__":
    GuessNumber.main()
     