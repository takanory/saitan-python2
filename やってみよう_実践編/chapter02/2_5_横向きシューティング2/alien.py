from random import randint

import pygame
from pygame.sprite import Sprite
 

class Alien(Sprite):
    """エイリアンを表すクラス"""

    def __init__(self, ss_game):
        """エイリアンを初期化し、開始時の位置を設定する"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # エイリアンの画像を読み込み、rectを取得する
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # 新しいエイリアンをp画面の右端のランダムな位置に配置する
        self.rect.left = self.screen.get_rect().right
        # 画面の一番下に配置するエイリアンの位置は、画面の高さからエイリアンの高さを引いた値
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        # エイリアンの水平の位置を浮動小数点数で保存する
        self.x = float(self.rect.x)

    def update(self):
        """エイリアンを左に移動する"""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
