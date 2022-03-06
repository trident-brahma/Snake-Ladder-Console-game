class Ladder():
    def __init__(self) -> None:
        self._ladders = {3: 20,
                    6: 14,
                    11: 28,
                    15: 34,
                    17: 74,
                    22: 37,
                    38: 59,
                    49: 67,
                    57: 76,
                    61: 78,
                    73: 86,
                    81: 98,
                    88: 91}
    def ladderValues(self):
        return self._ladders

    #The ladderJump function print the situation of the player after this incident.
    def ladderJump(self, oldVal, curVal, playerName):
        print("\n" + " ########")
        print("\n" + playerName + " climbed the ladder from " + str(oldVal) + " to " + str(curVal))
