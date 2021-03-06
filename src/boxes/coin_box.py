__author__ = 'jkamuda'

import pygame

from box import Box
from src import coordinates as coords
from src import constants as c
from src.spritesheet import SpriteSheet
from src.coin import Coin
from src.score import Score


class CoinBox(Box):
    def __init__(self, sound_manager, x, y, num_coins=1):
        Box.__init__(self, sound_manager, x, y)

        self.num_coins = num_coins
        self.empty_frame = None
        self.coin_box_frames = []
        self.frame_idx = 0
        self.coin_box_time = 0
        self.game_time = 0
        self.transition_time = 0

        self.coin_score_group = pygame.sprite.Group()

        self.init_frames()
        self.refresh_image(self.coin_box_frames[0])

    def init_frames(self):
        sprite_sheet = SpriteSheet("data/tile_set.png")

        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_1, c.IMG_MULTIPLIER, c.WHITE))
        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_2, c.IMG_MULTIPLIER, c.WHITE))
        self.coin_box_frames.append(sprite_sheet.get_image(coords.COIN_BOX_3, c.IMG_MULTIPLIER, c.WHITE))

        self.empty_frame = sprite_sheet.get_image(coords.COIN_BOX_EMPTY, c.IMG_MULTIPLIER, c.WHITE)

    def shift_world(self, shift):
        super(CoinBox, self).shift_world(shift)
        for item in self.coin_score_group:
            item.shift_world(shift)

    def activate(self):
        if self.num_coins > 0:
            self.in_transition = True
            self.y_offset = 10
            self.sound_manager.play_sound(c.SOUND_COIN)
            self.start_coin_animation()
            self.num_coins -= 1
            return 200, 1
        else:
            self.sound_manager.play_sound(c.SOUND_BUMP)
            return 0, 0

    def update(self, game_time):
        time_delta = (game_time - self.game_time)
        self.coin_box_time += time_delta
        self.transition_time = self.coin_box_time
        self.game_time = game_time

        if self.num_coins == 0:
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

        for item in self.coin_score_group:
            item.update(game_time)
            if isinstance(item, Coin):
                if not item.is_bouncing:
                    item.kill()
                    score = Score(self.rect.x + 5, self.rect.y - 25, c.SCORE_COIN)
                    self.coin_score_group.add(score)

    def start_coin_animation(self):
        coin = Coin(self.rect.x + (self.rect.width / 2), self.rect.y - self.y_offset - 40)
        coin.start_coin_bounce()
        self.coin_score_group.add(coin)

    def draw(self, screen):
        super(CoinBox, self).draw(screen)
        for item in self.coin_score_group:
            item.draw(screen)
