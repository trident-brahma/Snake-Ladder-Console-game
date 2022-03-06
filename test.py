import unittest
import random
from dice import Dice

class TestGame(unittest.TestCase):

    #negative unit test case
    def test_list_dice_value(self):
        '''
        Test that it gives random values everytime between 1 and 6
        '''
        result = Dice.diceValue()
        self.assertEqual(result, random.randint(1,6))


if __name__ == "__main__":
    unittest.main()