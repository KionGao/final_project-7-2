from __future__ import annotations
import pygame
import os
from settings import *
import pygame.freetype
from pygame import mixer

mixer.music.load('music','Choosing.wav')
mixer.music.play(-1)

class an_event:
    def __init__(self,question:an_question,select1:an_decision,select2:an_decision,select3:an_decision) -> None:
        self.question = question
        self.select1 = select1
        self.select2 = select2
        self.select3 = select3
        pass


class an_decision():
    def __init__(self, num:int,image:pygame.Surface , impact:list,notify_image:pygame.Surface) -> None:
        self.impact = impact
        self.notify =notify_image
        self.image = pygame.transform.scale(image, (400, 60))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (165+200,200+(num-1)*100+30)
        self.frame = pygame.Rect(165+200 - 205, 200+(num-1)*100+30 - 35, 405 + 5, 60 + 10)
        self.selected = None
        
class an_question:
    def __init__(self,num:int,image:pygame.Surface) -> None:
        if image.get_height()>300:
            self.image = pygame.transform.scale(image, (590, 80))
        else:
            self.image = pygame.transform.scale(image, (590, 40))
            
        self.image_rect = self.image.get_rect()
        self.image_rect.center=(400,120)
        pass
class Buttons:
    def __init__(self,name:str,image:pygame.Surface,x:int,y:int) -> None:
        self.name = name
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.center = x,y
    def is_clicked(self,x:int,y:int):
        return True if self.image_rect.collidepoint(x,y)  else False
#images
BACKGROUND_IMAGE_CHOOSE_PLAYER = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "choose_character.png")), (WIN_WIDTH, WIN_HEIGHT))
BACKGROUND_IMAGE_EVENT = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "make_a_choice.png")), (WIN_WIDTH, WIN_HEIGHT))
START_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "yes.png")), (200, 60))
START_ROUND = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "start_round.png")), (200, 60))
LEVEL1 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level1.png")), (140, 40))
LEVEL2 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level2.png")), (140, 40))
LEVEL3 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level3.png")), (140, 40))
LEVEL4 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level4.png")), (140, 40))
LEVEL5 = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "level5.png")), (140, 40))
MUTE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "mute.png")), (30, 30))
SOUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "sound.png")), (30, 30))
PAUSE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "pause.png")), (25, 25))
PLAY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "play.png")), (25, 25))
LAST_PAGE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "return.png")), (25, 25))
MUTE_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "mute_black.png")), (30, 30))
SOUND_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "sound_black.png")), (30, 30))
PAUSE_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "pause_black.png")), (25, 25))
PLAY_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "play_black.png")), (25, 25))
LAST_PAGE_IMAGE_BLACK = pygame.transform.scale(pygame.image.load(os.path.join("images1/buttons", "return_black.png")), (25, 25))
BACK_MENU = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "bank_menu.png")), (235, 100))
READ_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "read_button.png")), (235, 100))
BACKGROUND_IMAGE_MESSAGE = pygame.transform.scale(pygame.image.load(os.path.join("images1/choice_page", "message_page.png")), (WIN_WIDTH, WIN_HEIGHT))
