import pygame


def main():
	pygame.init() #inicio de módulos
	pantalla=pygame.display.set_mode([400,400])
	pygame.display.set_caption("Elyex Ejercicio1") #titulo	
	salir=False
	#Reloj
	reloj1=pygame.time.Clock()
	blanco=(255,255,255)
	rojo=(200,20,50)
	azul=(70,70,190)	
	s1=pygame.Surface([100,150])
	s1.fill(rojo)
	s2=pygame.Surface([25,50])
	s2.fill(azul)
	
	while salir!=True:#Loop Principal
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=True
				
		reloj1.tick(20)	#20 fotogramas ps	
		pantalla.fill(blanco)
		pantalla.blit(s1,[50,70])
		pantalla.blit(s2,[50,70])
				
		pygame.display.update() #Actualiza el display
	pygame.quit()
		
main()
