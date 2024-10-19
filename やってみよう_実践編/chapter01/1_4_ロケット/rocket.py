import pygame


class Rocket:
    """ロケットを管理するクラス"""

    def __init__(self, r_game):
        """ロケットを初期化し開始位置に配置する"""
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.screen_rect = r_game.screen.get_rect()

        # ロケットの画像を読み込みrectを取得する
        #   ロケットの画像: https://opengameart.org/content/rocket
        #   ライセンス: https://creativecommons.org/licenses/by/3.0/
        #   画像はリサイズされている
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # 新しいロケットの開始位置は画面の中央
        self.rect.center = self.screen_rect.center

        # ロケットの水平、垂直の位置を浮動小数点数で保存する
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移動のフラグ
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):
        """ロケットの位置を移動フラグを元に更新する"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # 位置の属性からrectを更新する
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """ロケットを現在の位置に描画する"""
        self.screen.blit(self.image, self.rect)
