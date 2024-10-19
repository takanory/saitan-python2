import sys

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from target import Target


class TargetPractice:
    """ゲーム全体のアセットとふるまいを管理するクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを生成する"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ターゲット練習")

        # ゲームの統計情報を格納するインスタンスを生成する
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        # Playボタンを作成する
        self.play_button = Button(self, "Play")

        # ゲームをアクティブな状態で開始する
        self.game_active = False

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.target.update()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """プレイヤーがPlayボタンをクリックしたら新規ゲームを開始する"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        """新規ゲームを開始する"""
        # ゲームの統計情報をリセットする
        self.stats.reset_stats()
        self.game_active = True

        # 残った弾とエイリアンを廃棄する
        self.bullets.empty()

        # 宇宙船とターゲットを中央に配置する
        self.ship.center_ship()
        self.target.center_target()

        # マウスカーソルを非表示にする
        pygame.mouse.set_visible(False)

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
        """弾の位置を更新し、古い弾を廃棄する。またミスの回数を更新する"""
        # 弾の位置を更新する
        self.bullets.update()

        # 見えなくなった弾を廃棄する
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self._increment_misses()

        self._check_bullet_target_collisions()

    def _increment_misses(self):
        """ミスした回数を増やし、ゲームを終了するかを確認する"""
        self.stats.num_misses += 1
        if self.stats.num_misses >= self.settings.miss_limit:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_bullet_target_collisions(self):
        """弾がターゲットに命中したかを確認する"""
        collisions = pygame.sprite.spritecollide(
                self.target, self.bullets, True)

    def _update_screen(self):
        """画面上の画像を更新し、新しい画面に切り替える"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.target.draw_target()

        # ゲームが非アクティブ状態のときに「Play」ボタンを描画する
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # ゲームのインスタンスを作成し、ゲームを実行する
    tp_game = TargetPractice()
    tp_game.run_game()
