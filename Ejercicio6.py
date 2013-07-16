# Rectangulos al azar
import pygame
import random
pygame.init()
pantalla=pygame.display.set_mode((500,500))
salir=False
reloj1=pygame.time.Clock()
listarec=[]
for x in range(15):
		w = random.randrange(15,45)
		h = random.randrange(20,60)
		x = random.randrange(450)
		y = random.randrange(450)
		listarec.append(pygame.Rect(x,y,w,h))
		
while salir!=True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir=True
	reloj1.tick(20)
	pantalla.fill((0,0,0))
	for recs in listarec:
		pygame.draw.rect(pantalla,(0,200,0),recs)
	pygame.display.update()
pygame.quit()
	
