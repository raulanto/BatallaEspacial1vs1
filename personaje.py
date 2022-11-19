import os
import random

import pygame
import configuracion

NIVEL_SUELO = 500

tamano_imagen = (84, 84)


class Cluto(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.df = random.randrange(1, 7)
        self.image = pygame.image.load(os.path.join(configuracion.carpeta_imagen, f"Imagen{self.df}.tif")).convert()
        self.image = pygame.transform.scale(self.image, tamano_imagen)
        self.image.set_colorkey(configuracion.NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = 300, 600
        # velocidad del personaje inicial
        self.velocidad_x = 0
        self.cadencia = 750
        self.velocidad_inicial = 0
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self):
        self.velocidad_x = 0
        # mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 5
            self.image = pygame.image.load(os.path.join(configuracion.carpeta_imagen, f"Imagen{self.df}.tif")).convert()
            self.image = pygame.transform.scale(self.image, tamano_imagen)
            self.image.set_colorkey(configuracion.NEGRO)

        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -5
            self.image = pygame.image.load(
                os.path.join(configuracion.carpeta_ezquierda, f"Imagen{self.df}.tif")).convert()
            self.image = pygame.transform.scale(self.image, tamano_imagen)
            self.image.set_colorkey(configuracion.NEGRO)
        if teclas[pygame.K_SPACE]:
            self.df = random.randrange(1, 7)
            self.image = pygame.image.load(os.path.join(configuracion.carpeta_imagen, f"Imagen{self.df}.tif")).convert()
            self.image = pygame.transform.scale(self.image, (84, 84))
            self.image.set_colorkey(configuracion.NEGRO)
        self.i = random.randrange(1, 10)
        if self.i == 1:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                self.disparo()
                self.ultimo_disparo = ahora
        if self.rect.bottom >= NIVEL_SUELO:
            self.rect.bottom = NIVEL_SUELO
            # solo evalúa un salto si está en el suelo.

            if teclas[pygame.K_UP]:
                self.velocidad_inicial = -10
                self.actualizar_salto()
        else:
            self.actualizar_salto()
        # actuliza la posicion del personaje
        self.rect.x += self.velocidad_x
        if self.rect.left < 0:
            self.rect.left = 0

        # Limita el margen derecho
        if self.rect.right > configuracion.ANCHO:
            self.rect.right = configuracion.ANCHO

    def actualizar_salto(self):
        # si está saltando actualiza su posición
        self.rect.y += self.velocidad_inicial
        self.velocidad_inicial += 0.5
    def disparo(self):
        bala = Disparo(self.rect.centerx, self.rect.top)
        configuracion.bala_grupo2.add(bala)
        configuracion.sonido_disparo.play()




class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join(configuracion.carpeta_explo, "disparo2.tif")).convert(), (10, 20))
        self.image.set_colorkey(configuracion.NEGRO)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def kill(self):
        super(Disparo, self).kill()
        explo = Explosion(self.rect.centerx, self.rect.centery)
        configuracion.animacion_explp.add(explo)

    def update(self):
        self.rect.y -= 25
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(4, 10):
            img = pygame.image.load(os.path.join(configuracion.carpeta_explo, f"Imagen{num}.tif"))
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
