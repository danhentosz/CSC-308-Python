# CSC 308 Python || Assignment 7
# Daniel Hentosz,  Casey Crowley, Tristan Rice, Ji Sue Lee
# hen3883@calu.edu, cro8478@calu.edu, ric5712@calu.edu, lee8474@calu.edu

# To generate random numbers.
import random


# Our main method.
def main():
    # The user will start with 100 chips.
    chips = 100
    # Our variable to see if the user wants to play again.
    again = 1
    # Will loop until the user decides to quit.
    while again == 1:
        # Creating a list by calling our getnums method.
        nums = gennums()
        # Getting the users bet.
        bet = getbet(chips)
        # Getting which game the user wants to play.
        choice = game()
        # Doing the math of the chips remaining.
        # Will NOT throw an exception as all were handled.
        chips = chips + play(nums, bet, choice)
        print("You have", chips, "chips left")
        # Is the user out of chips? If so end the game.
        if chips <= 0:
            print("You're out of chips, game over.")
            again = 2
        # If more chips remain, ask if they would like to play again.
        else:
            # pronpt will return 1 or 2.
            again = prompt()


# Creates and returns a list of size 7 with random single digit numbers.
# RECIVES: Nothing.
# RETURNES: A list of size 7 filled with random single digit numbers
# REQUIRES: Nothing.
def gennums():
    # Setting our list size.
    nums2 = [0] * 7
    # Filling our list with random single digit numbers.
    for i in range(len(nums2)):
        nums2[i] = random.randint(0, 9)
    # Returning the list.
    return nums2


# Gets and returns the bet the user places.
# RECIVES: The number of chips ramining.
# RETURNS: The users bet.
# REQUIRES: All bets must be 1-10, provided the user has enugh chips remaining
def getbet(rem):
    while True:
        try:
            print("You have", rem, "chips remaining.\nHow many chips do you want to bet?\n")
            bet = int(input())
            if bet >= 1 and bet <= 10 and bet <= rem:
                return bet
            else:
                print("Invalid number of chips")
        except:
            print("Invalid input")


# Gets the game the user wishes to play.
# RECIVES: Nothing.
# RETURNES: The users choice(1, 2, or 3- for each game respectively).
# REQUIRES: Nothing.
def game():
    while True:
        try:
            pick = int(input("PRESS 1: To play pick 1\nPRESS 2: To play pick 2\nPRESS 3: To play jumbo 7\n"))
            if pick >= 1 and pick <= 3:
                return pick
            else:
                print("Invalid range")
        except:
            print("Invalid Input")


# Plays the game the user picked.
# RECIVES: The random number list, the users bet, and the game the user chose.
# RETURNES: The number of chips the user lost, or gained.
# REQUIRES: A list of size 7 filled with single digit numbers, a bet in the range 1-10, and a game(1, 2, or 3).
def play(nums, bet, game):
    good = False
    while not good:
        try:
            if game == 1:
                l1 = [nums[0], nums[1], nums[2]]
                pick1 = int(input("Pick a number: "))
                good = True
                if l1.__contains__(pick1) and validrange(pick1):
                    chipsReturn = bet
                elif not validrange(pick1):
                    good = False
                    print("Pick a number 0-9.")
                else:
                    chipsReturn = bet - (bet * 2)
            elif game == 2:
                l1 = [nums[0], nums[1], nums[2]]
                pick1 = int(input("Pick your first number: "))
                pick2 = int(input("Pick your second number: "))
                good = True
                if l1.__contains__(pick1) and validrange(pick1) and l1.__contains__(pick2) and validrange(pick2):
                    chipsReturn = bet * 2
                elif not validrange(pick1) or not validrange(pick2):
                    good = False
                    print("Pick a number 0-9.")
                else:
                    chipsReturn = bet - (bet * 2)
            else:
                therenums = []
                for i in range(7):
                    good = False
                    while not good:
                        print("Enter number ", i + 1, ": ", sep="")
                        num = int(input())
                        if validrange(num):
                            therenums.append(num)
                            good = True
                        else:
                            print("Enter a number 0-9")
                count = 0
                for i in range(7):
                    if nums[i] == therenums[i]:
                        count += 1
                good = True
                if count == 7:
                    chipsReturn = bet * 50
                elif count == 6:
                    chipsReturn = bet * 25
                elif count == 5:
                    chipsReturn = bet * 15
                elif count == 4:
                    chipsReturn = bet * 5
                elif count == 3:
                    chipsReturn = bet * 3
                else:
                    chipsReturn = bet - (bet * 2)
        except:
            print("Invalid input.")
            good = False
    return chipsReturn


# Prompts the user if they want to play again.
# RECIVES: Nothing.
# RETURNES: The integer 1 or 2, indicating if they want to play again.
# REQUIRES: Nothing.
def prompt():
    good = False
    while not good:
        try:
            print("Would you like to play again?\nPRESS 1: for yes\nPRESS 2: for no")
            again = int(input())
            if again == 1 or again == 2:
                good = True
            if good:
                return again
        except:
            print("Invalid input")
            good = False


# Checks if the user entered a valid guess when playing any of our games.
# RECIVES: The guess the user entered(any integer).
# RETURNES: True if the guess is in the valid range, else false.
# REQUIRES: Nothing.
def validrange(a):
    if a >= 0 and a < 10:
        return True
    else:
        return False


# Calling main to execute our program.
main()
