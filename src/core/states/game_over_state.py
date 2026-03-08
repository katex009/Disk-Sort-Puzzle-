import pygame
from src.utils.asset import load_image
from pathlib import Path

pygame.init()


class game_over_state:

    def __init__(self):
        self.background = load_image("images/game-over/game_over.png")
        self.rect = self.background.get_rect()

        font_path = Path(__file__).resolve().parents[2] / "assets" / "fonts" / "Handy Pen.ttf"
        self.button_font = pygame.font.Font(str(font_path), 52)
        self.button_text = "Menu"
        self.button_normal_color = (245, 213, 105)
        self.button_hover_color = (200, 160, 255)
        self.button_rect = pygame.Rect(0, 0, 0, 0)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_ESCAPE):
                    return "menu"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    return "menu"
        return None

    def update(self, dt):
        pass

    def render(self, surface):
        self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
        surface.blit(self.background, self.rect)

        mouse_pos = pygame.mouse.get_pos()
        text_color = self.button_hover_color if self.button_rect.collidepoint(mouse_pos) else self.button_normal_color
        menu_surface = self.button_font.render(self.button_text, True, text_color)
        self.button_rect = menu_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() - 90))
        surface.blit(menu_surface, self.button_rect)
