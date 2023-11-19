import unittest
import pygame

from game import display_score, enemy_movement, collision, player_animation

class TestGame(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_display_score(self):
        # You may need to mock or simulate pygame.time.get_ticks() for testing
        # For simplicity, let's assume start_time is set correctly in the game
        start_time = 0
        pygame.time.get_ticks = lambda: start_time * 1000

        score = display_score()
        self.assertEqual(score, 0)  # Assuming the game just started

    def test_enemy_movement(self):
        # Test enemy movement with a sample list of enemy rectangles
        enemy_list = [pygame.Rect(600, 500, 35, 35), pygame.Rect(700, 500, 35, 35)]
        updated_enemy_list = enemy_movement(enemy_list)
        self.assertTrue(all(enemy.x < 600 for enemy in updated_enemy_list))

    def test_collision(self):
        # Test collision function with a player and an enemy rectangle
        player_rect = pygame.Rect(80, 525, 50, 50)
        enemy_rect = pygame.Rect(100, 500, 35, 35)
        self.assertTrue(collision(player_rect, [enemy_rect]))

    def test_player_animation(self):
        # Test player animation function
        global player_index, player_Naruto, player_walk
        player_rect = pygame.Rect(80, 525, 50, 50)
        player_index = 0
        player_Naruto = player_walk[player_index]
        player_animation()
        self.assertNotEqual(player_Naruto, player_walk[player_index])

if __name__ == '__main__':
    unittest.main()
