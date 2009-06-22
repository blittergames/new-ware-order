# setup.py

import pygame
import os
from sys import exit

class Level_1:
	def __init__(self, screen_name):
		self.screen = screen_name
		self.floor = pygame.image.load(os.path.join('graphics', 'floor.png'))
		
	def get_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
				if event.key == pygame.K_RETURN:
					pass
					#self.sel_player.run()
					#self.loop = 0		
		
	def run(self):
		while True:
			print "running in: Level_1 class"
			self.get_input()
			self.screen.fill((255,255,255))
			self.screen.blit(self.floor, (0,0))
			pygame.display.update()
			pygame.time.delay(25)

class Select_player:
	def __init__(self, screen_name):
		self.loop = 1
		self.screen = screen_name
		self.player_1_img = pygame.image.load(os.path.join('graphics', 'john.jpg'))
		self.player_2_img = pygame.image.load(os.path.join('graphics', 'john.jpg'))
		self.default_font = pygame.font.get_default_font()
		self.font = pygame.font.SysFont(self.default_font, 26)
		self.header_text = self.font.render("CHOOSE PLAYER", True, (0,0,0))
		self.lev_1 = Level_1(self.screen)
		
	def get_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
				if event.key == pygame.K_RETURN:
					self.lev_1.run()
					self.loop = 0
		
	def run(self):
		while self.loop == 1:
			print "running in: Select_player class"
			#setup.get_input()
			self.get_input()
			self.screen.fill((255,255,255))
			self.screen.blit(self.player_1_img, (0,0))
			self.screen.blit(self.header_text, (5,5))
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
			print "running in: Setup class"
			self.get_input()
			self.screen.blit(self.bg_img, (0,0))
			pygame.display.update()
			pygame.time.delay(25)
