# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random


def name_to_number(name):
    # function converts strings into numbers
    if name=="rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "no such name available"



def number_to_name(number):
    # function converts numbers into corresponding strings
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "no such number available"


def rpsls(player_choice):
    # functions prints what is player's choice and prints computer's choice and defines who wins
    choice= name_to_number(player_choice)
    print ""
    print "Players chooses %s"  % number_to_name(choice)

    comp_choice= random.randrange(0,5)
    print "Computer chooses %s" % number_to_name(comp_choice)

    if (choice - comp_choice)%5 == 1 or (choice - comp_choice)%5 == 2:
        print "Player wins!"
    elif (choice - comp_choice)%5 == 3 or (choice - comp_choice)%5 == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


