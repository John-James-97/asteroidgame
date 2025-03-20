import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
	
	def update(self, dt):
		self.position += self.velocity * dt
	
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			angle = random.uniform(20, 50)
			pos_velocity = self.velocity.rotate(angle)
			neg_velocity = self.velocity.rotate(angle * -1)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid1.velocity = pos_velocity * 1.2
			asteroid2.velocity = neg_velocity * 1.2
