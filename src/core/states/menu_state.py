import pygame
from src.utils.asset import load_image, load_music

pygame.init()


class menu_state:

    def __init__(self):

        self.background = load_image("images/menu/menu.png")
        self.rect = self.background.get_rect()

        self.start_image = load_image("images/menu/start.png", (89, 59))
        self.start_rect = self.start_image.get_rect()

        self.start_rect.x = 595.2
        self.start_rect.y = 413.1

        self.start_image2 = load_image("images/menu/start2.png", (89, 59))
        self.actual_start_image = self.start_image

        self.exit_image = load_image("images/menu/exit.png", (89, 59))
        self.exit_rect = self.exit_image.get_rect()

        self.exit_rect.x = 595.2
        self.exit_rect.y = 525.4

        self.exit_image2 = load_image("images/menu/exit2.png", (89, 59))
        self.actual_exit_image = self.exit_image

        load_music("sounds/menu_music.mp3", volume=0.3, loop=0)

    def render(self, surface):
        surface.blit(self.background, self.rect)
        surface.blit(self.actual_start_image, self.start_rect)
        surface.blit(self.actual_exit_image, self.exit_rect)

    def update(self, dt):
        if pygame.get_init():
            mouse_pos = pygame.mouse.get_pos()

            if self.start_rect.collidepoint(mouse_pos):
                self.actual_start_image = self.start_image2
            else:
                self.actual_start_image = self.start_image

            if self.exit_rect.collidepoint(mouse_pos):
                self.actual_exit_image = self.exit_image2
            else:
                self.actual_exit_image = self.exit_image

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.start_rect.collidepoint(event.pos):
                    return "play"
                if self.exit_rect.collidepoint(event.pos):
                    pygame.quit()
        return None
