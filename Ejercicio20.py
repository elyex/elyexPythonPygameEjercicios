#--------------------------------------------
#  Autor: Mauricio Eyx
#  GitHub: https://github.com/elyex
#  Twitter: @MauEyx
#  Facebook: https://www.facebook.com/MauEyx
#  Web: http://mauricio.elyex.com
#--------------------------------------------
#  Programa: Uso de Claces en Pygame con Self
#--------------------------------------------
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		self.imagen1=pygame.image.load("nave.png").convert_alpha()
		self.imagen2=pygame.image.load("and.png").convert_alpha()
		self.imagenes=[self.imagen1,self.imagen2]
		self.imagen_actual=0
		self.imagen=self.imagenes[self.imagen_actual]		
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=(100,200)
		self.estamoviendo=False
	def mover(self,vx,vy):
		self.rect.move_ip(vx,vy)
	def update(self,superficie,vx,vy,t):
		if (vx,vy)==(0,0):self.estamoviendo=False
		else:estamoviendo=True
		if t==1:
			self.imagen_actual+=1
		if self.imagen_actual>(len(self.imagenes)-1):
			self.imagen_actual=0
			
		self.mover(vx,vy)
		self.imagen=self.imagenes[self.imagen_actual]
		if self.estamoviendo==False:
			self.imagen=self.imagenes[0]
		
		superficie.blit(self.imagen,self.rect)
	
def main():
	import pygame #importar modulo Pygame
	
	pygame.init() #Inicia las librerias de pygame
	pantalla=pygame.display.set_mode((480,300)) 
	salir=False
	reloj1=pygame.time.Clock()
	player1=Player()
	#variables auxiliares
	vx, vy = 0,0
	velocidad=10
	lftS, rgtS, topS, dwnS = False, False, False, False
	t=0
	while salir!=True: #Loop principal del juego 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lftS=True
					vx=-velocidad
				if event.key == pygame.K_RIGHT:
					rgtS=True
					vx=velocidad
				if event.key == pygame.K_UP:
					topS=True
					vy=-velocidad
				if event.key == pygame.K_DOWN:
						dwnS=True
						vy=velocidad
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					lftS=False
					if rgtS:vx=velocidad
					else: vx=0
				if event.key == pygame.K_RIGHT:
					rghS = False
					if lftS: vx=-velocidad
					else: vx=0
				if event.key == pygame.K_UP:
					topS = False
					if dwnS: vy=velocidad
					else: vy=-0
				if event.key == pygame.K_DOWN:
					dwnS = False
					if topS: vy=-velocidad
					else: vy=0							
	
		reloj1.tick(30)
		t+=1
		if t>1:
			t=0
			 
		pantalla.fill((200,200,200))
		player1.update(pantalla,vx,vy,t)		
		pygame.display.update()

		
	pygame.quit()
	
main()
