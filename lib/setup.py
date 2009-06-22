# setup.py

import pygame
import os
from sys import exit

class Select_player:
	def __init__(self, screen_name):
		self.screen = screen_name
		self.player_1_img = pygame.image.load(os.path.join('graphics', 'john.jpg'))
		self.player_2_img = pygame.image.load(os.path.join('graphics', 'john.jpg'))	
		
	def run(self):
		while True:
			print "sel_player run"
			#setup.get_input()
			self.screen.blit(self.player_1_img, (0,0))
			pygame.display.update()
			pygame.time.delay(25)

class Setup:
	def __init__(self):
		self.loop = 1
		self.resolution = (600, 600)
		self.screen = pygame.display.set_mode(self.resolution, 0, 32)
		self.window_title = pygame.display.set_caption("NEW-WARE-ORDER")
		self.bg_img = pygame.image.load(os.path.join('graphics', 'intro_screen.png'))
		self.sel_player = Select_player(self.screen)
		
	def get_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
				if event.key == pygame.K_RETURN:
					self.sel_player.run()
					self.loop = 0
		
	def run(self):
		while self.loop == 1:
			self.get_input()
			self.screen.blit(self.bg_img, (0,0))
			pygame.display.update()
			pygame.time.delay(25)
		
