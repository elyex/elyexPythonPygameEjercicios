import pygame
def main():
	pygame.init() #inicio de modulos
	pantalla=pygame.display.set_mode([400,400])
	pygame.display.set_caption("Elyex Ejercicio2") #titulo	
	salir=False
	#Reloj
	reloj1=pygame.time.Clock()
	#colores
	blanco=(255,255,255)
	rojo=(200,20,50)
	azul=(70,70,190)	
	
	r1=pygame.Rect(50,50,45,45)
	r2=pygame.Rect(150,150,75,95)
	
	while salir!=True:#Loop Principal
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=True
		reloj1.tick(20)	#20 fotogramas ps	
		pantalla.fill(blanco)
		pygame.draw.rect(pantalla,rojo,r2)
		pygame.draw.rect(pantalla,azul,r1)
		pygame.display.update() #Actualiza el display
	pygame.quit()
		
main()
