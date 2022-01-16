import random

continueGame = True
again = ""
def printRules():
    print("The computer will think of either rock, paper or scissors.")
    print("You will enter r for rock, p for paper or s for scissors.")
    print("The computer will reveal it's choice and the winner.\n")

def chooseRPS():
    choice = ""
    while choice not in ["r", "p", "s"]:
        choice = input("Enter r for rock, p for paper or s for scissors: ").lower()
    return choice
def playGame():
    
    computerChoice = random.choice(["r", "p", "s"])
    choice = chooseRPS()

    # Tell the user that computer's choice
    if computerChoice == "r":
        print("The computer chose: Rock")
    elif computerChoice == "p":
        print("The computer chose: Paper")
    elif computerChoice == "s":
        print("The computer chose: Scissors")
    
    # Check who won
    if choice == "r" and computerChoice == "r":
        print("No one wins")
    if choice == "r" and computerChoice == "p":
        print("Computer wins")
    if choice == "r" and computerChoice == "s":
        print("Player wins")
    
    if choice == "p" and computerChoice == "r":
        print("Player wins")
    if choice == "p" and computerChoice == "p":
        print("No one wins")
    if choice == "p" and computerChoice == "s":
        print("Computer wins")
    
    if choice == "s" and computerChoice == "r":
        print("Computer wins")
    if choice == "s" and computerChoice == "p":
        print("Player wins")
    if choice == "s" and computerChoice == "s":
        print("No one wins")

print("Welcome to the Rock, Paper, Scissors Game")
print("======")
printRules()
while continueGame == True:
    playGame()

    again = input("Play again? (y/n) ").lower()

    if again == "y":
        continueGame = True
    elif again == "n":
        continueGame = False




