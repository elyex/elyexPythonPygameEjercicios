# Fuentes
import pygame
pygame.init()
pantalla=pygame.display.set_mode((480,300))
salir=False
reloj1=pygame.time.Clock()
fuente1=pygame.font.Font(None, 48)
texto1=fuente1.render("HolA @MAUEYX",0,(255,230,245))

while salir!=True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir=True
			
	reloj1.tick(15)
	pantalla.fill((30,30,200))
	pantalla.blit(texto1,(150,200))
	pygame.display.update()
pygame.quit()
	
