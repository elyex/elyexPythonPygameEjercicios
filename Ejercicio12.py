#Autor: Mauricio Eyx
#Web: http://mauricio.elyex.com
#--------------------------------------------
#  Autor: Mauricio Eyx
#  GitHub: https://github.com/elyex
#  Twitter: @MauEyx
#  Facebook: https://www.facebook.com/MauEyx
#--------------------------------------------
#  Programa: Imagenes Movimiento con el mouse 
#--------------------------------------------

import pygame #importar modulo Pygame
pygame.init() #Inicia las librerias de pygame
pantalla=pygame.display.set_mode((480,300)) 
salir=False
reloj1=pygame.time.Clock()
imagen1=pygame.image.load("monster.png")
(x,y) = (100,100)
while salir!=True: #Loop principal del juego 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir=True
			
		reloj1.tick(25)
		(x,y)=pygame.mouse.get_pos()
		pantalla.fill((255,255,255))
		pantalla.blit(imagen1,(x,y))
		pygame.display.update()
pygame.quit()
