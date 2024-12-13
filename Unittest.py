import unittest
from My_SNAKE_GAME import SnakeGame

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        # Create an instance of the game
        self.game = SnakeGame()

    def test_initial_score(self):
        # Check initial score
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.high_score, 0)

    def test_movement_up(self):
        # Test moving up
        self.game.go_up()
        self.assertEqual(self.game.head.direction, "up")

    def test_food_collision(self):
        # Simulate food collision
        self.game.food.goto(0, 20)
        self.game.head.goto(0, 20)
        self.game.check_food_collision()
        self.assertEqual(self.game.score, 5)  # Score should increase by 5


if __name__ == "__main__":
    unittest.main()

