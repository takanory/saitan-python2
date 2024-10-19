import sys
from random import random

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # ゲームの統計情報を格納するインスタンスを生成する
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # ゲームをアクティブな状態で開始する
        self.game_active = True

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()

            if self.game_active:
                # 新しいエイリアンを生成する
                self._create_alien()

                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """弾がエイリアンに当たったかを調べる"""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

    def _create_alien(self):
        """条件がTrueであればエイリアンを生成する"""
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)

    def _update_aliens(self):
        """エイリアンの位置を更新し、宇宙船との衝突を調べる"""
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 画面の左端に到達したエイリアンを探す
        self._check_aliens_left_edge()

    def _check_aliens_left_edge(self):
        """画面の左端に到達したエイリアンに対応する。
        宇宙船に衝突したときと同じ扱いをする。
        """

        for alien in self.aliens.sprites():
            if alien.rect.left < 0:
                self._ship_hit()
                break

    def _ship_hit(self):
        """エイリアンと宇宙船の衝突に対応する"""
        if self.stats.ships_left > 0:
            # 残りの宇宙船の数を減らす
            self.stats.ships_left -= 1

            # 残ったエイリアンと弾を廃棄する
            self.aliens.empty()
            self.bullets.empty()

            # Center the ship.
            self.ship.center_ship()
        else:
            self.game_active = False

    def _update_screen(self):
        """画面上の画像を更新し、新しい画面に切り替える"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # ゲームのインスタンスを生成して実行する
    ss_game = SidewaysShooter()
    ss_game.run_game()
