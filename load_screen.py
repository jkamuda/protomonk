__author__ = 'jkamuda'

from game_state import GameState
from texthelper import TextHelper
from spritesheet import SpriteSheet
import constants as c
import coordinates as coords


class LoadScreen(GameState):

    mario_frame = None

    background = None
    load_screen_time = -1
    text_helper = None
    game_info = None

    def __init__(self):
        GameState.__init__(self, GameState.STATE_LOAD, GameState.STATE_MENU)

        #self.game_info = game_info
        self.text_helper = TextHelper()

        # Mario frame
        sprite_sheet = SpriteSheet("data\characters.gif")
        self.mario_frame = sprite_sheet.get_image_v2(coords.MARIO_SMALL_STANDING_RIGHT, c.IMG_MULTIPLIER)

    def update(self, game_time):
        if self.load_screen_time == -1:
            self.load_screen_time = game_time
        elif (game_time - self.load_screen_time) > 2000:
            self.switch = True

    def draw(self, screen):
        screen.fill(c.BLACK)

        screen.blit(self.text_helper.get_text('w'), (280, 200))
        screen.blit(self.text_helper.get_text('o'), (300, 200))
        screen.blit(self.text_helper.get_text('r'), (320, 200))
        screen.blit(self.text_helper.get_text('l'), (340, 200))
        screen.blit(self.text_helper.get_text('d'), (360, 200))

        screen.blit(self.text_helper.get_text('1'), (420, 200))
        screen.blit(self.text_helper.get_text('-'), (440, 205))
        screen.blit(self.text_helper.get_text('1'), (460, 200))

        screen.blit(self.text_helper.get_text('+'), (390, 270))

        screen.blit(self.mario_frame, (320, 250))

        screen.blit(self.text_helper.get_text('3'), (430, 265))
