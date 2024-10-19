import pygame
 
class Ship:
    """宇宙船を管理するクラス"""

    def __init__(self, ss_game):
        """宇宙船を初期化し、開始時の位置を設定する"""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # 宇宙船の画像を読み込み、rectを取得する
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # 新しい宇宙船の開始位置は画面左端の中央
        self.center_ship()

        # 移動のフラグ
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """宇宙船の位置を移動フラグを元に更新する"""
        # rectではなく、宇宙船のY座標を更新する
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # self.yからrectを更新する
        self.rect.y = self.y

    def center_ship(self):
        """宇宙船の位置を画面左端の中央にする"""
        self.rect.midleft = self.screen_rect.midleft

        # 宇宙船の垂直の位置を浮動小数点数で保存する
        self.y = float(self.rect.y)

    def blitme(self):
        """宇宙船を現在の位置に描画する"""
        self.screen.blit(self.image, self.rect)
