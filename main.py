import pygame
from constants import *
from player import Player
from asteroid import Asteroid
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
	Shot.containers = (shots, updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidField = AsteroidField()
	
	dt = 0
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collisionCheck(player):
				print("Game over!")
				exit()
			for shot in shots:
				if shot.collisionCheck(asteroid):
					shot.kill()
					asteroid.split()
				
		
		screen.fill("black")
		
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
