import pygame
import random
import os
import configuracion

NEGRO=(0,0,0)
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load(os.path.join(configuracion.carpeta_imagen,"nave.tif")).convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.image.set_colorkey(configuracion.NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # darle forma de circulo
        self.radius = 30
        # velocidad de la bala
        self.cadencia = 1750
        # Centra el rectángulo (sprite)
        self.rect.centerx = 0
        self.rect.centery = 40
        # velocidad del personaje inicial
        self.velocidad_x = 0
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self):
        # velocidad predeterminada cada vuelta  del blcle si no pulsas nada
        self.velocidad_x = 0
        # mantiene las presionar pulsadas
        presionar = pygame.key.get_pressed()
        if presionar[pygame.K_d]:
            self.velocidad_x = 10

        if presionar[pygame.K_a]:
            self.velocidad_x = -10
        self.i=random.randrange(1,10)
        if self.i==1:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                self.disparo()
                self.ultimo_disparo = ahora
        # actuliza la posicion del personaje
        self.rect.x += self.velocidad_x
        if self.rect.left < 0:
            self.rect.left = 0
        # Limita el margen derecho
        if self.rect.right > configuracion.ANCHO:
            self.rect.right = configuracion.ANCHO

    def disparo(self):
        bala = Disparo(self.rect.centerx, self.rect.top)
        configuracion.bala_grupo.add(bala)
        configuracion.sonido_disparo.play()



class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(configuracion.carpeta_explo,"disparo2.tif")).convert(), (10, 20))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def kill(self):
        super(Disparo, self).kill()
        explo = Explosion(self.rect.centerx, self.rect.centery)
        configuracion.animacion_explp.add(explo)

    def update(self):
        self.rect.y += 25
        if self.rect.bottom >500:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(4, 10):
            img = pygame.image.load(os.path.join(configuracion.carpeta_explo,f"Imagen{num}.tif"))
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 4
        # update explosion animation
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        # if the animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()
