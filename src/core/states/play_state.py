import pygame
from src.utils.asset import load_image, load_music

pygame.init()


class play_state:

    def __init__(self):
        self.fondo = load_image("images/game/fondo.png")
        self.rect = self.fondo.get_rect()
        self.base = load_image("images/game/base.png")

        stack_center_x = 640
        current_y = 120

        self.disco_amarillo = load_image("images/game/disco_amarillo.png")
        self.disco_amarillo_rect = self.disco_amarillo.get_rect(midtop=(stack_center_x, current_y))

        current_y = self.disco_amarillo_rect.bottom 
        self.disco_azul = load_image("images/game/disco_azul.png")
        self.disco_azul_rect = self.disco_azul.get_rect(midtop=(stack_center_x, current_y))

        current_y = self.disco_azul_rect.bottom 
        self.disco_morado = load_image("images/game/disco_morado.png")
        self.disco_morado_rect = self.disco_morado.get_rect(midtop=(stack_center_x, current_y))

        current_y = self.disco_morado_rect.bottom 
        self.disco_rojo = load_image("images/game/disco_rojo.png")
        self.disco_rojo_rect = self.disco_rojo.get_rect(midtop=(stack_center_x, current_y))

        current_y = self.disco_rojo_rect.bottom 
        self.disco_rosa = load_image("images/game/disco_rosa.png")
        self.disco_rosa_rect = self.disco_rosa.get_rect(midtop=(stack_center_x, current_y))

        current_y = self.disco_rosa_rect.bottom 
        self.disco_verde = load_image("images/game/disco_verde.png")
        self.disco_verde_rect = self.disco_verde.get_rect(midtop=(stack_center_x, current_y))

        stack_bottom = self.disco_verde_rect.bottom
        self.base_rect = self.base.get_rect(midtop=(stack_center_x, stack_bottom))

        load_music("sounds/juego.mp3", volume=0.3, loop=-1)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "pause"
        return None

    def update(self, dt):
        pass

    def render(self, surface):
        surface.blit(self.fondo, self.rect)
        surface.blit(self.base, self.base_rect)
        surface.blit(self.disco_amarillo, self.disco_amarillo_rect)
        surface.blit(self.disco_azul, self.disco_azul_rect)
        surface.blit(self.disco_morado, self.disco_morado_rect)
        surface.blit(self.disco_rojo, self.disco_rojo_rect)
        surface.blit(self.disco_rosa, self.disco_rosa_rect)
        surface.blit(self.disco_verde, self.disco_verde_rect)
