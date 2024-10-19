import pygame
 

class Target:
    """ターゲットを管理するクラス"""

    def __init__(self, ss_game):
        """ターゲットのオブジェクトを生成する"""
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ss_game.settings
        self.color = self.settings.target_color

        # ターゲットのrectを生成し、正しい位置に設定する
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
            self.settings.target_height)
        self.center_target()

        # プラスでは下降し、マイナスでは上昇する
        self.direction = 1

    def update(self):
        """ターゲットを上下に動かす"""
        # ターゲットの浮動小数点の位置を更新する
        self.y += self.direction * self.settings.target_speed

        if self.rect.top < 0:
            # 画面の一番上に到達したら方向を変える
            self.rect.top = 0
            self.direction = 1
        elif self.rect.bottom > self.screen_rect.bottom:
            # 画面の一番下に到達したら方向を変える
            self.rect.bottom = self.screen_rect.bottom
            self.direction = -1

        # rectの位置を更新する
        self.rect.y = self.y

    def center_target(self):
        """ターゲットを画面右端中央に配置する"""
        self.rect.midright = self.screen_rect.midright

        # 浮動小数点数からターゲットの位置を格納する
        self.y = float(self.rect.y)

    def draw_target(self):
        """ターゲットを画面に描画する"""
        pygame.draw.rect(self.screen, self.color, self.rect)
