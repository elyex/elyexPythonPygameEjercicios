#--------------------------------------------
#  Autor: Mauricio Eyx
#  GitHub: https://github.com/elyex
#  Twitter: @MauEyx
#  Facebook: https://www.facebook.com/MauEyx
#--------------------------------------------
#  Programa: Imagenes Movimiento con SPRITE bloqueo con el cuadrado rojo
#--------------------------------------------

import pygame #importar modulo Pygame
pygame.init() #Inicia las librerias de pygame
pantalla=pygame.display.set_mode((480,300)) 
salir=False
reloj1=pygame.time.Clock()
imagen1=pygame.image.load("monster.png").convert_alpha()
vx=0
r1=pygame.Rect(450,80,10,450)
sprite1=pygame.sprite.Sprite()
sprite1.image=imagen1
sprite1.rect=imagen1.get_rect()
sprite1.rect.top=115
sprite1.rect.left=30

while salir!=True: #Loop principal del juego 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir=True			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				vx-=10
			if event.key == pygame.K_RIGHT:
				vx+=10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				vx=0
			if event.key == pygame.K_RIGHT:
				vx=0
	oldx=sprite1.rect.left
	sprite1.rect.move_ip(vx,0)
	if sprite1.rect.colliderect(r1):
		sprite1.rect.left=oldx
	
	reloj1.tick(15)
	pantalla.fill((255,255,255))
	pygame.draw.rect(pantalla,(220,0,0),r1)
	pantalla.blit(sprite1.image,sprite1.rect)
	pygame.display.update()
pygame.quit()
