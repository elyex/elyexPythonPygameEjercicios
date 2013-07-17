#--------------------------------------------
#  Autor: Mauricio Eyx
#  GitHub: https://github.com/elyex
#  Twitter: @MauEyx
#  Facebook: https://www.facebook.com/MauEyx
#--------------------------------------------
#  Programa: Plantilla Basica 
#--------------------------------------------

import pygame #importar modulo Pygame
pygame.init() #Inicia las librerias de pygame
pantalla=pygame.display.set_mode((480,300)) 
salir=False
reloj1=pygame.time.Clock()
while salir!=True: #Loop principal del juego 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir=True			
		reloj1.tick(25)
		pantalla.fill((255,255,255))
		pygame.display.update()
pygame.quit()
