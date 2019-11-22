# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kris Elers
#               Liam Estes
#               Brandi Sahualla
# Section:      523
# Assignment:   Lab 13
# Date:         20 November 2019
#

import random


def main_menu():
    print("1. Play")
    print("2. Instructions")
    print("3. Scoring")
    print("4. Quit")


def instructions():
    option = '0'
    waiting = True
    print("Yahtzee Instructions")
    print("The objective of Yahtzee is to score points by rolling five dice to make certain combinations.\n"
          "The dice can be rolled up to three times in a turn. A game consists of thirteen rounds. \n"
          "After each round the player chooses which scoring category is to be used for that round. \n"
          "Once a category is used in a game, it can't be used again. For reference to the scoring card \n"
          "Yahtzee uses, please refer to the scoring selection from the main menu.")
    while waiting:
        if option == "back":
            print()
            return
        else:
            option = input("Unrecognized command. Please enter 'back' to return to the menu: ")


# Function that will explain the score system of Yahtzee
def scoring():
    option = '0'
    waiting = True
    print("Yahtzee's Scoring System:")
    print("1. Sets of the same number (1's, 2's, 3's, etc.)")
    print("2. Three of a Kind - at least 3 dice of the same number; score is the sum of all five dice")
    print("3. Four of a Kind - at least 4 dice of the same number; score is the sum of all five dice")
    print("4. Small Straight - four consecutive numbers are represented (i.e 2345); the score is 30 points")
    print("5. Large Straight - five consecutive numbers are represented (i.e 23456); the score is 40 points")
    print("6. Full House - three of a kind, two of another (i.e. 33322); the score is 25 points")
    print("7. Yahtzee! - five of a kind; the score is 50 points")
    print("8. Chance - nothing special; score is the sum of all five dive")
    option = input("Enter 'back' to return to the menu: ")
    while waiting:
        if option == "back":
            print()
            return
        else:
            option = input("Unrecognized command. Please enter 'back' to return to the menu: ")


# Function that is playing the game of Yahtzee
def game():
    scoreCats = ["Three of a Kind", "Four of a Kind", "Small Straight", "Large Straight", "Full House", "Yahtzee",
                  "Chance"]
    setCats = ["Set of 1's", "Set of 2's", "Set of 3's", "Set of 4's", "Set of 5's", ""]
    results = [] * 5
    option = '0'
    roundNum = 1
    turn = 1
    while roundNum < 14:
        # TODO - write game function
        pass


# Function that will roll a given amount of dice
def roll():
    results = [random.randint(1, 6) for i in range(5)]
    return results


# Function that will roll a Yahtzee with a "special" input.
def rick_rolled():
    rng = random.randint(1, 6)
    temp = [rng] * 5
    return temp


def main():
    option = '0'
    while option != '4':
        print("Welcome to Yahtzee!")
        main_menu()
        option = input("Select Option: ")
        print()
        if option == '1':  # Play
            option = input("Start the game (y/n)?")
            game()
            continue
        elif option == '2':  # Instructions
            instructions()
            continue
        elif option == '3':  # Scoring
            scoring()
            continue
        elif option == '4':  # Quit
            print("Thanks for playing!")
            continue
        else:
            print("You entered an incorrect menu option. Please try again.")
            continue


main()  # Call to main
