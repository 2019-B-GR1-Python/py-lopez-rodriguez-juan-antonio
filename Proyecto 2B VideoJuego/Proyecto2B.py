import pygame, sys
from pygame.locals import *
from random import randint 

pygame.init()
ventana = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Mi Proyecto") 

Mi_imagen = pygame.image.load("Imagenes/darkGenne2.png")
Mi_imagen = pygame.transform.scale(Mi_imagen, (120,140))
Imagen_fondo = pygame.image.load("Imagenes/Fondo_bosque_magico.png")

posX = 200
posY = 400

velocidad = 1
#Color_fondo = (255,255,255)
derecha = True   # para movimineto automatico

rectangulo = pygame.Rect(0,0,100,50)
rectangulo_dos = pygame.Rect(300,300,100,50)

while True:
    ventana.blit(Imagen_fondo, (0,0))
    #ventana.fill(Color_fondo)
    ventana.blit(Mi_imagen,(posX,posY))

    pygame.draw.rect(ventana,(180,70,70), rectangulo_dos)
    pygame.draw.rect(ventana,(180,70,70),rectangulo)
    #mover rectangulo
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()

    # colision
    if rectangulo.colliderect(rectangulo_dos):
        velocidad = 0
        print('Colision')



    for event in pygame.event.get():
    # cerrar pantalla
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Movimiento automatico
    if derecha == True:
        if posX<900:
            posX+=velocidad
            rectangulo_dos.left = posX
        else:
            derecha=False
    else:
        if posX>1:
            posX-=velocidad
            rectangulo_dos.left = posX
        else:
            derecha=True

    """

    # Movimiento teclado
        elif event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                posX-=velocidad
            elif event.key==K_RIGHT:
                posX += velocidad
        elif event.type == pygame.KEYUP:
            if event.key==K_LEFT:
                print("Izq libre")
            elif event.key==K_RIGHT:
                print("derecha libre")
    """
    """
    #Movimiento con mouse
    posX,posY = pygame.mouse.get_pos()
    posX = posX - 50
    posY = posY - 50
    """

    pygame.display.update()


