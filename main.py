import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collition(bullet):
                    print("shot")
                    bullet.kill()
                    asteroid.split()
            if asteroid.collition(player):
                print("Game over!")
                exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
