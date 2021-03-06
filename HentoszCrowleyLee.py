# CSC 308 Assignment 7 || Program 2 Assignment 7
# Daniel Hentosz,  Casey Crowley, Ji Sue Lee
# hen3883@calu.edu, cro8478@calu.edu, lee8472@calu.edu


import random


def main():
    chips = 100
    again = 1
    while again == 1:
        nums = gennums()
        bet = getbet(chips)
        choice = game()
        chips = chips + play(nums, bet, choice)
        print("You have", chips, "chips left")
        if chips <= 0:
            print("You're out of chips, game over.")
            again = 2
        else:
            again = prompt()


# Call main
def gennums():
    nums2 = [0] * 7
    for i in range(len(nums2)):
        nums2[i] = random.randint(0, 9)
    return nums2


def getbet(rem):
    while True:
        try:
            print("You have", rem, "chips remaining.\nHow many chips do you want to bet?\n")
            bet = int(input())
            if bet >= 1 and bet <= 10:
                return bet
            else:
                print("Invalid number of chips")
        except:
            print("Invalid input")


def game():
    good = True
    pick = -1
    while True:
        try:
            pick = int(input("PRESS 1: To play pick 1\nPRESS 2: To play pick 2\nPRESS 3: To play jumbo 7\n"))
            if pick >= 1 and pick <= 3:
                return pick
            else:
                print("Invalid range")
        except:
            print("Invalid Input")


def play(nums, bet, game):
    good = False
    while not good:
        try:
            if game == 1:
                l1 = [nums[0], nums[1], nums[2]]
                pick1 = int(input("Pick a number: "))
                good = True
                if l1.__contains__(pick1):
                    chipsReturn = bet
                else:
                    chipsReturn = bet - (bet * 2)
            elif game == 2:
                l1 = [nums[0], nums[1], nums[2]]
                pick1 = int(input("Pick your first number: "))
                pick2 = int(input("Pick your second number: "))
                good = True
                if l1.__contains__(pick1) and l1.__contains__(pick2):
                    chipsReturn = bet * 2
                else:
                    chipsReturn = bet - (bet * 2)
            else:
                therenums = []
                for i in range(7):
                    print("Enter number", i + 1)
                    therenums.append(int(input()))
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
            print("Invalid input")
            good = False
    return chipsReturn


def prompt():
    good = False
    while not good:
        try:
            print("Would you like to play again?\nPRESS 1: for yes\nPRESS 2: for no")
            again = int(input())
            if again==1 or again==2:
                good = True
            if good:
                return again
        except:
            print("Invalid input")
            good = False


main()
