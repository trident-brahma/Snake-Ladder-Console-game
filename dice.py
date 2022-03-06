import time
import random

class Dice():
    #The FACE value has the total number of faces of the dice and 
    #he SLEEP value has the wait time of 1 second
    SLEEP = 1
    FACE = 6
    def __init__(self) -> None:
        self.diceVal = None
        
    def diceValue(self):
        time.sleep(self.SLEEP)
        self.diceVal = random.randint(1, self.FACE)

        print("It's a " + str(self.diceVal))
        return self.diceVal