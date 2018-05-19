import pygame
import random
import time

(W, H) = (800, 600)
(HW, HH) = (W / 2, H / 2)

pygame.init()

class player(object):
	def __init__(self, x, y, width, height):
		self.sprite = pygame.sprite.Sprite()
		self.rect = pygame.Rect(x, y, width, height)
		self.image = pygame.Surface((width, height))
		self.speed = 4

class car(object):
	def __init__(self, x, y, width, height):
		self.sprite = pygame.sprite.Sprite()
		self.rect = pygame.Rect(x, y, width, height)
		self.image =pygame.Surface((width, height))
		self.speed = 4

class apple(object):
	def __init__(self, x, y, width, height):
		self.sprite = pygame.sprite.Sprite()
		self.rect = pygame.Rect(x, y, width, height)
		self.image = pygame.Surface((width, height))
		
canvas = pygame.display.set_mode((W, H))
pygame.display.set_caption('Okay')
clock = pygame.time.Clock()

appleCount = 0

ranX = random.randint(0, 755)
ranY = random.randint(0, 555)
apple = apple(ranX, ranY, 16, 16)
apple.image.fill((255, 0, 0))

snake = player(HW, HH, 16, 16)
snake.image.fill((255, 255, 255))

car1 = car(10, 50, 32, 24)
car1.image.fill((255, 255, 255))

car2 = car(780, 250, 32, 24)
car2.image.fill((255, 255, 255))

car3 = car(10, 450, 32, 24)
car3.image.fill((255, 255, 255))

def draw():
	canvas.fill((0, 0, 0))
	canvas.blit(car1.image, car1.rect.topleft)
	canvas.blit(car2.image, car2.rect.topleft)
	canvas.blit(car3.image, car3.rect.topleft)
	canvas.blit(snake.image, snake.rect.topleft)
	canvas.blit(apple.image, apple.rect.topleft)


def isCollision(ob1):
	global appleCount
	ranX = random.randint(5, 755)
	ranY = random.randint(0, 555)
	if pygame.sprite.collide_rect(ob1, car1) or pygame.sprite.collide_rect(ob1, car2) or pygame.sprite.collide_rect(ob1, car3):
		gameOver()

	if pygame.sprite.collide_rect(ob1, apple):
		musicPlay('Blip_Select.wav', 1)
		apple.rect.x = ranX
		apple.rect.y = ranY
		appleCount += 1
		snake.speed += 0.05
		car1.speed += 0.05
		car2.speed += 0.05
		car3.speed += 0.05

def restart():
	appleCount
	snake.rect.x = HW
	snake.rect.y = HH
	car1.rect.x = 0
	car2.rect.x = 800
	car3.rect.x = 0
	car1.speed = car2.speed = car3.speed = 4

def musicPlay(name, time):
	pygame.mixer.music.load(name)
	pygame.mixer.music.play(time)

def gameOver():
	font = pygame.font.SysFont(None, 125)
	text = font.render('GAME OVER', True, (255, 0, 0))
	canvas.blit(text, (150,300))
	musicPlay('Explosion.wav', 1)

	pygame.display.update()
	

	time.sleep(2.0)
	
	restart()

	loop()

def score(count):
	global appleCount
	font = pygame.font.SysFont(None, 25)
	text = font.render('Score = ' + str(count), True, (0, 255, 0))
	canvas.blit(text, (0,0))

def carMoves():
	car1.rect.x += car1.speed
	car2.rect.x -= car2.speed
	car3.rect.x += car3.speed
	if car1.rect.x > W + car1.rect.width or car3.rect.x > W + car3.rect.width:
		car1.rect.x = 0 - car1.rect.width
		car3.rect.x = 0 - car3.rect.width
	elif car2.rect.x < 0 - car2.rect.width:
		car2.rect.x = 800 + car2.rect.width

def controls():
	

	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT] and snake.rect.x > 0:
		snake.rect.x -= snake.speed
	elif key[pygame.K_RIGHT] and snake.rect.x < W - snake.rect.width - snake.speed:
		snake.rect.x += snake.speed
	elif key[pygame.K_DOWN] and snake.rect.y < H - snake.rect.height - snake.speed:
		snake.rect.y += snake.speed
	elif key[pygame.K_UP] and snake.rect.y > 0:
		snake.rect.y -= snake.speed
	elif key[pygame.K_ESCAPE]:
		restart()

def loop():
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw()
		controls()
		carMoves()
		isCollision(snake)
		score(appleCount)
		pygame.display.update()
		clock.tick(60)

loop()
pygame.quit()
quit()