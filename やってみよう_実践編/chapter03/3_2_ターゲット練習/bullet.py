import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """宇宙船から発射される弾を管理するクラス"""

    def __init__(self, ss_game):
        """宇宙船の現在の位置から弾のオブジェクトを生成する"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        # 弾のrectを(0, 0)の位置に作成してから、正しい位置を設定する
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midright = ss_game.ship.rect.midright
        
        # 弾の位置を浮動小数点数で保存する
        self.x = float(self.rect.x)

    def update(self):
        """画面上の弾を移動する"""
        # 弾の浮動小数点数での位置を更新する
        self.x += self.settings.bullet_speed
        # rectの位置を更新する
        self.rect.x = self.x

    def draw_bullet(self):
        """画面に弾を描画する"""
        pygame.draw.rect(self.screen, self.color, self.rect)
