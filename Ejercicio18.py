#--------------------------------------------
#  Autor: Mauricio Eyx
#  GitHub: https://github.com/elyex
#  Twitter: @MauEyx
#  Facebook: https://www.facebook.com/MauEyx
#--------------------------------------------
#  Programa: Uso de Claces en Pygame con fondos y rectangulos aleatorios
#--------------------------------------------
import pygame
import random
class Recs(object):
	def __init__(self,numeroinicial):
		self.lista=[]
		for x in range(numeroinicial):
			#creo un random
			leftrandom=random.randrange(2,560)
			toprandom=random.randrange(-580,-10)
			width=random.randrange(10,30)
			height=random.randrange(15,30)
			self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))
	#redibuja el random de cuadrados
	def reagresar(self):
		for x in range(len(self.lista)):
			if self.lista[x].top>482:
				leftrandom=random.randrange(2,560)
				toprandom=random.randrange(-580,-10)
				width=random.randrange(10,30)
				height=random.randrange(15,30)
				self.lista[x]=(pygame.Rect(leftrandom,toprandom,width,height))
	def agregarotro(self):
		pass
	def mover(self):
		for rectangulo in self.lista:
			rectangulo.move_ip(0,2)
	def pintar(self,superficie):
		for rectangulo in self.lista:
			pygame.draw.rect(superficie,(200,0,0), rectangulo)
			
class Player(pygame.sprite.Sprite):
	def __init__(self,imagen):
		self.imagen=imagen
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=(100,200)
	def mover(self,vx,vy):  
		self.rect.move_ip(vx,vy)
	def update(self,superficie):
		superficie.blit(self.imagen,self.rect)
	def colision(player, recs):
		pass
def main():
	#import pygame #importar modulo Pygame
	pygame.init() #Inicia las librerias de pygame
	pantalla=pygame.display.set_mode((480,300)) 
	salir=False
	reloj1=pygame.time.Clock()
	imagen1=pygame.image.load("nave.png").convert_alpha()
	imagenfondo=pygame.image.load("fondo.png").convert_alpha()
	
	recs1=Recs(25)
	player1=Player(imagen1)
	
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
					else: vy=-0
				if event.key == pygame.K_DOWN:
					dwnS = False
					if topS: vy=-velocidad
					else: vy=0							
		
		reloj1.tick(20)
		player1.mover(vx,vy)
		recs1.mover()
		pantalla.blit(imagenfondo,(0,0))
		recs1.pintar(pantalla)
		player1.update(pantalla)		
		pygame.display.update()
		recs1.reagresar()
	pygame.quit()
main()
