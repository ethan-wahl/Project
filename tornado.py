import pygame, simpleGE
import random


# Constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (135, 206, 250)  # Light blue
TORNADO_COLOR = (139, 69, 19)        # Brown
PLAYER_COLOR = (255, 0, 0)            # Red
OBSTACLE_COLOR = (0, 0, 0)            # Black
PLAYER_SPEED = 5
OBSTACLE_SPEED = 3
OBSTACLE_SIZE = 20
OBSTACLE_GAP = 200
OBSTACLE_FREQUENCY = 100

# Tornado class
class Tornado(simpleGE):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.image.fill(TORNADO_COLOR)

    def update(self):
        self.rotate(5)  # Rotate the tornado

# Player class
class Player(simpleGE):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.image.fill(PLAYER_COLOR)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.move(PLAYER_SPEED, 0)
        if keys[pygame.K_UP]:
            self.move(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            self.move(0, PLAYER_SPEED)

# Obstacle class
class Obstacle(simpleGE):
    def __init__(self, x, y):
        super().__init__(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE)
        self.image.fill(OBSTACLE_COLOR)

    def update(self):
        self.move(0, OBSTACLE_SPEED)

# Main game class
class TornadoGame(simpleGE):
    def __init__(self):
        super().__init__("Tornado Game", WIDTH, HEIGHT, BACKGROUND_COLOR)
        self.tornado = Tornado(WIDTH // 2, HEIGHT // 2)
        self.player = Player(WIDTH // 2, HEIGHT - 100)
        self.obstacles = []
        self.score = 0
        self.score_text = simpleGE("Score: 0", 20, 20, font_size=24)

    def update(self):
        self.tornado.update()
        self.player.update()
        self.spawn_obstacles()
        self.move_obstacles()
        self.check_collisions()
        self.update_score()

    def render(self, screen):
        self.tornado.draw(screen)
        self.player.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        self.score_text.draw(screen)

    def spawn_obstacles(self):
        if random.randint(1, OBSTACLE_FREQUENCY) == 1:
            x = random.randint(0, WIDTH - OBSTACLE_SIZE)
            y = -OBSTACLE_SIZE
            self.obstacles.append(Obstacle(x, y))

    def move_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()

    def check_collisions(self):
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                print("Game Over!")
                self.quit()

    def update_score(self):
        self.score += 1
        self.score_text.text = f"Score: {self.score}"

# Main function
def main():
    game = TornadoGame()
    game.run()

if __name__ == "__main__":
    main()
