# setup.py

import pygame
import os
from sys import exit

class Animation:
 
    # data = [ [time, image], [time, image], ...]
 
    def __init__(self, repeat, data): 
        self.data = data
        self.cur_frame = 0
        self.ticks = pygame.time.get_ticks()
        self.ticks_remaining = data[0][0]
        self.pos = [0, 0]
        self.frames = (len(self.data) - 1)
        self.repeat = repeat
        self.pause = 0
 
    def draw(self, dest): 
        old_ticks = self.ticks
        self.ticks = pygame.time.get_ticks() 
        tick_difference = self.ticks - old_ticks 
        self.ticks_remaining -= tick_difference
 
        while (self.ticks_remaining <= 0): 
            self.cur_frame += 1
            
            if self.cur_frame > self.frames and self.repeat == 0:
                self.pause = 1
                break
            
            self.cur_frame %= len(self.data) 
            self.ticks_remaining += self.data[self.cur_frame][0]

        if self.pause == 0:
            dest.blit(self.data[self.cur_frame][1], self.pos)

class Player:
	def __init__(self, screen_name):
		self.screen = screen_name
		self.sprite_sheet_file = pygame.image.load(os.path.join('graphics', 'john.png'))
		#self.sprite_sheet = pygame.image.load(self.sprite_sheet_file).convert()
		'''
		self.walking_right_1 = self.sprite_sheet.subsurface(34, 258, 30, 60)
		self.walking_right_2 = self.sprite_sheet.subsurface(34, 258, 48, 224)
		self.walking_right = Animation(1, [[30, self.walking_right_1],[30, self.walking_right_2]])
		self.rect = self.sprite_sheet.get_rect()
		self.rect.x = 300
		self.rect.y = 300
		self.anim = self.walking_right
		#self.person = pygame.image.load(os.path.join('graphics', 'floor.png'))
		
		
	def draw(self, dest):
		self.anim.pos = self.rect
		self.anim.draw(dest)
	'''
	def update(self):
        
        #Get the current key state.
		key = pygame.key.get_pressed()
        
        #Move left/right
		if key[pygame.K_RIGHT]:
			self.rect.x += 5
		print self.sprite_sheet_file
		#self.draw(screen)
		
class Level_1:
	def __init__(self, screen_name):
		self.screen = screen_name
		self.floor = pygame.image.load(os.path.join('graphics', 'floor.png'))
		self.player_1 = Player(self.screen)
		
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
			self.player_1.update()
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
