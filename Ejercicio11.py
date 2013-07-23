# Primer juego Cuadrados al azar con fuente, timer, sonido y contador de puntos
import pygame
import random
pygame.init()
sonido1=pygame.mixer.Sound("EfectoDisparos.mp3")
pantalla=pygame.display.set_mode((500,500))
fuente1=pygame.font.SysFont("Arial",15,True,False)
info=fuente1.render("Haga click sobre los rectangulos, tienes 10 segundos",0,(255,255,255))
salir=False
reloj1=pygame.time.Clock()
listarec=[]
segundosint=0
termino=False
r1=pygame.Rect(0,0,25,25)
rotos=0
for x in range(25):
		w = random.randrange(20,30)
		h = random.randrange(20,30)
		x = random.randrange(450)
		y = random.randrange(450)
		listarec.append(pygame.Rect(x,y,w,h))
while salir!=True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir=True
		if event.type == pygame.MOUSEBUTTONDOWN:
			#recorre los rectangulos
			for recs in listarec:
				#deja en 0,0 el rectangulo
				if termino==False:
					if r1.colliderect(recs):
						sonido1.play()
						recs.width=0
						recs.height=0
						rotos+=1
				 
	reloj1.tick(20)
	(r1.left,r1.top)=pygame.mouse.get_pos()
	#poner cursor del mouse en el medio
	r1.left-=r1.width/2
	r1.top-=r1.height/2
	
	pantalla.fill((0,0,0))
	for recs in listarec:
		pygame.draw.rect(pantalla,(0,200,0),recs)
	pygame.draw.rect(pantalla,(0,0,200),r1)
	pantalla.blit(info,(5,5))
	
	
	#contador de segundos
	if segundosint >= 10 :
		termino=True
	if termino == False:
		segundosint=pygame.time.get_ticks()/1000
		segundos=str(segundosint)
		contador=fuente1.render(segundos,0,(0,0,230))
	else:
		contador=fuente1.render(" Usted rompio: "+str(rotos),0,(100,0,230))
	pantalla.blit(contador,(5,40))
	pygame.display.update()
pygame.quit()
	
