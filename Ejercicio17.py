#--------------------------------------------
#  Autor: Mauricio Eyx
#  GitHub: https://github.com/elyex
#  Twitter: @MauEyx
#  Facebook: https://www.facebook.com/MauEyx
#--------------------------------------------
#  Programa: Uso de Claces en Pygame con fondos
#--------------------------------------------
import pygame
class Player(pygame.sprite.Sprite):
	def __init__(self,imagen):
		self.imagen=imagen
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=(100,200)
	def mover(self,vx,vy):  
		self.rect.move_ip(vx,vy)
	def update(self,superficie):
		superficie.blit(self.imagen,self.rect)
		
def main():
	import pygame #importar modulo Pygame
	pygame.init() #Inicia las librerias de pygame
	pantalla=pygame.display.set_mode((480,300)) 
	salir=False
	reloj1=pygame.time.Clock()
	imagen1=pygame.image.load("monster.png").convert_alpha()
	imagenfondo=pygame.image.load("monster.png").convert_alpha()
	#player1=Player(imagen1)
	
	#variables auxiliares
	player1=Player(imagen1)
	vx, vy = 0,0
	velocidad=10
	lftS, rgtS, topS, dwnS = False, False, False, False
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
					lftS = False
					if rgtS: vx=velocidad
					else: vx=0
				if event.key == pygame.K_RIGHT:
					rghS = False
					if lftS: vx=-velocidad
					else: vx=0
				if event.key == pygame.K_UP:
					topS = False
					if dwnS: vy=velocidad
					else: vy=0
				if event.key == pygame.K_DOWN:
					dwnS = False
					if topS: vy=-velocidad
					else: vy=0							
		
		reloj1.tick(20)
		player1.mover(vx, vy)
		pantalla.blit(imagenfondo,(0,0))
		player1.update(pantalla)		
		pygame.display.update()
	pygame.quit()
main()
