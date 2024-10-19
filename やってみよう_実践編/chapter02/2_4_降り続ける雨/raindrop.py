import pygame
from pygame.sprite import Sprite
 

class Raindrop(Sprite):
    """1つの雨粒を管理するクラス"""

    def __init__(self, rd_game):
        """雨粒を初期化し開始位置に配置する"""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # 雨粒の画像を読み込みrectを取得する
        #   雨粒の画像: https://commons.wikimedia.org/wiki/File:Antu_raindrop.svg
        #   ライセンス: https://creativecommons.org/licenses/by-sa/3.0/deed.en
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # 新しい雨粒の最初の位置は画面の左上
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 雨粒のY座標を格納する
        self.y = float(self.rect.y)

    def check_disappeared(self):
        """雨粒が画面の下から消えたか確認する"""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """雨粒を画面の下に移動する"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
