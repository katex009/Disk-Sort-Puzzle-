import pygame
from pathlib import Path
from src.utils.asset import load_image, load_music, load_sound

pygame.init()


class play_state:

    def __init__(self):
        self.fondo = load_image("images/game/fondo.png")
        self.rect = self.fondo.get_rect()
        self.base = load_image("images/game/base.png")

        self.capacity = 4
        self.selected_stack = None
        self.next_state = None
        self.won_sound_played = False

        self.disks = {
            "rojo": load_image("images/game/disco_rojo.png"),
            "azul": load_image("images/game/disco_azul.png"),
            "verde": load_image("images/game/disco_verde.png"),
            "amarillo": load_image("images/game/disco_amarillo.png"),
            "morado": load_image("images/game/disco_morado.png"),
            "naranja": load_image("images/game/disco_rosa.png"),
        }

        self.stacks = [
            ["amarillo", "verde", "azul", "rojo"],
            ["rojo", "naranja", "morado", "azul"],
            ["morado", "azul", "amarillo", "verde"],
            ["naranja", "morado", "verde", "amarillo"],
            ["verde", "rojo", "naranja", "morado"],
            ["azul", "amarillo", "rojo", "naranja"],
            [],
            [],
        ]

        self.stack_centers = [
            (220, 180),
            (500, 180),
            (780, 180),
            (1060, 180),
            (220, 460),
            (500, 460),
            (780, 460),
            (1060, 460),
        ]

        self.stack_rects = []
        disk_sample = next(iter(self.disks.values()))
        disk_w, disk_h = disk_sample.get_size()
        self.stack_height = disk_h * self.capacity
        for cx, cy in self.stack_centers:
            self.stack_rects.append(
                pygame.Rect(cx - disk_w // 2 - 15, cy - 15, disk_w + 30, self.stack_height + 35)
            )

        font_path = Path(__file__).resolve().parents[2] / "assets" / "fonts" / "Handy Pen.ttf"
        self.ui_font = pygame.font.Font(str(font_path), 50)
        self.select_color = (245, 213, 105)
        self.hover_color = (255, 255, 255)
        self.win_sound = load_sound("sounds/ganar.mp3", volume=0.35)

        load_music("sounds/juego.mp3", volume=0.3, loop=-1)

    def handle_events(self, events):
        if self.next_state is not None:
            return self.next_state

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "pause"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked_stack = self._find_clicked_stack(event.pos)
                if clicked_stack is not None:
                    self._handle_stack_click(clicked_stack)

        return None

    def update(self, dt):
        if self._is_solved():
            if not self.won_sound_played:
                self.win_sound.play()
                self.won_sound_played = True
            self.next_state = "game_over"

    def render(self, surface):
        surface.blit(self.fondo, self.rect)

        mouse_pos = pygame.mouse.get_pos()
        for idx, stack_rect in enumerate(self.stack_rects):
            if idx == self.selected_stack:
                pygame.draw.rect(surface, self.select_color, stack_rect, 3, border_radius=8)
            elif stack_rect.collidepoint(mouse_pos):
                pygame.draw.rect(surface, self.hover_color, stack_rect, 2, border_radius=8)

        for idx, stack in enumerate(self.stacks):
            center_x, top_y = self.stack_centers[idx]
            base_y = top_y + self.stack_height
            base_rect = self.base.get_rect(midtop=(center_x, base_y))
            surface.blit(self.base, base_rect)

            for level, color in enumerate(stack):
                disk_image = self.disks[color]
                disk_top = base_y - ((level + 1) * disk_image.get_height())
                disk_rect = disk_image.get_rect(midtop=(center_x, disk_top))
                surface.blit(disk_image, disk_rect)

        help_text = self.ui_font.render("Ordena los colores, seleccionando los discos y su destino", True, (255, 255, 255))
        help_rect = help_text.get_rect(center=(surface.get_width() // 2, 85))
        surface.blit(help_text, help_rect)

    def _find_clicked_stack(self, pos):
        for idx, stack_rect in enumerate(self.stack_rects):
            if stack_rect.collidepoint(pos):
                return idx
        return None

    def _handle_stack_click(self, stack_idx):
        if self.selected_stack is None:
            if self.stacks[stack_idx]:
                self.selected_stack = stack_idx
            return

        if self.selected_stack == stack_idx:
            self.selected_stack = None
            return

        self._try_move(self.selected_stack, stack_idx)
        self.selected_stack = None

    def _try_move(self, source_idx, target_idx):
        source = self.stacks[source_idx]
        target = self.stacks[target_idx]
        if not source or len(target) >= self.capacity:
            return

        source_color = source[-1]
        if target and target[-1] != source_color:
            return

        target.append(source.pop())

    def _is_solved(self):
        non_empty_stacks = 0
        for stack in self.stacks:
            if not stack:
                continue

            non_empty_stacks += 1
            if len(stack) != self.capacity:
                return False
            if any(color != stack[0] for color in stack):
                return False

        return non_empty_stacks > 0
