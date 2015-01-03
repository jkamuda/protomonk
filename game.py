__author__ = 'jkamuda'

import os
import pygame
import constants
from player import Player
from sound import SoundManager
from menu import Menu
from overhead import Overhead
from game_state import GameState
from load_screen import LoadScreen


class Game():
    screen = None
    caption = 'NES Mario'
    sound_manager = None

    def __init__(self):
        # Center window on screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()

        size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

        self.sound_manager = SoundManager()

    def get_game_state(self, game_state):
        if game_state == GameState.STATE_MENU:
            return Menu()
        if game_state == GameState.STATE_LOAD:
            return LoadScreen()

    def run(self):
        pygame.display.set_caption(self.caption)

        running = True
        clock = pygame.time.Clock()

        active_sprite_list = pygame.sprite.Group()
        player = Player(self.sound_manager)
        player.rect.x = 100
        player.rect.bottom = constants.GROUND_HEIGHT

        active_sprite_list.add(player)

        #self.sound_manager.play_music(constants.MUSIC_MAIN_THEME)

        overhead_info = Overhead()
        game_state = self.get_game_state(GameState.STATE_MENU)

        while running:
            game_time = pygame.time.get_ticks()

            if game_state.switch_state():
                game_state = self.get_game_state(game_state.next)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_ESCAPE or key == pygame.K_q:
                        running = False

            game_state.process_events(events)

            game_state.update(game_time)

            game_state.draw(self.screen)
            overhead_info.draw(self.screen, game_time)

            # limit to 60 frames per second
            clock.tick(60)

            # update screen
            pygame.display.flip()

        pygame.quit()
