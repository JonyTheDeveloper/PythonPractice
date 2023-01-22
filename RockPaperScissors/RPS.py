# Rock Paper Scissors
from random import randrange
import pyfiglet

# Choose best off/how many games you want to play
# Start Game
# Choose option
# Display result

rps_options = ["Rock", "Paper", "Scissors"]
games = []


# 0 = Rock
# 1 = Paper
# 2 = Scissors
# 0 > 2
# 1 > 0
# 2 > 1

def play():
    print("\n\n")
    option = input("Select your option:\n> ")
    while option not in ["Rock", "Paper", "Scissors", "rock", "paper", "scissors", "r", "p", "s"]:
        print("Please write your option correctly")
        option = input("Select your option:\n> ")
    rps(option)


def to_int(option):
    if option in ["Rock", "rock", "r"]:
        return 0
    elif option in ["Paper", "paper", "p"]:
        return 1
    elif option in ["Scissors", "scissors", "s"]:
        return 2


def to_str(option):
    if option == 0:
        return "Rock"
    elif option == 1:
        return "Paper"
    elif option == 2:
        return "Scissors"


def rps(p1_option):
    p1_option = to_int(p1_option)
    p2_option = randrange(3)
    print(to_str(p1_option))
    print(to_str(p2_option))

    if p1_option == 0:
        if p2_option == 0:
            # Draw
            print("Draw!\n You chose", to_str(p1_option), " and they also chose", to_str(p2_option))
            games.append("/")
        elif p2_option == 1:
            # Loss
            print("Oof! A Loss!\n Your ", to_str(p1_option), " looses to their ", to_str(p2_option))
            games.append("x")
        elif p2_option == 2:
            # Win
            print("A win!\n Your ", to_str(p1_option), " beats their ", to_str(p2_option))
            games.append("y")
    elif p1_option == 1:
        if p2_option == 0:
            # Win
            print("A win!\n Your ", to_str(p1_option), " beats their ", to_str(p2_option))
            games.append("y")
        elif p2_option == 1:
            # Draw
            print("Draw!\n You chose", to_str(p1_option), " and they also chose", to_str(p2_option))
            games.append("/")
        elif p2_option == 2:
            # Loss
            print("Oof! A Loss!\n Your ", to_str(p1_option), " looses to their ", to_str(p2_option))
            games.append("x")
    elif p1_option == 2:
        if p2_option == 0:
            # Loss
            print("Oof! A Loss!\n Your ", to_str(p1_option), " looses to their ", to_str(p2_option))
            games.append("x")
        elif p2_option == 1:
            # Win
            print("A win!\n Your ", to_str(p1_option), " beats their ", to_str(p2_option))
            games.append("y")
        elif p2_option == 2:
            # Draw
            print("Draw!\n You chose", to_str(p1_option), " and they also chose", to_str(p2_option))
            games.append("/")


# Intro
ascii_banner = pyfiglet.figlet_format("Rock Paper Scissors")
print(ascii_banner)

# Select rounds
print("How many rounds do you wish to play?")
print("a) Best of 3")
print("b) Best of 5")
print("c) Custom")
menu_option = input("> ")
while menu_option not in ["a", "b", "c", "A", "B", "C"]:
    print("Please select an option available")
    menu_option = input("> ")

if menu_option == "a" or menu_option == "A":
    rounds = 3
elif menu_option == "b" or menu_option == "B":
    rounds = 5
elif menu_option == "c" or menu_option == "C":
    print("How many rounds do you wish to play?")
    rounds = input("> ")
else:
    rounds = 0

# Select your options
rounds_played = 0
wins = 0
losses = 0
rounds = int(rounds)
while rounds_played < rounds:
    play()
    if games[-1] == "y":
        wins = wins + 1
        if wins > (rounds / 2):
            rounds_played = rounds
            print("You win")
    elif games[-1] == "x":
        losses = losses + 1
        rounds_played = rounds_played + 1
        if losses > (rounds / 2):
            rounds_played = rounds
            print("You lose")

    # print(games)
    # print("Total rounds: ", rounds)
    # print("Rounds played: ", rounds_played)
    # print("Wins: ", wins)
    # print("Losses: ", losses)
