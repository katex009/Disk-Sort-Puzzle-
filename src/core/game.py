from enfocate import GameBase, GameMetadata
import pygame
from src.core.states.menu_state import menu_state
from src.core.states.play_state import play_state
from src.core.states.pause_state import pause_state
from src.core.states.game_over_state import game_over_state

pygame.init()


class myGame(GameBase):

    def __init__(self) -> None:
        ###
        x=1
        meta = GameMetadata(
            title="Disk Sort Puzzle",
            description="juego puzzle para ni\u00f1os con TDAH",
            authors=["Rene Franco"],
            group_number=11
        )
        super().__init__(meta)

        self.state = menu_state()
        self.previous_state = None
        self.play_state_instance = None
        self.game_over_state_instance = game_over_state()
        self.music_paused = False

    def handle_events(self, events):

        next_state = self.state.handle_events(events)
        if next_state == "play":
            if self.play_state_instance is None:
                self.play_state_instance = play_state()
            self.state = self.play_state_instance
        elif next_state == "pause":
            if pygame.mixer.get_init():
                pygame.mixer.music.pause()
                self.music_paused = True
            self.previous_state = self.state
            self.state = pause_state(self.previous_state)
        elif next_state == "resume":
            if self.music_paused and pygame.mixer.get_init():
                pygame.mixer.music.unpause()
                self.music_paused = False
            self.state = self.previous_state
        elif next_state == "menu":
            self.music_paused = False
            self.state = menu_state()
        elif next_state == "game_over":
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
            self.music_paused = False
            self.state = self.game_over_state_instance

    def update(self, dt):
        self.state.update(dt)

    def draw(self):
        self.state.render(self.surface)
