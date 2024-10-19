import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """1つの星を管理するクラス"""

    def __init__(self, stars_game):
        """星を初期化し開始位置に配置する"""
        super().__init__()
        self.screen = stars_game.screen

        # 星の画像を読み込みrectを取得する
        #   星の画像: https://opengameart.org/content/star
        #   ライセンス: public domain
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # 新しい星の最初の位置は画面の左上
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 注: 星は動かないため星の位置を追跡する必要はない
