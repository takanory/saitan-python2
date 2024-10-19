import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class SidewaysShooter:
    """ゲーム全体のアセットとふるまいを管理するクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを生成する"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("横向きシューティング")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """キーボードとマウスのイベントに対応する"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """キーを押すイベントに対応する"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """キーを離すイベントに対応する"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """新しい弾を生成し bullets グループに追加する"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """弾の位置を更新し、古い弾を廃棄する"""
        # 弾の位置を更新する
        self.bullets.update()

        # 見えなくなった弾を廃棄する
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)

    def _update_screen(self):
        """画面上の画像を更新し、新しい画面に切り替える"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # ゲームのインスタンスを生成して実行する
    ss_game = SidewaysShooter()
    ss_game.run_game()
