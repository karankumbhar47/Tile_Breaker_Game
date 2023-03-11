import pygame
import pickle
from os import path


pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
tile_size = 106
cols = 8
margin = 10
num_repeat = 8
screen_width = 836#tile_size * cols
screen_height = 800#(tile_size * cols) -48

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')


#load images
tile1_img = pygame.image.load('images/07-Breakout-Tiles.png')
tile1_img = pygame.transform.scale(tile1_img, (tile_size, 28))
tile2_img = pygame.image.load('images/17-Breakout-Tiles.png')
tile2_img = pygame.transform.scale(tile2_img, (tile_size, 28))
tile3_img = pygame.image.load('images/19-Breakout-Tiles.png')
tile3_img = pygame.transform.scale(tile3_img, (tile_size, 28))

save_img = pygame.image.load('images/save_btn.png')
load_img = pygame.image.load('images/load_btn.png')


#define game variables
clicked = False
level = 4

#define colours
white = (255, 255, 255)
green = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

#create empty tile list
world_data = []
for row in range(screen_height//28):
	r = [0] * num_repeat
	world_data.append(r)


#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_grid():
	for c in range(num_repeat):
		#vertical lines
		pygame.draw.line(screen, white, (c * tile_size, 0), (c * tile_size, screen_height))
	for d in range(screen_height//28):
		#horizontal lines
		pygame.draw.line(screen, white, (0, d * screen_height//28), (screen_width, d * screen_height//28))


def draw_world():
	for row in range(screen_height//28):
		for col in range(num_repeat):
			if world_data[row][col] > 0:
				if world_data[row][col] == 1:
					#tile1
					img = pygame.transform.scale(tile1_img, (tile_size,28))
					screen.blit(img, (col * tile_size, row * screen_height//28))
				if world_data[row][col] == 2:
					#tile2
					img = pygame.transform.scale(tile2_img, (tile_size, 28))
					screen.blit(img, (col * tile_size, row * screen_height//28))
				if world_data[row][col] == 3:
					#tile3
					img = pygame.transform.scale(tile3_img, (tile_size,28))
					screen.blit(img, (col * tile_size, row * screen_height//28))


class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action

#create load and save buttons
save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

#main game loop
run = True
while run:

	clock.tick(fps)

	#draw background
	screen.fill(green)
	# screen.blit(bg_img, (0, 0))
	# screen.blit(sun_img, (tile_size * 2, tile_size * 2))

	#load and save level
	if save_button.draw():
		#save level data
		pickle_out = open(f'level{level}_data', 'wb')
		pickle.dump(world_data, pickle_out)
		pickle_out.close()
	if load_button.draw():
		#load in level data
		if path.exists(f'level{level}_data'):
			pickle_in = open(f'level{level}_data', 'rb')
			world_data = pickle.load(pickle_in)


	#show the grid and draw the level tiles
	draw_grid()
	draw_world()


	#text showing current level
	draw_text(f'Level: {level}', font, white, tile_size, screen_height - 60)
	draw_text('Press UP or DOWN to change level', font, white, tile_size, screen_height - 40)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		#mouseclicks to change tiles
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = pos[0] // tile_size
			y = pos[1] // 28
			#check that the coordinates are within the tile area
			if x < 20 and y < 20:
				#update tile value
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 3:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 3
		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		#up and down key presses to change level number
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level += 1
			elif event.key == pygame.K_DOWN and level > 1:
				level -= 1

	#update game display window
	pygame.display.update()

pygame.quit()