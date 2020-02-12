import pygame,sys
from pygame.locals import *
import time
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

        self.velocidad = 10

        self.sonidoDisparo = pygame.mixer.Sound("Sonidos/266168__plasterbrain__shooting-star-2.wav")
        self.sonidoMuerte = pygame.mixer.Sound("Sonidos/142610__autistic-lucario__wizard-eye.wav")


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
        miProyectil = Proyectil(x+160,y+280, "Imagenes/disparogenne.png", True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()


    def dibujar(self, superficie):
        superficie.blit(self.ImagenPersonajePrincipal, self.rect)

    def destruccion(self):
        self.sonidoMuerte.play()
        self.Vida = False
        self.velocidad = 0
        


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)

        self.imagenProyectil = pygame.image.load(ruta)
        self.imagenProyectil = pygame.transform.scale(self.imagenProyectil, (70,100))
        self.rect = self.imagenProyectil.get_rect()

        self.velocidad_disparo = 5

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

"""ENEMIGOS PARA CADA NIVEL """

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
        self.velocidad = 2

        self.rect.top= posy
        self.rect.left = posx
        
        self.rangoDisparo = 1 #controla la frecuencia de disparos
        self.tiempoCambio=1 # cambio de sprite

        self.conquista = False
        
        self.derecha = True
        self.contador = 0   #Controlar movimiento derecha izquierda y descenso
        self.Maxdescenso = self.rect.top + 20

        self.limiteDerecha = posx + distancia
        self.limiteIzquierda = posx - distancia

    

    def dibujar(self, superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)
        

    def comportamiento(self, tiempo):
        if self.conquista == False:
            self.__movimientos()
            
            self.__ataque()
            if self.tiempoCambio == tiempo:
                self.posImagen +=1 
                self.tiempoCambio +=1 

                if self.posImagen > len(self.listaImagenes) -1:
                    self.posImagen = 0

    def __movimientos(self):
        if self.contador <3: # numero de choques antes de descender
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
        if (randint(0,285)<self.rangoDisparo): #rango random de disparo
            self.__disparo()

    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil(x-60,y-25, "Imagenes/EspadaEmbrujadaProyectil.png", False)
        self.listaDisparo.append(miProyectil)



class Invasor2(pygame.sprite.Sprite):
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
        self.velocidad = 5

        self.rect.top= posy
        self.rect.left = posx
        
        self.rangoDisparo = 1 #controla la frecuencia de disparos
        self.tiempoCambio=1 # cambio de sprite

        self.conquista = False
        
        self.derecha = True
        self.contador = 0   #Controlar movimiento derecha izquierda y descenso
        self.Maxdescenso = self.rect.top + 35

        self.limiteDerecha = posx + distancia
        self.limiteIzquierda = posx - distancia

    

    def dibujar(self, superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)
        

    def comportamiento(self, tiempo):
        if self.conquista == False:
            self.__movimientos()
            
            self.__ataque()
            if self.tiempoCambio == tiempo:
                self.posImagen +=1 
                self.tiempoCambio +=1 

                if self.posImagen > len(self.listaImagenes) -1:
                    self.posImagen = 0

    def __movimientos(self):
        if self.contador <3: # numero de choques antes de descender
            self.__movimientoLateral()
        else:
            self.__descenso()

    def __descenso(self):
        if self.Maxdescenso == self.rect.top:
            self.contador = 0 
            self.Maxdescenso = self.rect.top + 15
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
        if (randint(0,250)<self.rangoDisparo): #rango random de disparo
            self.__disparo()

    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil(x-60,y-25, "Imagenes/EspadaEmbrujadaProyectil.png", False)
        self.listaDisparo.append(miProyectil)



class BossFinal(pygame.sprite.Sprite):
    def __init__(self, posx, posy, distancia, imagenUno, imagenDos):
        pygame.sprite.Sprite.__init__(self)

        self.imagenVampiroA = pygame.image.load(imagenUno)
        self.imagenVampiroA = pygame.transform.scale(self.imagenVampiroA, (360,280))
        #segundo sprite para animar
        #self.imagenVampiroB = pygame.image.load("Imagenes/vampiroB.png")
        self.imagenVampiroB = pygame.image.load(imagenDos)
        self.imagenVampiroB = pygame.transform.scale(self.imagenVampiroB, (360,280))
        

        self.listaImagenes = [self.imagenVampiroA, self.imagenVampiroB]
        self.posImagen = 0

        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()

        self.listaDisparo = []
        self.velocidad = 15

        self.rect.top= posy
        self.rect.left = posx
        
        self.rangoDisparo = 8 #controla la frecuencia de disparos
        self.tiempoCambio=1 # cambio de sprite

        self.conquista = False
        
        self.derecha = True
        self.contador = 0   #Controlar movimiento derecha izquierda y descenso
        self.Maxdescenso = self.rect.top + 50

        self.limiteDerecha = posx + distancia
        self.limiteIzquierda = posx - distancia

    

    def dibujar(self, superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)
        

    def comportamiento(self, tiempo):
        if self.conquista == False:
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
            self.Maxdescenso = self.rect.top + 15
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
        if (randint(0,100)<self.rangoDisparo): #rango random de disparo
            self.__disparo()

    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil(x-60,y-25, "Imagenes/EspadaEmbrujadaProyectil.png", False)
        self.listaDisparo.append(miProyectil)




def detenerTodo():
    for enemigo in lista_enemigos:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
    
    enemigo.conquista = True


""" CARGA DE ENEMIGOS POR NIVEL """

def cargarEnemigos():
    
    posx=100
    for x in range(1,5):
        enemigo = Invasor(posx,100,20, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo1 = Invasor(posx,0,30, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo2 = Invasor(posx,-100,20, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo3 = Invasor(posx,-200,20, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        
        lista_enemigos.append(enemigo)
        lista_enemigos.append(enemigo1)
        lista_enemigos.append(enemigo2)
        lista_enemigos.append(enemigo3)
        
        posx = posx + 300


def cargarEnemigos2():
    
    posx=100
    for x in range(1,5):
        enemigo = Invasor2(posx,100,30, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo1 = Invasor2(posx,0,30, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo2 = Invasor2(posx,-100,30, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo3 = Invasor(posx,-200,20, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo4 = Invasor(posx,-300,20, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        enemigo5 = Invasor(posx,-400,20, "Imagenes/vampiroA.png", "Imagenes/vampiroB.png")
        

        lista_enemigos.append(enemigo)
        lista_enemigos.append(enemigo1)
        lista_enemigos.append(enemigo2)
        lista_enemigos.append(enemigo3)
        lista_enemigos.append(enemigo4)
        lista_enemigos.append(enemigo5)

        posx = posx + 300


def cargarEnemigosFinal():
    
    posx=275
    
    enemigo = BossFinal(posx,-50,400, "Imagenes/Demon1.png", "Imagenes/Demon2.png")
        
    lista_enemigos.append(enemigo)
        




"""NIVELES DE EXPLORACION"""

def Sobrevive_y_explora():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Sobrevive y explora")
    Imagen_fondo = pygame.image.load("Imagenes/Fondo_bosque_magico.png")

    pygame.mixer.music.load("Sonidos/of-game-thrones-intro-remix.mp3")
    pygame.mixer.music.play(10) #el numero es para la cantidad de veces que se va a repetir la musica

    miFuenteSistema = pygame.font.SysFont("Arial",30)
    Texto = miFuenteSistema.render("Fin del Juego", 0,(120,100,40))
    TextoWin = miFuenteSistema.render("Superaste este nivel", 0,(120,100,40))

    jugador = personajePrincipal()
    cargarEnemigos()

    contar = True
    enJuego = True
    aux = 1
    Fuente = pygame.font.SysFont(None, 30)  # para mostrar el tiempo


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
                    time.sleep(0.09)
                    x,y = jugador.rect.center
                    jugador.disparar(x -160,y-350)
                
                
                elif evento.key == K_SPACE:
                    pygame.mixer.music.fadeout(3000)
            
            
        
        ventana.blit(Imagen_fondo,(0,0))
        
        jugador.dibujar(ventana)

        
        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujarDisparo(ventana)
                x.trayectoria()

                if x.rect.top < -10:
                    jugador.listaDisparo.remove(x)
                else:
                    for enemigo in lista_enemigos:
                        if x.rect.colliderect(enemigo.rect): 
                            lista_enemigos.remove(enemigo)
                            jugador.listaDisparo.remove(x)
                            

        if len(lista_enemigos)>0:
            for enemigo in lista_enemigos:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador):
                    jugador.destruccion()
                    enJuego = False
                    detenerTodo()

                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujarDisparo(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego = False
                            contar = False
                            detenerTodo()

                        if x.rect.top>700:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    if x in enemigo.listaDisparo:
                                        enemigo.listaDisparo.remove(x)
                                    if x not in enemigo.listaDisparo:
                                        pass
                
                
        #jajaja
        # Contador
        if contar==True:
            Tiempo = pygame.time.get_ticks()/1000
            Tiempo = int(Tiempo)
        
            if aux == 1:
                aux+=1
            else:
                aux=aux
        Score = str(Tiempo)

        
        contador = Fuente.render("Puntos:"+str(Tiempo),0,(120,70,0))
        ventana.blit(contador,(30,30))
        WinPuntaje = Fuente.render("Puntos:"+Score,0,(120,70,0))
        
        if enJuego==False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(Texto,(300,300))
            ventana.blit(WinPuntaje, (300,250))

       


        print(len(lista_enemigos))
        
        WinPuntaje = Fuente.render("Puntos:"+str(Score),0,(120,70,0))
        if len(lista_enemigos)==4:
            contar = False
            pygame.mixer.music.fadeout(3000)
            ventana.blit(TextoWin,(300,300))
            
            ventana.blit(WinPuntaje, (300,250))
            

        pygame.display.update()
        


def Sobrevive_y_explora2():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Sobrevive y explora")
    Imagen_fondo = pygame.image.load("Imagenes/terrenosombrio.jpg")

    pygame.mixer.music.load("Sonidos/of-game-thrones-intro-remix.mp3")
    pygame.mixer.music.play(10) #el numero es para la cantidad de veces que se va a repetir la musica

    miFuenteSistema = pygame.font.SysFont("Arial",30)
    Texto = miFuenteSistema.render("Fin del Juego", 0,(120,100,40))
    TextoWin = miFuenteSistema.render("Superaste este nivel", 0,(120,100,40))

    jugador = personajePrincipal()
    cargarEnemigos2()

    contar = True
    enJuego = True
    aux = 1 
    Fuente = pygame.font.SysFont(None, 30)  # para mostrar el tiempo


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
                    time.sleep(0.09)
                    x,y = jugador.rect.center
                    jugador.disparar(x -160,y-350)
                
                
                elif evento.key == K_SPACE:
                    pygame.mixer.music.fadeout(3000)
            
            
        
        ventana.blit(Imagen_fondo,(0,0))
        
        jugador.dibujar(ventana)

        
        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujarDisparo(ventana)
                x.trayectoria()

                if x.rect.top < -10:
                    jugador.listaDisparo.remove(x)
                else:
                    for enemigo in lista_enemigos:
                        if x.rect.colliderect(enemigo.rect): 
                            lista_enemigos.remove(enemigo)
                            jugador.listaDisparo.remove(x)
                            

        if len(lista_enemigos)>0:
            for enemigo in lista_enemigos:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador):
                    jugador.destruccion()
                    enJuego = False
                    detenerTodo()

                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujarDisparo(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego = False
                            contar = False
                            detenerTodo()


                        if x.rect.top>700:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    if x in enemigo.listaDisparo:
                                        enemigo.listaDisparo.remove(x)
                                    if x not in enemigo.listaDisparo:
                                        pass
                
        # Contador
        if contar==True:
            Tiempo = pygame.time.get_ticks()/1000
            Tiempo = int(Tiempo)
        
            if aux == 1:
                aux+=1
            else:
                aux=aux
        Score = str(Tiempo)

        
        contador = Fuente.render("Puntos:"+str(Tiempo),0,(120,70,0))
        ventana.blit(contador,(30,30))
        WinPuntaje = Fuente.render("Puntos:"+Score,0,(120,70,0))
        
        if enJuego==False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(Texto,(300,300))
            ventana.blit(WinPuntaje, (300,250))

       


        #print(len(lista_enemigos))
        print(str(aux))
        WinPuntaje = Fuente.render("Puntos:"+str(Score),0,(120,70,0))
        if len(lista_enemigos)==6:
            contar = False
            pygame.mixer.music.fadeout(3000)
            ventana.blit(TextoWin,(300,300))
            
            ventana.blit(WinPuntaje, (300,250))
            

        pygame.display.update()



def Sobrevive_y_exploraFinal():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Sobrevive y explora")
    Imagen_fondo = pygame.image.load("Imagenes/camino-al-infierno.jpg")
    
    Imagen_fondo = pygame.transform.scale(Imagen_fondo, (1000,600))


    pygame.mixer.music.load("Sonidos/of-game-thrones-intro-remix.mp3")
    pygame.mixer.music.play(10) #el numero es para la cantidad de veces que se va a repetir la musica

    miFuenteSistema = pygame.font.SysFont("Arial",30)
    Texto = miFuenteSistema.render("Fin del Juego", 0,(120,100,40))
    TextoWin = miFuenteSistema.render("Superaste este nivel", 0,(120,100,40))

    jugador = personajePrincipal()
    cargarEnemigosFinal()

    contar = True
    enJuego = True
    aux = 1 
    Fuente = pygame.font.SysFont(None, 30)  # para mostrar el tiempo
    Score = 0


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
                    time.sleep(0.09)
                    x,y = jugador.rect.center
                    jugador.disparar(x -160,y-350)
                
                
                elif evento.key == K_SPACE:
                    pygame.mixer.music.fadeout(3000)
            
            
        
        ventana.blit(Imagen_fondo,(0,0))
        
        jugador.dibujar(ventana)

        
        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujarDisparo(ventana)
                x.trayectoria()

                if x.rect.top < -10:
                    jugador.listaDisparo.remove(x)
                else:
                    for enemigo in lista_enemigos:
                        if x.rect.colliderect(enemigo.rect): 
                            
                            jugador.listaDisparo.remove(x)
                            Score = Score + 1
                            if Score >= 200:
                                lista_enemigos.remove(enemigo)

                            

        if len(lista_enemigos)>0:
            for enemigo in lista_enemigos:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador):
                    jugador.destruccion()
                    enJuego = False
                    detenerTodo()

                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujarDisparo(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego = False
                            contar = False
                            detenerTodo()


                        if x.rect.top>700:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    if x in enemigo.listaDisparo:
                                        enemigo.listaDisparo.remove(x)
                                    if x not in enemigo.listaDisparo:
                                        pass
                
        # Contador
        """
        if contar==True:
            Tiempo = pygame.time.get_ticks()/1000
            Tiempo = int(Tiempo)
        
            if aux == 1:
                aux+=1
            else:
                aux=aux
        
        """
        
        contador = Fuente.render("Puntos:"+str(Score),0,(120,70,0))
        ventana.blit(contador,(30,30))
        WinPuntaje = Fuente.render("Puntos:"+str(Score),0,(120,70,0))
        
        if enJuego==False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(Texto,(300,300))
            ventana.blit(WinPuntaje, (300,250))

       


        print(len(lista_enemigos))
        #print(str(aux))
        WinPuntaje = Fuente.render("Puntos:"+str(Score),0,(120,70,0))
        if len(lista_enemigos)==0:
            contar = False
            pygame.mixer.music.fadeout(3000)
            ventana.blit(TextoWin,(300,300))
            
            ventana.blit(WinPuntaje, (300,250))
            

        pygame.display.update()


#Sobrevive_y_explora()

#Sobrevive_y_explora2()

Sobrevive_y_exploraFinal()