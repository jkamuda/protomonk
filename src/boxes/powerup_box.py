__author__ = 'jkamuda'

import pygame

from src import coordinates as coords
from .. import constants as c
from src.spritesheet import SpriteSheet
from src.powerups.mushroom import Mushroom


class PowerUpBox(pygame.sprite.Sprite):
    def __init__(self, sound_manager, group, x, y, powerup=c.POWERUP_MUSHROOM):
        pygame.sprite.Sprite.__init__(self)

        self.sound_manager = sound_manager
        self.group = group
        self.powerup = powerup
        self.empty_frame = None
        self.display_frame = None
        self.coin_box_frames = []
        self.frame_idx = 0
        self.coin_box_time = 0
        self.game_time = 0
        self.in_transition = False
        self.transition_time = 0
        self.y_offset = 0
        self.empty = False

        self.shift = 0

        self.powerup_group = pygame.sprite.Group()

        self.init_frames()

        self.image = self.coin_box_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def init_frames(self):
        sprite_sheet = SpriteSheet("data\\tile_set.png")

        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_1, c.IMG_MULTIPLIER, c.WHITE))
        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_2, c.IMG_MULTIPLIER, c.WHITE))
        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_3, c.IMG_MULTIPLIER, c.WHITE))

        self.empty_frame = sprite_sheet.get_image(coords.COIN_BOX_EMPTY, c.IMG_MULTIPLIER, c.WHITE)

    def shift_world(self, shift):
        self.rect.x += shift
        self.shift += shift

    def activate(self):
        if not self.empty:
            self.in_transition = True
            self.y_offset = 10
            self.sound_manager.play_sound(c.SOUND_POWERUP_APPEARS)
            self.spawn_powerup()
            return 0, 0
        else:
            self.sound_manager.play_sound(c.SOUND_BUMP)
            return 0, 0

    def update(self, game_time):
        time_delta = (game_time - self.game_time)
        self.coin_box_time += time_delta
        self.transition_time = self.coin_box_time
        self.game_time = game_time

        if self.empty:
            self.display_frame = self.empty_frame
        else:
            if 0 < self.coin_box_time <= 400:
                self.frame_idx = 0
            elif 400 < self.coin_box_time <= 600:
                self.frame_idx = 1
            elif 600 < self.coin_box_time <= 700:
                self.frame_idx = 2
            elif self.coin_box_time > 700:
                self.frame_idx = 0
                self.coin_box_time = 0

            self.display_frame = self.coin_box_frames[self.frame_idx]

        if self.in_transition is True:
            if self.transition_time > 10:
                self.y_offset -= 1
                self.transition_time = 0
            if self.y_offset == 0:
                self.in_transition = False
        else:
            self.transition_time = 0

    def spawn_powerup(self):
        powerup = Mushroom(self.rect.x, self.rect.top)
        self.group.add(powerup)
        self.empty = True

    def draw(self, screen):
        screen.blit(self.display_frame, (self.rect.x, self.rect.y - self.y_offset))
