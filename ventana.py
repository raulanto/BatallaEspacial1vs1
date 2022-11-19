import pygame
import personaje
import sys
import random
import configuracion
from nave import Nave

b = 0

pygame.init()
ventana = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
pygame.display.set_icon(configuracion.iconoimagen)
pygame.display.set_caption("Battle Space")




def ventana_inicio():
    t = True
    a = 0
    f = 0
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                t = False
                break
        x1_relativa = a % configuracion.fondo.get_rect().width
        ventana.blit(configuracion.fondo, (x1_relativa - configuracion.fondo.get_rect().width, b))
        if x1_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.fondo, (x1_relativa, 0))
        a -= 1
        x_relativa = f % configuracion.tierra_fondo.get_rect().width
        ventana.blit(configuracion.tierra_fondo, (x_relativa - configuracion.tierra_fondo.get_rect().width, -270))
        if x_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.tierra_fondo, (x_relativa, -270))
        f -= 10
        mostrar()
        pygame.display.update()
def textoPerdido(ganador):
    t = True
    a = 0
    b=0
    f = 0
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                t = False
                break
        x1_relativa = a % configuracion.fondo.get_rect().width
        ventana.blit(configuracion.fondo, (x1_relativa - configuracion.fondo.get_rect().width, b))
        if x1_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.fondo, (x1_relativa, 0))
        a -= 1
        x_relativa = f % configuracion.tierra_fondo.get_rect().width
        ventana.blit(configuracion.tierra_fondo, (x_relativa - configuracion.tierra_fondo.get_rect().width, -270))
        if x_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.tierra_fondo, (x_relativa, -270))
        f -= 10

        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        configuracion.muestra_texto(ventana,  "-GANADOR "+ganador+" ", configuracion.BLANCO, 65,
                                    configuracion.ANCHO / 2, configuracion.ALTO / 2)
        configuracion.muestra_texto(ventana,  "<PRESIONA ESPACIO>", color, 25,
                                    configuracion.ANCHO / 2, configuracion.ALTO - 250)
        pygame.display.update()

def mostrar():
    a = random.randrange(0, 255)
    b = random.randrange(0, 255)
    c = random.randrange(0, 255)
    color = (a, b, c)
    configuracion.muestra_texto(ventana, "___________________________", BLANCO, 35, configuracion.ANCHO / 2, 150)
    configuracion.muestra_texto(ventana, "-BATTLE 1vs1-", configuracion.BLANCO, 65, configuracion.ANCHO / 2, 200)
    configuracion.muestra_texto(ventana, "___________________________", BLANCO, 35, configuracion.ANCHO / 2, 230)
    configuracion.muestra_texto(ventana,  "<PRESIONA ESPACIO>", color, 25,configuracion.ANCHO / 2,configuracion.ALTO-330)
def cerrar():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
def juego():
    a = 0
    ganador = ""
    f = 0
    grupo = pygame.sprite.Group()
    cluto = personaje.Cluto()
    grupo.add(cluto)
    grupo_nave = pygame.sprite.Group()
    nave = Nave()
    grupo_nave.add(nave)
    j=True
    while j:
        cerrar()
        x1_relativa = a % configuracion.fondo.get_rect().width
        ventana.blit(configuracion.fondo, (x1_relativa - configuracion.fondo.get_rect().width, b))
        if x1_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.fondo, (x1_relativa, 0))
        a -= 1
        x_relativa = f % configuracion.tierra_fondo.get_rect().width
        ventana.blit(configuracion.tierra_fondo, (x_relativa - configuracion.tierra_fondo.get_rect().width, -270))
        if x_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.tierra_fondo, (x_relativa, -270))
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            f -= 10
        if teclas[pygame.K_LEFT]:
            f += 10
        grupo.update()
        grupo.draw(ventana)
        grupo_nave.update()
        # grupos de coliciones
        colision = pygame.sprite.groupcollide(grupo, configuracion.bala_grupo, True, True,pygame.sprite.collide_circle)
        colision2 = pygame.sprite.groupcollide(grupo_nave, configuracion.bala_grupo2, True, True, pygame.sprite.collide_circle)
        if colision:
            ganador = "NAVE"
            j = False
        if colision2:
            ganador = "CLUTU"
            j = False

        grupo_nave.draw(ventana)
        configuracion.bala_grupo.update()
        configuracion.bala_grupo2.update()
        configuracion.animacion_explp.update()
        configuracion.animacion_explp.draw(ventana)
        configuracion.bala_grupo.draw(ventana)
        configuracion.bala_grupo2.draw(ventana)
        pygame.display.update()
    configuracion.bala_grupo.empty()
    configuracion.animacion_explp.empty()
    grupo.empty()
    grupo_nave.empty()
    textoPerdido(ganador)


BLANCO = (255, 255, 255)
configuracion.musica_fondo.play(-1)
while True:
    configuracion.reloj.tick(160)
    ventana_inicio()
    juego()
    pygame.display.update()
