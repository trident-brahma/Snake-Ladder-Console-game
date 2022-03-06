import time
import sys
import snake
import ladder
from dice import Dice

diceObj = Dice()
snakeObj = snake.Snake()
ladderObj = ladder.Ladder()
class Board:

    snakes = snakeObj.snakesValues()
    ladders = ladderObj.ladderValues()

    #The SLEEP value has the wait time of 1 second, 
    #and the MAXV value has the total number of boxes on the board.
    SLEEP = 1
    MAXV = 100

    #This will initiate the game.
    def __init__(self) -> None:
        self.playerNames()

    #It will take the input of names for players.
    def playerNames(self):
        self.players=2
        while True:
            try:
                print("How many players will be playing in the game?")
                self.players = int(input())
                if self.players < 2:
                    print("Must be greater than 1")
                else:
                    break
            except ValueError:
                print("Must be a number")

        self.names = {}
        for i in range(1,self.players+1):
            while True:
                time.sleep(self.SLEEP)
                self.name = input("What is the name of Player {}? ".format(i))
                if (not self.name in self.names) and (len(self.name) > 0):
                    self.names[self.name] = 0
                    break
                else:
                    print('Cannot have duplicate or zero length names')
        print("\nGet Ready Players\n")
        self.start(self.names)

    #The snakeLadder function checks whether the player has landed on a ladder step or a snake mouth.
    #If it is none of the above, then the normal movement is occured.
    def snakeLadder(self, playerName, curVal, diceVal):
        time.sleep(self.SLEEP)
        self.oldVal = curVal
        curVal = curVal + diceVal

        if curVal > self.MAXV:
            print("You need " + str(self.MAXV - self.oldVal) + " to win this game.")
            return self.oldVal

        print("\n" + playerName + " moved from " + str(self.oldVal) + " to " + str(curVal))
        if curVal in self.snakes:
            self.finVal = self.snakes.get(curVal)
            snakeObj.snakeBite(curVal, self.finVal, playerName)

        elif curVal in self.ladders:
            self.finVal = self.ladders.get(curVal)
            ladderObj.ladderJump(curVal, self.finVal, playerName)

        else:
            self.finVal = curVal

        return self.finVal

    #It will check whether the player has reached the 100th block successfully or not.
    def isWin(self, playerName, position):
        time.sleep(self.SLEEP)
        if self.MAXV == position:
            print("\n" + playerName + " won the game.")
            print("Congratulations " + playerName)
            sys.exit(1)

    #The driver code of the program.
    def start(self, players):
        print("{}, Welcome To Snakes And Ladders".format(", ".join(players)))
        input("Press Enter")
        self.diceVal = 0
        while True:

            # Foreach player
            for player, currPos in players.items():

                # Move player
                time.sleep(self.SLEEP)
                input_1 = input("\n" + player + ": " + " Press enter to roll dice: ")
                print("\nRolling dice...")
                diceVal = diceObj.diceValue()
                time.sleep(self.SLEEP)
                print(player + " is moving...")
                players[player] = self.snakeLadder(player, currPos, diceVal)

                # Check win
                self.isWin(player, currPos)
Board()