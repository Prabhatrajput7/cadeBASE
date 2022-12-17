import unittest
import gamesup
class Game(unittest.TestCase):
    def test_checking(self):
        guess = 5
        answer = 5
        result = gamesup.games(guess,answer)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
