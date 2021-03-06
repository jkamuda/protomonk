__author__ = 'jkamuda'

from enemy import Enemy
from src.spritesheet import SpriteSheet
import src.constants as c
import src.coordinates as coords


class Goomba(Enemy):
    def __init__(self, x, y, direction=c.DIR_RIGHT):
        Enemy.__init__(self, x, y, c.SCORE_GOOMBA, direction)

        self.goomba_frames = []
        self.dead_frame = None
        self.x_vel = 2

        self.init_frames()
        self.refresh_image(self.goomba_frames[0])

    def init_frames(self):
        sprite_sheet = SpriteSheet("data/characters.gif")

        self.goomba_frames.append(sprite_sheet.get_image(coords.GOOMBA_LEFT, c.IMG_MULTIPLIER, c.BLUE))
        self.goomba_frames.append(sprite_sheet.get_image(coords.GOOMBA_RIGHT, c.IMG_MULTIPLIER, c.BLUE))
        self.dead_frame = sprite_sheet.get_image(coords.GOOMBA_DEAD, c.IMG_MULTIPLIER, c.BLUE)

    def update(self, game_time, viewport):
        time_delta = game_time - self.enemy_time
        if self.state == c.ENEMY_STATE_DEAD:
            self.image = self.dead_frame
            if time_delta > 1000:
                self.kill()
        elif self.state == c.ENEMY_STATE_ALIVE:
            if time_delta > 250:
                if self.frame_idx == 0:
                    self.frame_idx = 1
                else:
                    self.frame_idx = 0
                self.enemy_time = game_time
            self.image = self.goomba_frames[self.frame_idx]

            self.calc_gravity()
            if self.direction == c.DIR_RIGHT:
                self.x_vel = 2
            else:
                self.x_vel = -2

            self.x += self.x_vel
            self.rect.y += self.y_vel

        self.refresh_rect()
        self.rect.x = self.x + viewport