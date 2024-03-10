#  File: Game number 3
#  Purpose: Subtract a square game -> a positive integer is written down and two players take turns subtracting squared integer values (1,4,9,..etc) until one player leaves zero,in which case he (or she) is the winner.
#  Author: Rana Tarek Ahmed Fouad Ibrahim
#  ID: 20230632



#Game starts with display a welcome massage ,instructions how game is played and a menu the user choose to start the game or exit the game

while True :
    print("***Welcome to Subtract-A-Square game***\n \nThis game a positive integer is written down\nand two players take turns subtracting squared\ninteger values (1,4,9,..etc) until one player leaves \nzero,in which case he (or she) is the winner.\n \n-> Choose and enter A or B : \nA) Start a round \nB) Exit the game")
    # The user must input either A or B only
    choiceone = input()

#If the user enter anything neither A nor B (uppercase or lowercase) an error massage will display to the user and let the user to try again

    while choiceone != "A" and choiceone != "B" and choiceone != "a" and choiceone != "b":
        print("Please Select a valid choice ")
        choiceone = input()

#If the user choose A (uppercase or lowercase) the user must to input the number to start with this round and it must be a non-square and non-negative number

    if choiceone == "A" or choiceone == "a" :
        numcoins = input("-> Enter the number of coins to start with :\n")
#Checking the user input a number
        x = numcoins.isnumeric()
        while x == False:
            print("Please enter a valid choice")
            numcoins = input()
            x = numcoins.isnumeric()
        numcoins = int(numcoins)
#Checking the user input a non-square number (not zero also)
        sqrtnum = int(numcoins ** 0.5)
        while numcoins == 1 or numcoins == 0 or sqrtnum**2 == numcoins :
             print("Please enter a valid choice")
             numcoins = input("Enter the number of coins to start with :\n")
             x = numcoins.isnumeric()
             while x == False:
                print("Please enter a valid choice")
                numcoins = input()
                x = numcoins.isnumeric()
             numcoins = int(numcoins)
             sqrtnum = int(numcoins ** 0.5)

#If the user choose B (uppercase or lowercase) ,the program ( Subtract a square game) exit and end working

    elif choiceone == "B" or choiceone == "b":
        break
#After the user input the number to start with a menu will display to choose to play with computer or 2 Players play

    print("-> Choose and enter A or B :\nA) 2 Players play\nB) Play with the computer")
    choicetwo = input()

#If the user enter anything neither A nor B (uppercase or lowercase) an error massage will display to the user and let the user to try again

    while choicetwo != "A" and choicetwo != "B" and choicetwo != "a" and choicetwo != "b":
        print("Please Select a valid choice ")
        choicetwo = input()

#If the user enter A (uppercase or lowercase) , The game round begins in 2 players mode

    if choicetwo == "A" or choicetwo == "a":
        print("** Starting the game with number of coins : ", numcoins ,"**")

#Game is PLAYING

        while numcoins >= 1:

#The round will not end unless the number of coins equals 0 and who takes the last coin wins

            turnaction = input("-> Player 1 turn Please Enter a non-zero square number and less than or equal to the number of coins:\n")

#Checking the user input is a number
            x = turnaction.isnumeric()
            while x == False :
                print ("Please enter a valid choice")
                turnaction = input()
                x = turnaction.isnumeric()
            turnaction = int(turnaction)

#Check if the player 1 input is greater than 1 and not a zero number (if less than an error massage appear and let user to try again)

            while turnaction < 1 :
                print ("Please select a valid choice")
                turnaction = input("-> Player 1 turn Please Enter a non-zero square number and less than or equal to the number of coins:\n")
                # Checking the user input is a number
                x = turnaction.isnumeric()
                while x == False:
                    print("Please enter a valid choice")
                    turnaction = input()
                    x = turnaction.isnumeric()
                turnaction = int(turnaction)

#Checking the number the user enter if it is square or not by take the intger number of square root the number and if the square of the integer number equals to the input number then the input is a square number

            sqrtnum = int (turnaction**0.5)

#Check if the user input is less than or equal the number of coins

            while sqrtnum**2 != turnaction or turnaction > numcoins :
                print ("Please enter a valid choice")
                turnaction = input("-> Player 1 turn Please Enter a non-zero square number and less than or equal to the number of coins:\n")
                # Checking the user input is a number
                x = turnaction.isnumeric()
                while x == False:
                    print("Please enter a valid choice")
                    turnaction = input()
                    x = turnaction.isnumeric()
                turnaction = int(turnaction)
                sqrtnum = int(turnaction ** 0.5)

#If the number is a square number then the game will subtract the square number from the number of coins

            numcoins -= turnaction

#Display the new number of coins

            print ("Current coins: " , numcoins)

#Check the new number of coins if it is zero or not if it is zero so player 1 wins and the first menu will appear again

            if numcoins == 0 :
                print("****Player 1 is the winner!****\n")
                break

#If player 1 doesn't win ,player 2 will turn

            turnaction = input("-> Player 2 turn Please Enter a non-zero square number and less than or equal to the number of coins:\n")

# Checking the user input is a number
            x = turnaction.isnumeric()
            while x == False:
                    print("Please enter a valid choice")
                    turnaction = input()
                    x = turnaction.isnumeric()
            turnaction = int(turnaction)

# Check if the player 2 input is greater than to 1 and not a zero number (if less than an error massage appear and let user to try again)

            while turnaction < 1:
                    print("Please select a valid choice")
                    turnaction = input("-> Player 2 turn Please Enter a non-zero square number and less than or equal to the number of coins:\n")
                    # Checking the user input is a number
                    x = turnaction.isnumeric()
                    while x == False:
                        print("Please enter a valid choice")
                        turnaction = input()
                        x = turnaction.isnumeric()
                    turnaction = int(turnaction)

# Checking the number the user enter if it is square or not by take the intger number of square root the number and if the square of the integer number equals to the input number then the input is a square number

            sqrtnum = int(turnaction ** 0.5)

# Check if the user input is less than or equal the number of coins

            while sqrtnum ** 2 != turnaction or turnaction > numcoins:
                    print("Please enter a valid choice")
                    turnaction = input( "-> Player 2 turn Please Enter a non-zero square number and less than or equal to the number of coins:\n")
                    # Checking the user input is a number
                    x = turnaction.isnumeric()
                    while x == False:
                        print("Please enter a valid choice")
                        turnaction = input()
                        x = turnaction.isnumeric()
                    turnaction = int(turnaction)
                    sqrtnum = int(turnaction ** 0.5)

# If the number is a square number then the game will subtract the square number from the number of coins

            numcoins -= turnaction

# Display the new number of coins

            print("Current coins: ", numcoins)

# Check the new number of coins if it is zero or not if it is zero so player 2 wins and the 1st menu will appear again

            if numcoins == 0:
                    print("****Player 2 is the winner!****\n")
                    break

######################################################################################################################################################################

#If the user enter B (uppercase or lowercase) , The game round begins in play with computer mode

    elif choicetwo == "B" or "b":

        def validmoves(n):

#Returns a list of valid moves for a given number of coins
            return [i ** 2 for i in range(1, int(n ** 0.5) + 1) if i ** 2 <= n]

        def chckterminal(n):

#Checking if the game is in a terminal state no more moves possible (number of coins = 0)

            return len(validmoves(n)) == 0


        def playgame(n):

#Plays the game with a strategy where the computer always chooses the largest square less than or equal to the current number of coins

            while not chckterminal(n):
                print("Current coins:", n)
                move = input("-> Enter your move:\n ")
                x = move.isnumeric()
                while x == False:
                    print("Invalid move Try again")
                    move = input()
                    x = move.isnumeric()
                move = int(move)

                if move not in validmoves(n):
                    print("Invalid move Try again ")
                    continue
                n -= move
                if chckterminal(n):
                    print("****Player wins!**** \n")
                    break
                else:
                    print("Remaining coins:", n)
                    print("Computer's turn...")
                    comp_move = max(validmoves(n))
                    print("Computer removes", comp_move, "coins.")
                    n -= comp_move
                    if chckterminal(n):
                        print("****Computer wins!**** \n")
                        break
# Game is PlAYING

        print("Starting game with", numcoins, "coins.")
        playgame(numcoins)
