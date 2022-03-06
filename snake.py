from collections import defaultdict


class Snake():
    def __init__(self) -> None:
        self._snakes = {8: 4,
                    18: 1,
                    26: 10,
                    39: 5,
                    51: 6,
                    54: 36,
                    56: 1,
                    60: 23,
                    75: 28,
                    83: 45,
                    85: 59,
                    90: 48,
                    92: 25,
                    97: 87,
                    99: 63}
    def snakesValues(self):
        return self._snakes 
        
    #The snakeBite function print the situation of the player after this incident.
    def snakeBite(self, oldVal, curVal, playerName):
        print("\n" + " ~~~~~~~~>")
        print("\n" + playerName + " got a snake bite. Down from " + str(oldVal) + " to " + str(curVal))