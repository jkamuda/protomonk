__author__ = 'jkamuda'

from src.spritesheet import SpriteSheet
from src import coordinates as coords, utils
from src import constants as c


class TextHelper():
    def __init__(self):
        self.color_key = (92, 148, 252)

        self.text_dict = {}

        self.init_image_dictionary()

    def init_image_dictionary(self):
        ss = SpriteSheet("data/text_images.png")

        self.text_dict['0'] = ss.get_image(coords.NUM_0)
        self.text_dict['1'] = ss.get_image(coords.NUM_1)
        self.text_dict['2'] = ss.get_image(coords.NUM_2)
        self.text_dict['3'] = ss.get_image(coords.NUM_3)
        self.text_dict['5'] = ss.get_image(coords.NUM_5)
        self.text_dict['4'] = ss.get_image(coords.NUM_4)
        self.text_dict['6'] = ss.get_image(coords.NUM_6)
        self.text_dict['7'] = ss.get_image(coords.NUM_7)
        self.text_dict['8'] = ss.get_image(coords.NUM_8)
        self.text_dict['9'] = ss.get_image(coords.NUM_9)

        self.text_dict['a'] = ss.get_image(coords.CHAR_A)
        self.text_dict['b'] = ss.get_image(coords.CHAR_B)
        self.text_dict['c'] = ss.get_image(coords.CHAR_C)
        self.text_dict['d'] = ss.get_image(coords.CHAR_D)
        self.text_dict['e'] = ss.get_image(coords.CHAR_E)
        self.text_dict['f'] = ss.get_image(coords.CHAR_F)
        self.text_dict['g'] = ss.get_image(coords.CHAR_G)
        self.text_dict['h'] = ss.get_image(coords.CHAR_H)
        self.text_dict['i'] = ss.get_image(coords.CHAR_I)
        self.text_dict['j'] = ss.get_image(coords.CHAR_J)
        self.text_dict['k'] = ss.get_image(coords.CHAR_K)
        self.text_dict['l'] = ss.get_image(coords.CHAR_L)
        self.text_dict['m'] = ss.get_image(coords.CHAR_M)
        self.text_dict['n'] = ss.get_image(coords.CHAR_N)
        self.text_dict['o'] = ss.get_image(coords.CHAR_O)
        self.text_dict['p'] = ss.get_image(coords.CHAR_P)
        self.text_dict['q'] = ss.get_image(coords.CHAR_Q)
        self.text_dict['r'] = ss.get_image(coords.CHAR_R)
        self.text_dict['s'] = ss.get_image(coords.CHAR_S)
        self.text_dict['t'] = ss.get_image(coords.CHAR_T)
        self.text_dict['u'] = ss.get_image(coords.CHAR_U)
        self.text_dict['v'] = ss.get_image(coords.CHAR_V)
        self.text_dict['w'] = ss.get_image(coords.CHAR_W)
        self.text_dict['x'] = ss.get_image(coords.CHAR_X)
        self.text_dict['y'] = ss.get_image(coords.CHAR_Y)
        self.text_dict['z'] = ss.get_image(coords.CHAR_Z)

        self.text_dict['+'] = ss.get_image(coords.XXX)
        self.text_dict['-'] = ss.get_image(coords.HYPHEN)
        self.text_dict['!'] = ss.get_image(coords.EXCLAIMATION)

        for key in self.text_dict:
            image = self.text_dict[key]
            image = utils.scale_image(image, c.IMG_MULTIPLIER)
            image.set_colorkey(self.color_key)
            self.text_dict[key] = image

    def get_text(self, key):
        return self.text_dict[key.lower()]
