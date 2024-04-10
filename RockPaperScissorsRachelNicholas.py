## Nicholas Shy, Rachel Cheung
# 7/25/2022
# Project 5/6
# A rock paper Scissors game


# global variables
player1 = ""
player2 = ""


## translate the input into full name
# @param inp: the decision of the user
# @return the translated string
def translate(inp):
    if inp == "R":
        return "Rock"
    elif inp == "P":
        return "Paper"
    elif inp == "S":
        return "Scissors"
    else:
        # default case
        return inp


## Validates the user input and return boolean value
# @param string: the input from user
# @return True if valid, False if invalid
def userInput(string):
    string = string.upper()
    if string != 'R' and string != "P" and string != "S":
        return False
    return True


## Printing the result
# @param valid: True only if both inputs are valid
# @return none
def gamePrint(valid):
    global player1, player2
    if valid:
        print(translate(player1), "v.", translate(player2))
        print(solving())


## Solving decides the winner and return the result
# @param none
# @return result of game
def solving():
    global player1, player2
    result = ""
    if player1 == 'S':
        if player2 == 'S':
            result = "It's a TIE"
        elif player2 == 'R':
            result = "Player 2 wins"
        else:
            result = "Player 1 wins"
    elif player1 == 'R':
        if player2 == 'R':
            result = "It's a tie"
        elif player2 == 'S':
            result = "Player 1 wins"
        else:
            result = "Player 2 wins"
    elif player1 == 'P':
        if player2 == 'P':
            result = "It's a tie"
        elif player2 == 'S':
            result = "Player 2 wins"
        else:
            result = "Player 1 wins"
    return result


## The main function that starts the game and
# @param none
# @return none
def main():
    print("Let's play Rock, Paper, Scissors.")
    cont = "y"
    while cont.lower() == "y":
        global player1, player2
        player1 = input("Player 1: ")
        valid = userInput(player1)
        if valid:
            player1 = player1.upper()
            player2 = input("Player 2: ")
            valid = userInput(player2)
            if not valid:
                print(translate(player1), "v. [ERROR:",
                      player2, "not a valid move.]")
            else:
                player2 = player2.upper()
        else:
            print("[ERROR:", player1, "not a valid move.]")
        gamePrint(valid)
        cont = input("\n\nagain? \n")
    print("Nice game!")


## calling the main
if __name__ == '__main__':
    main()
