import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from settings import FPS,ALL_PASS_BG, WIN_STAGE_BG
from pygame import mixer  #音樂新增

pygame.mixer.init
pygame.mixer.music.load("music","bg_music.wav")

class Game:
    def __init__(self,player:int) -> None:
        print('build game')
        self.game_model = GameModel(player)  # core of the game (database, game logic...)
        self.game_view = GameView(player)  # render everything
        self.keep_going = False
        self.all_pass = False
        self.player = player
        self.fail = False
        self.quit_game = False
        pass
    def run(self):
        # initialization
        pygame.init()
        game_control = GameControl(self.game_model, self.game_view)  # deal with the game flow and user request
        self.keep_going = False
        while (not self.quit_game) and (not self.keep_going) and not self.all_pass and not self.fail:
            pygame.time.Clock().tick(FPS*20)  # control the frame rate
            game_control.receive_user_input()  # receive user input
            game_control.update_model()  # update the model
            game_control.update_view()  # update the view
            pygame.display.update()
            self.keep_going = game_control.keep_going
            self.fail = game_control.fail
            self.quit_game = game_control.quit_game
        if self.quit_game:
            pass
        elif self.fail:
            self.keep_going = False
        elif self.keep_going :
            self.game_model.seller.update(self.game_model)
            if self.game_model.stage == 2:
                self.all_pass = True
                self.keep_going = False
            else:
                pass
        print(self.keep_going,self.fail,self.all_pass,self.quit_game)
        return self.quit_game
    def mute(self,mute:bool):
        self.game_model.mute = mute
        

class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()
    
