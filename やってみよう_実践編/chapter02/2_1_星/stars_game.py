import sys

import pygame

from settings import Settings
from star import Star


class StarsGame:
    """ゲーム全体のアセットとふるまいを管理するクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを生成する"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("星")

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """キーボードとマウスのイベントに対応する"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """キーを押すイベントに対応する"""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        """空全体に星を生成する"""
        # 星を配置する余白がなくなるまで星を生成する
        # 星の間には2つの星の分のスペースを空ける
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = 2*star_width, 2*star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            # 列の最後でX座標をリセットし、Y座標を増加する
            current_x = 2 * star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """星を1つ生成し配置する"""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """画面上の画像を更新し、新しい画面に切り替える"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # ゲームのインスタンスを生成して実行する
    sg = StarsGame()
    sg.run_game()
