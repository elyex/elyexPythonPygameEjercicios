#--------------------------------------------
#  Autor: Mauricio Eyx
#  GitHub: https://github.com/elyex
#  Twitter: @MauEyx
#  Facebook: https://www.facebook.com/MauEyx
#--------------------------------------------
#  Programa: Imagenes Movimiento con el teclado iz y dr
#--------------------------------------------

import pygame #importar modulo Pygame
pygame.init() #Inicia las librerias de pygame
pantalla=pygame.display.set_mode((480,300)) 
salir=False
reloj1=pygame.time.Clock()
imagen1=pygame.image.load("monster.png")
(x,y) = (100,100)
vx=0
r1=pygame.Rect(250,80,10,400)
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
	x+=vx
	reloj1.tick(15)
	pantalla.fill((255,255,255))
	pantalla.blit(imagen1,(x,y))
	pygame.draw.rect(pantalla,(0,0,0),r1)
	pygame.display.update()
pygame.quit()
