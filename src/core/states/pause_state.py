import pygame
from pathlib import Path

pygame.init()


class pause_state:

    def __init__(self, previous_state):
        self.previous_state = previous_state

        font_path = Path(__file__).resolve().parents[2] / "assets" / "fonts" / "Handy Pen.ttf"
        self.title_font = pygame.font.Font(str(font_path), 150)
        self.button_font = pygame.font.Font(str(font_path), 84)

        self.normal_color = (255, 255, 255)
        self.hover_color = (245, 213, 105)

        self.pause_text = "Pause"
        self.resume_text = "Resume"
        self.exit_text = "Exit"

        self.pause_rect = pygame.Rect(0, 0, 0, 0)
        self.resume_rect = pygame.Rect(0, 0, 0, 0)
        self.main_menu_rect = pygame.Rect(0, 0, 0, 0)

    def render(self, surface):
        self.previous_state.render(surface)

        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        surface.blit(overlay, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        title_surface = self.title_font.render(self.pause_text, True, self.normal_color)
        resume_color = self.hover_color if self.resume_rect.collidepoint(mouse_pos) else self.normal_color
        exit_color = self.hover_color if self.main_menu_rect.collidepoint(mouse_pos) else self.normal_color

        resume_surface = self.button_font.render(self.resume_text, True, resume_color)
        exit_surface = self.button_font.render(self.exit_text, True, exit_color)

        width, height = surface.get_size()
        self.pause_rect = title_surface.get_rect(center=(width // 2, height // 2 - 190))
        self.resume_rect = resume_surface.get_rect(center=(width // 2, height // 2 - 20))
        self.main_menu_rect = exit_surface.get_rect(center=(width // 2, height // 2 + 80))

        surface.blit(title_surface, self.pause_rect)
        surface.blit(resume_surface, self.resume_rect)
        surface.blit(exit_surface, self.main_menu_rect)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "resume"

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.resume_rect.collidepoint(event.pos):
                        return "resume"

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.main_menu_rect.collidepoint(event.pos):
                        return "menu"
        return None

    def update(self, dt):
        pass
