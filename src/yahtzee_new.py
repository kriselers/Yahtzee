import os
import random
import re
import sys

from hand import Hand
from scoreboard import Scoreboard
from yahtzee_rules import (
    Aces,
    Twos,
    Threes,
    Fours,
    Fives,
    Sixes,
    ThreeOfAKind,
    FourOfAKind,
    FibonYahtzee,
    FullHouse,
    SmallStraight,
    LargeStraight,
    Yahtzee,
    Chance,
)

class YahtzeeGame:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("""
            Welcome to Yahtzee!

            To begin, simply press [Enter] and follow the instructions on
            on the screen.

            To exit, press [Ctrl+C]
            """)

        # Begin by intatntiating the hand and scoreboard
        self.hand = Hand()
        self.scoreboard = Scoreboard()

        # Register the rules for Yahtzee
        self.scoreboard.register_rules([
            Aces(),
            Twos(),
            Threes(),
            Fours(),
            Fives(),
            Sixes(),
            ThreeOfAKind(),
            FourOfAKind(),
            FullHouse(),
            SmallStraight(),
            LargeStraight(),
            Yahtzee(),
            FinbonYahtzee(),
            Chance(),
        ])

    def show_scoreboard_points(self, hand: Hand = None):
        print("\nSCOREBOARD")
        print("=" * 50)
        print(self.scoreboard.points_overview(hand))
        print("=" * 50)

    def select_scoring(self):
        self.show_scoreboard_points(self.hand)
        while True:
            scoreboard_row = input("Choose which scoring to use: ")
            try:
                scoreboard_row_int = int(re.sub('[^0-9]', "", scoreboard_row))
                if scoreboard_row_int < 1 or scoreboard_row_int > self.scoreboard.rule_count():
                    print("Please select an existing scoring rule.")
                return self.scoreboard.get_rule(scoreboard_row_int - 1)
            except ValueError:
                print("You entered something other than a number. Please try again.")

    def choose_dice_reroll(self):
        while True:
            try:
                reroll = input("\nChoose which dice to re-roll "
                    "(comma-separated or 'all'), or 0 to continue: ")

                if reroll.lower() == "all":
                    return self.hand.all_dice()
                
                # Perform some clean-up of input
                reroll = reroll.replace(" ", "") # Remove spaces
                reroll = re.sub('[^0-9]', "", reroll)   # Remove non-numerals
                reroll = reroll.split(",")  # Turn string into list
                reroll = list(map(int, reroll)) # Turn strings in list to int
                
                if not reroll or 0 in reroll:
                    return []
                return reroll
            except ValueError:
                print("Invalid input. Please try again.")

    def do_turn(self):
        rolls = 0
        selected_dice = self.hand.all_dice()
        while True:
            print("\nRolling dice...")
            self.hand.roll(selected_dice)
            print(self.hand)
            rolls += 1

            # If we reach the maximum numbers of rolls, we're done
            if rolls >= 3:
                break

            # Choose which dice to reroll
            selected_dice = self.choose_dice_reroll()
            if not selected_dice:
                break

        rule = self.select_scoring()
        points = self.scoreboard.assign_points(rule, self.hand)
        print(f"Adding {points} points to {rule.name()}")
        self.show_scoreboard_points()
        input("\nPress [Enter] to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')  

    def play(self):
        # We keep going until the scoreboard is full
        for _ in range(self.scoreboard.rule_count()):
            self.do_turn()

        print("\nCongratulations! You finished the game!\n")
        self.show_scoreboard_points()
        print(f"Total points: {scoreboard.total_points()}")

if __name__ == "__main__":
    try:
        game = YahtzeeGame()
        game.play()
    except KeyboardInterrupt:
        print("\nExiting...")
