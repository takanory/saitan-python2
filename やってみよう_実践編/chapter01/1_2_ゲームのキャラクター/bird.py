import pygame


class Bird:
    """トリを管理するクラス"""

    def __init__(self, bb_game):
        """トリを初期化し開始位置に配置する"""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        # トリの画像を読み込みrectを取得する
        # トリの画像: https://opengameart.org/content/game-character-blue-flappy-bird-sprite-sheets
        self.image = pygame.image.load('images/bird_small.bmp')
        self.rect = self.image.get_rect()

        # Start each new bird at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """現在の位置にトリを描画する"""
        self.screen.blit(self.image, self.rect)
