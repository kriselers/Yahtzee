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
    print("4. Tutorial")
    print("5. Quit")


def tutorial():
    waiting = True
    print("Upon starting the game, the user will be asked if they're ready to start the game. Inputting 'y' will roll\n"
          "the dice and begin the game. Any other input will bring the user back to the main menu. \n"
          "Once a roll is completed, the user will be asked how many dice they're going to keep followed by which \n"
          "dice they'd like to keep. Then they'll be presented with a menu to roll the remaining dice, \n"
          "view this menu, view the current score, or quit the game. This will continue for 13 total turns until the\n"
          "game is completed or the user quits, then the final score will be displayed. Then the user will be \n"
          "prompted to return the main menu.")

    while waiting:
        choice = input("Go back (y)? ")
        if choice == "y":
            print()
            return
        else:
            print("Unrecognized command. Please enter 'y' to return to the menu.")


def instructions():
    waiting = True
    print("\nYahtzee Instructions")
    print("The objective of Yahtzee is to score points by rolling five dice to make certain combinations.\n"
          "The dice can be rolled up to three times in a turn. A game consists of thirteen rounds. \n"
          "After each round the player chooses which scoring category is to be used for that round. \n"
          "Once a category is used in a game, it can't be used again. For reference to the scoring card \n"
          "Yahtzee uses, please refer to the scoring selection from the main menu.\n")

    while waiting:
        choice = input("Go back (y)? ")
        if choice == "y":
            print()
            return
        else:
            print("Unrecognized command. Please enter 'y' to return.")


# Function that will erick_rolled()plain the score system of Yahtzee
def scoring():
    waiting = True
    print("Yahtzee's Scoring System:")
    print("1. Sets of the same number (1's, 2's, 3's, etc.); score is the sum of all dice")
    print("2. Three of a Kind - at least 3 dice of the same number; score is the sum of all five dice")
    print("3. Four of a Kind - at least 4 dice of the same number; score is the sum of all five dice")
    print("4. Small Straight - four consecutive numbers are represented (i.e 2345); the score is 30 points")
    print("5. Large Straight - five consecutive numbers are represented (i.e 23456); the score is 40 points")
    print("6. Full House - three of a kind, two of another (i.e. 33322); the score is 25 points")
    print("7. Yahtzee! - five of a kind; the score is 50 points")
    print("8. Chance - nothing special; score is the sum of all five dive")

    while waiting:
        choice = input("Go back (y)? ")
        if choice == "y":
            print()
            return
        else:
            print("Unrecognized command. Please enter 'y' to return.")


def get_score(uppercar, upperscor, lowercar, lowerscor, t):
    print("1. %s  - %d \t\t 8. %s - %d" % (lowercar[0], int(lowerscor[0]), uppercar[1], int(upperscor[1])))
    print("2. %s - %d \t\t 9. %s - %d" % (lowercar[1], int(lowerscor[1]), uppercar[2], int(upperscor[2])))
    print("3. %s - %d \t\t 10. %s - %d" % (lowercar[2], int(lowerscor[2]), uppercar[3], int(upperscor[3])))
    print("4. %s - %d \t\t 11. %s - %d" % (lowercar[3], int(lowerscor[3]), uppercar[4], int(upperscor[4])))
    print("5. %s - %d \t\t 12. %s - %d" % (lowercar[4], int(lowerscor[4]), uppercar[5], int(upperscor[5])))
    print("6. %s - %d \t\t 13. %s - %d" % (lowercar[5], int(lowerscor[5]), uppercar[6], int(upperscor[6])))
    print("7. %s - %d \t\t Total Score - %d\n" % (uppercar[0], upperscor[0], t))
    return


def calculate_round_score(card, cardScore, roundRoll, x):
    needInput = True
    dice = [0, 0, 0, 0, 0, 0, 0]
    for i in range(5):
        dice[roundRoll[i]] = dice[roundRoll[i]] + 1
    while needInput:
        index = x - 1
        if 0 < x <= 6:
            cardScore[index] = sum(roundRoll)
        elif 6 < x < 14:
            index = x - 7
            if x == 7:
                if 3 in dice:  # Three of a kind
                    cardScore[index] = sum(roundRoll)
                else:
                    x = int(input("You did not have three of a kind in your roll. Enter another category: "))
            elif x == 8:  # Four of a kind
                if 4 in dice:
                    cardScore[index] = sum(roundRoll)
                else:
                    x = int(input("You did not have four of a kind in your roll. Enter another category: "))
            elif x == 9:  # Small Straight
                string = ''
                for i in dice:
                    string += str(i)
                if '1111' in string or '1112' in string or '1121' in string or '1211' in string or '2111' in string:
                    cardScore[index] = 30
                else:
                    x = int(input("You did not a small straight in your dice set. Enter another category: "))
            elif x == 10:  # Large straight
                string = ''
                for i in dice:
                    string += str(i)
                if '11111' in string:
                    cardScore[index] = 40
                else:
                    x = int(input("You did not a large straight in your dice set. Enter another category: "))
            elif x == 11:  # Full House
                if 3 in dice and 2 in dice:
                    cardScore[index] = 25
                else:
                    x = int(input("You did not have a full house in your dice set. Enter another category: "))
            elif x == 12:  # Yahtzee
                if 5 in dice:
                    cardScore[index] = 50
                else:
                    x = int(input("You did not have a Yahtzee in your dice set. Enter another category: "))
            elif x == 13:  # Chance
                cardScore[index] = sum(roundRoll)
        needInput = False


# Function that is playing the game of Yahtzee
def game():
    upperCats = ["Three of a Kind", "Four of a Kind", "Small Straight", "Large Straight", "Full House", "Yahtzee",
                 "Chance"]
    upperScores = [0] * 7
    lowerCats = ["Set of 1's", "Set of 2's", "Set of 3's", "Set of 4's", "Set of 5's", "Set of 6's"]
    lowerScores = [0] * 6
    totalScore = 0
    turnNum = 1
    blah = 0

    while turnNum < 14:
        needInput = True
        dice = 5
        rollResults = [0] * 5
        roundResults = []
        rolls = 1
        # Displaying the menu after each turn
        if turnNum == 1:
            pass
        else:
            dice = 5
            while needInput:
                print("1. Roll again")
                print("2. Display Instructions")
                print("3. Display Current Score")
                print("4. Quit Game")
                choice = input("Select Option: ")
                if choice == '1':
                    needInput = False
                elif choice == '2':
                    instructions()
                elif choice == '3':
                    get_score(upperCats, upperScores, lowerCats, lowerScores, totalScore)
                elif choice == '4':
                    print("\nFINAL SCORE")
                    get_score(upperCats, upperScores, lowerCats, lowerScores, totalScore)
                    return
                else:
                    print("You entered an incorrect option. Please try again.\n")

        print("\nTurn", turnNum, "\b:")
        # For the three rolls per turn
        while rolls <= 3:
            rollResults = roll(dice)
            # Printing roll results
            print("Rolled:", end=" ")
            for i in rollResults:
                print(i, end=" ")

            needInput = True
            # Making sure the user inputs a valid amount of dice to keep
            while needInput:
                if rolls == 3:
                    break
                blah = int(input("\nHow many dice would like like to keep: "))
                if blah == 0:
                    needInput = False
                else:
                    dice -= blah
                    if dice >= 0:
                        needInput = False
                    else:
                        print("You can't keep", blah, "dice. Please try again.")

            needInput = True
            # Making sure the user is keeping dice that were actually rolled
            while needInput:
                if rolls == 3:
                    keeping = ""
                    for i in rollResults:
                        keeping += str(i) + ","
                    temp = [x.strip() for x in keeping.split(',')]
                    del temp[-1]
                    kept = [int(x) for x in temp]
                    for ele in range(len(kept)):
                        roundResults.append(kept[ele])
                    needInput = False
                elif blah == 0:
                    needInput = False
                else:
                    keeping = input("Which dice would you like to keep? Please separate your numbers by commas "
                                    "(i.e. 3, 3, 3): ")
                    temp = [x.strip() for x in keeping.split(',')]
                    kept = [int(x) for x in temp]
                    exists = all((elm in rollResults for elm in kept))
                    if exists:
                        for i in range(len(kept)):
                            roundResults.append(kept[i])
                        needInput = False
                    else:
                        print("You're trying to keep a set of dice that weren't rolled. Please try again.")

            needInput = True
            # Seeing if the user wants to roll again, or end their turn.
            while needInput:
                if rolls >= 3:
                    print("\n\n1. %s\t8. %s" % (lowerCats[0], upperCats[1]))
                    print("2. %s\t9. %s" % (lowerCats[1], upperCats[2]))
                    print("3. %s\t10. %s" % (lowerCats[2], upperCats[3]))
                    print("4. %s\t11. %s" % (lowerCats[3], upperCats[4]))
                    print("5. %s\t12. %s" % (lowerCats[4], upperCats[5]))
                    print("6. %s\t13. %s" % (lowerCats[5], upperCats[6]))
                    print("7. %s" % upperCats[0])
                    print("Current dice are:", end=" ")
                    for i in roundResults:
                        print(i, end=" ")
                    while needInput:
                        choice = int(input("\nPlease choose the category you'd like to save this turn to: "))
                        if 0 < choice < 7:
                            if lowerScores[choice] == 0:
                                calculate_round_score(lowerCats, lowerScores, roundResults, choice)
                                needInput = False
                            else:
                                print("You've already used the '%s' category. Please select another." %
                                      lowerCats[choice])
                        elif 6 < choice < 14:
                            temp = choice - 7
                            if upperScores[temp] == 0:
                                calculate_round_score(upperCats, upperScores, roundResults, choice)
                                needInput = False
                            else:
                                print("You've already used the '%s' category. Please select another."
                                      % upperCats[temp])
                        rolls += 1
                        turnNum += 1
                        totalScore = sum(upperScores) + sum(lowerScores)
                else:
                    print("Current dice are:", end=" ")
                    if len(roundResults) == 0:
                        print("None")
                    else:
                        for i in roundResults:
                            print(i, end=" ")
                    choice = input("\nRoll again (y/n)? ")
                    if choice == 'y':
                        rolls += 1
                        needInput = False
                    elif choice == 'n':
                        rolls = 4
                    else:
                        print("Invalid input. Please try again")
    return


# Function that will roll a given amount of dice
def roll(x):
    results = [random.randint(1, 6) for i in range(x)]
    return results


def main():
    option = '0'
    while option != '5':
        print("Welcome to Yahtzee!")
        main_menu()
        option = input("Select Option: ")
        print()
        if option == '1':  # Play
            option = input("Start the game (y/n)? ")
            if option == 'y':
                game()
            elif option == 'n':
                print("Returning to menu...\n")
                continue
            else:
                print("Invalid input. Please read the tutorial and try again. Returning to main menu...")
                continue
        elif option == '2':  # Instructions
            instructions()
            continue
        elif option == '3':  # Scoring
            scoring()
            continue
        elif option == '4':  # How to Play
            tutorial()
            continue
        elif option == '5':  # Quit
            print("Thanks for playing!")
            continue
        else:
            print("You entered an incorrect menu option. Please try again.\n")
            continue


main()  # Call to main
