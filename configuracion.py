import pygame
import random
import os
# tipografia
CONSOLA = pygame.font.match_font("04B_30")
# tamaño ventana
ANCHO = 1000
ALTO = 600
# colores
NEGRO = (0, 0, 0)
BLANCO=(255,255,255)
#rutas
carpeta_juego=os.path.dirname(__file__)
carpeta_imagen=os.path.join(carpeta_juego,"imagen")
carpeta_explo=os.path.join(carpeta_juego,"explocion")
carpeta_ezquierda=os.path.join(carpeta_juego,"izquierda")
carpeta_fondo=os.path.join(carpeta_juego,"recursos")
carpeta_musica=os.path.join(carpeta_juego,"sonidos")

fondo = pygame.image.load(os.path.join(carpeta_fondo,"fondo_extendido1.png"))
fondo = pygame.transform.scale(fondo, (2000, ALTO))

tierra_fondo = pygame.image.load(os.path.join(carpeta_fondo,"Imagen1 - copia.png"))
tierra_fondo = pygame.transform.scale(tierra_fondo, (8000, 1000))

bala_grupo=pygame.sprite.Group()
bala_grupo2=pygame.sprite.Group()
animacion_explp=pygame.sprite.Group()

i = random.randrange(20, 26)
iconoimagen = pygame.image.load(os.path.join(carpeta_fondo,f"Imagen{i}.png"))
# tiempo
# fotogramas
fotogramas = 160
reloj = pygame.time.Clock()
#musica
pygame.mixer.init()
musica_fondo=pygame.mixer.Sound(os.path.join(carpeta_musica,"musicafondo.wav"))
musica_fondo.set_volume(0.1)
sonido_disparo=pygame.mixer.Sound(os.path.join(carpeta_musica,"laser.wav"))
sonido_disparo.set_volume(0.1)
# mostrar texto em pantalla
def muestra_texto(pantalla, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(CONSOLA, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)
