import sys

import pygame

from settings import Settings
from bird import Bird


class BlueBirdGame:
    """ゲーム全体のアセットとふるまいを管理するクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを生成する"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("青いトリのゲーム")

        self.bird = Bird(self)

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            # キーボードとマウスのイベントを監視する
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # ループを通過するたびに画面を再描画する
            self.screen.fill(self.settings.bg_color)
            self.bird.blitme()

            # 最新の状態の画面を表示する
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # ゲームのインスタンスを生成して実行する
    bbg = BlueBirdGame()
    bbg.run_game()
