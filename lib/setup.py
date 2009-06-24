# setup.py

import pygame
import os
import random
from sys import exit

class Animation:
 
    # data = [ [time, image], [time, image], ...]
 
    def __init__(self, data): 
        self.data = data
        self.cur_frame = 0
        self.ticks = pygame.time.get_ticks()
        self.ticks_remaining = data[0][0]
        self.pos = [0, 0]
        self.frames = (len(self.data) - 1)
 
    def draw(self, dest): 
        old_ticks = self.ticks
        self.ticks = pygame.time.get_ticks() 
        tick_difference = self.ticks - old_ticks 
        self.ticks_remaining -= tick_difference		
			
        while (self.ticks_remaining <= 0):
            self.cur_frame += 1
            self.cur_frame %= len(self.data)
            self.ticks_remaining += self.data[self.cur_frame][0]
 
        dest.blit(self.data[self.cur_frame][1], self.pos) 


class Player:
	def __init__(self, screen_name):
		self.screen = screen_name
		self.sprite_sheet = pygame.image.load(os.path.join('graphics', 'john.png')).convert()
		self.sprite_sheet.set_colorkey((255, 255, 255))
		self.walking_right_1 = self.sprite_sheet.subsurface(4, 197, 28, 60)
		self.walking_right_2 = self.sprite_sheet.subsurface(35, 197, 30, 60)
		self.walking_right_3 = self.sprite_sheet.subsurface(70, 197, 30, 60)
		self.walking_right_4 = self.sprite_sheet.subsurface(100, 197, 30, 60)
		self.walking_right_5 = self.sprite_sheet.subsurface(131, 197, 30, 60)	
		self.walking_right_6 = self.sprite_sheet.subsurface(166, 197, 30, 60)
		self.walking_left_1 = self.sprite_sheet.subsurface(164, 133, 28, 60)
		self.walking_left_2 = self.sprite_sheet.subsurface(132, 133, 30, 60)
		self.walking_left_3 = self.sprite_sheet.subsurface(98, 133, 30, 60)
		self.walking_left_4 = self.sprite_sheet.subsurface(67, 133, 30, 60)
		self.walking_left_5 = self.sprite_sheet.subsurface(36, 133, 30, 60)	
		self.walking_left_6 = self.sprite_sheet.subsurface(2, 133, 30, 60)		
		self.walking_down_1 = self.sprite_sheet.subsurface(1, 65, 29, 64)
		self.walking_down_2 = self.sprite_sheet.subsurface(30, 65, 29, 64)
		self.walking_down_3 = self.sprite_sheet.subsurface(64, 65, 29, 64)
		self.walking_down_4 = self.sprite_sheet.subsurface(97, 65, 29, 64)
		self.walking_down_5 = self.sprite_sheet.subsurface(136, 65, 29, 64)	
		self.walking_down_6 = self.sprite_sheet.subsurface(170, 65, 29, 64)
		self.walking_up_1 = self.sprite_sheet.subsurface(2, 2, 29, 63)
		self.walking_up_2 = self.sprite_sheet.subsurface(36, 2, 29, 64)
		self.walking_up_3 = self.sprite_sheet.subsurface(66, 2, 29, 64)
		self.walking_up_4 = self.sprite_sheet.subsurface(98, 2, 29, 64)
		self.walking_up_5 = self.sprite_sheet.subsurface(131, 2, 29, 64)	
		self.walking_up_6 = self.sprite_sheet.subsurface(161, 2, 29, 64)	
		self.walking_right = Animation([[150, self.walking_right_1],[150, self.walking_right_2],[150, self.walking_right_2],[150, self.walking_right_3],[150, self.walking_right_4],[150, self.walking_right_5],[150, self.walking_right_6]])
		self.walking_left = Animation([[150, self.walking_left_1],[150, self.walking_left_2],[150, self.walking_left_2],[150, self.walking_left_3],[150, self.walking_left_4],[150, self.walking_left_5],[150, self.walking_left_6]])
		self.walking_down = Animation([[150, self.walking_down_1],[150, self.walking_down_2],[150, self.walking_down_2],[150, self.walking_down_3],[150, self.walking_down_4],[150, self.walking_down_5],[150, self.walking_down_6]])
		self.walking_up = Animation([[150, self.walking_up_1],[150, self.walking_up_2],[150, self.walking_up_2],[150, self.walking_up_3],[150, self.walking_up_4],[150, self.walking_up_5],[150, self.walking_up_6]])
		self.rect = self.sprite_sheet.get_rect()
		self.rect.x = 300
		self.rect.y = 300
		self.anim = self.walking_left
		
		
	#def shoot(self):
		
	def draw(self, dest):
		
        #Get the current key state.
		key = pygame.key.get_pressed()
        
        #Move left/right
		if key[pygame.K_RIGHT]:
			self.anim = self.walking_right
			self.rect.x += 4
		elif key[pygame.K_LEFT]:
			self.anim = self.walking_left
			self.rect.x -= 4
		elif key[pygame.K_DOWN]:
			self.anim = self.walking_down
			self.rect.y += 4
		elif key[pygame.K_UP]:
			self.anim = self.walking_up
			self.rect.y -= 4
		elif key[pygame.K_SPACE]:
			pass
		
		self.anim.pos = self.rect
		self.anim.draw(dest)
	
	def update(self):
		self.draw(self.screen)
		
class Transition:
	def __init__(self, screen_name):
		self.loop = 1
		self.screen = screen_name		
		
	def run(self):
		while self.loop == 1:
			random.seed()
			x = random.randrange(0, 600)
			y = random.randrange(0, 600)
			pygame.draw.circle(self.screen, (0, 0, 0), (x,y), 100)
			pygame.display.update()
			#pygame.time.delay(6)
		
class Level_1:
	def __init__(self, screen_name):
		self.screen = screen_name
		self.floor = pygame.image.load(os.path.join('graphics', 'floor.png'))
		self.player_1 = Player(self.screen)
		self.loop = 1
		self.trans = Transition(self.screen)
		
	def get_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
				if event.key == pygame.K_RETURN:
					pass
					self.trans.run()
					self.loop = 0		
		
	def run(self):
		while self.loop == 1:
			print "running in: Level_1 class"
			self.get_input()
			self.screen.fill((255,255,255))
			self.screen.blit(self.floor, (0,0))
			self.player_1.update()
			pygame.display.update()
			pygame.time.delay(25)
				
class Story_screen:
	def __init__(self, screen_name):
		self.screen = screen_name
		self.default_font = pygame.font.get_default_font()
		self.font = pygame.font.SysFont(self.default_font, 26)
		self.text = "In an alternate time line, the year is 2010. \n you are doomed"
		self.story_text = self.font.render(self.text, True, (0,0,0))
		self.y = 600
		self.loop = 1
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
	'''
	def run(self):
		while self.loop == 1:
			self.screen.fill((255,255,255))
			y = 0
			for line in self.text.split("\n"):
				line = self.font.render(line, True, (0,0,0))
				self.screen.blit(line, (0, y+self.y))
				y -= self.font.get_height()
			pygame.display.update()
			pygame.time.delay(25)
	
	'''	
	def run(self):
		while self.loop == 1:
			self.get_input()
			self.y -= 1
			self.screen.fill((255,255,255))
			self.screen.blit(self.story_text, (0,self.y))
			pygame.display.update()
			pygame.time.delay(25)

		
class Select_player:
	def __init__(self, screen_name):
		self.loop = 1
		self.screen = screen_name
		self.player_1_img = pygame.image.load(os.path.join('graphics', 'john.png'))
		self.default_font = pygame.font.get_default_font()
		self.font = pygame.font.SysFont(self.default_font, 26)
		self.header_text = self.font.render("CHOOSE PLAYER", True, (0,0,0))
		self.story = Story_screen(self.screen)
		
	def get_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
				if event.key == pygame.K_RETURN:
					self.story.run()
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
		#self.music = pygame.mixer.music.load(os.path.join('sounds', 'music.mp3'))
		self.play = 1
		
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
			#if self.play == 1:
			#	pygame.mixer.music.play()
			#	self.play = 0
			self.get_input()
			self.screen.blit(self.bg_img, (0,0))
			pygame.display.update()
			pygame.time.delay(25)
