import pygame
from src.utils.asset import load_image

pygame.init()


class game_over_state:

    def __init__(self):
        self.background = load_image("images/game-over/game_over.png")
        self.rect = self.background.get_rect()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_ESCAPE):
                    return "menu"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return "menu"
        return None

    def update(self, dt):
        pass

    def render(self, surface):
        self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
        surface.blit(self.background, self.rect)
