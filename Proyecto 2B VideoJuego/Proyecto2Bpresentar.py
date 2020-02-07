import pygame,sys
from pygame.locals import *

from random import randint
#variables globales
ancho = 1000
alto = 600
lista_enemigos = []

class personajePrincipal(pygame.sprite.Sprite):
    """Clase para el jugador principal"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPersonajePrincipal = pygame.image.load("Imagenes/darkGenne2.png")
        self.ImagenPersonajePrincipal = pygame.transform.scale(self.ImagenPersonajePrincipal, (120,140))
        self.rect = self.ImagenPersonajePrincipal.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-100

        self.listaDisparo = []
        self.Vida = True

        self.velocidad = 15

        #print(self.rect)

    def movimientoDerecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()

    def movimientoIzquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento()

    def __movimiento(self):
        if self.Vida == True:
            if self.rect.left <=0:
                self.rect.left = 0
            elif self.rect.right>950:
                self.rect.right = 930

    def disparar(self,x,y):
        miProyectil = Proyectil(x,y, "Imagenes/disparogenne.png", True)
        self.listaDisparo.append(miProyectil)

    def dispararSuperPoder(self,x,y):
        miProyectil = Proyectil(x,y, "Imagenes/darkGenneRRRulti.png", True)
        self.listaDisparo.append(miProyectil)

    def dibujar(self, superficie):
        superficie.blit(self.ImagenPersonajePrincipal, self.rect)


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)

        self.imagenProyectil = pygame.image.load(ruta)
        self.imagenProyectil = pygame.transform.scale(self.imagenProyectil, (400,560))
        self.rect = self.imagenProyectil.get_rect()

        self.velocidad_disparo = 10

        self.rect.top= posy
        self.rect.left = posx

        self.disparoPersonaje = personaje


    def trayectoria(self):
        if self.disparoPersonaje ==True:
            self.rect.top = self.rect.top - self.velocidad_disparo
        else:
            self.rect.top = self.rect.top + self.velocidad_disparo

    def dibujarDisparo(self, superficie):
        superficie.blit(self.imagenProyectil, self.rect)


class Invasor(pygame.sprite.Sprite):
    def __init__(self, posx, posy, distancia, imagenUno, imagenDos):
        pygame.sprite.Sprite.__init__(self)

        self.imagenVampiroA = pygame.image.load(imagenUno)
        self.imagenVampiroA = pygame.transform.scale(self.imagenVampiroA, (180,140))
        #segundo sprite para animar
        #self.imagenVampiroB = pygame.image.load("Imagenes/vampiroB.png")
        self.imagenVampiroB = pygame.image.load(imagenDos)
        self.imagenVampiroB = pygame.transform.scale(self.imagenVampiroB, (180,140))
        

        self.listaImagenes = [self.imagenVampiroA, self.imagenVampiroB]
        self.posImagen = 0

        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()

        self.listaDisparo = []
        self.velocidad = 3

        self.rect.top= posy
        self.rect.left = posx
        
        self.rangoDisparo = 2 #controla la frecuencia de disparos
        self.tiempoCambio=1 # cambio de sprite
        
        self.derecha = True
        self.contador = 0   #Controlar movimiento derecha izquierda y descenso
        self.Maxdescenso = self.rect.top + 20

        self.limiteDerecha = posx + distancia
        self.limiteIzquierda = posx - distancia

    

    def dibujar(self, superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)
        

    def comportamiento(self, tiempo):
        self.__movimientos()
        
        self.__ataque()
        if self.tiempoCambio == tiempo:
            self.posImagen +=1 
            self.tiempoCambio +=1 

            if self.posImagen > len(self.listaImagenes) -1:
                self.posImagen = 0

    def __movimientos(self):
        if self.contador <2: # numero de choques antes de descender
            self.__movimientoLateral()
        else:
            self.__descenso()

    def __descenso(self):
        if self.Maxdescenso == self.rect.top:
            self.contador = 0 
            self.Maxdescenso = self.rect.top + 30
        else:
            self.rect.top += 1

    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left>self.limiteDerecha:
                self.derecha=False
                self.contador+=1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left < self.limiteIzquierda:
                self.derecha = True
            


    
    def __ataque(self):
        if (randint(0,100)<self.rangoDisparo):
            self.__disparo()

    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil(x-205,y-235, "Imagenes/EspadaEmbrujadaProyectil.png", False)
        self.listaDisparo.append(miProyectil)


def cargarEnemigos():
    enemigo = Invasor(100,0,100, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
    lista_enemigos.append(enemigo)
    enemigo = Invasor(250,0,100, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
    lista_enemigos.append(enemigo)
    enemigo = Invasor(400,0,100, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
    lista_enemigos.append(enemigo)
    enemigo = Invasor(550,0,100, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
    lista_enemigos.append(enemigo)
    enemigo = Invasor(700,0,100, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
    lista_enemigos.append(enemigo)


def Sobrevive_y_explora():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Sobrevive y explora")
    Imagen_fondo = pygame.image.load("Imagenes/Fondo_bosque_magico.png")

    jugador = personajePrincipal()
    cargarEnemigos()

    enJuego = True

    reloj = pygame.time.Clock()

    while True:

        # establecer frames por segundo
        reloj.tick(60)

        tiempo = pygame.time.get_ticks()/1000
        tiempo = int(tiempo)
        #jugador.movimiento()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            
        if enJuego == True:
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT: #Movimiento
                    jugador.movimientoIzquierda()
                
                elif evento.key == K_RIGHT:
                    jugador.movimientoDerecha()

                elif evento.key== K_q:
                    x,y = jugador.rect.center
                    jugador.disparar(x -160,y-350)
                
                elif evento.key== K_r:
                    x,y = jugador.rect.center
                    jugador.dispararSuperPoder(x -160,y-350)
            
            
        
        ventana.blit(Imagen_fondo,(0,0))
        
        jugador.dibujar(ventana)

        
        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujarDisparo(ventana)
                x.trayectoria()

                if x.rect.top < -300:
                    jugador.listaDisparo.remove(x)

        if len(lista_enemigos)>0:
            for enemigo in lista_enemigos:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujarDisparo(ventana)
                        x.trayectoria()

                        if x.rect.top>300:
                            enemigo.listaDisparo.remove(x)
                    

        pygame.display.update()


Sobrevive_y_explora()