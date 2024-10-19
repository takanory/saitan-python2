import sys

import pygame

from settings import Settings


class KeyGame:
    """ゲーム全体のアセットとふるまいを管理するクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを生成する"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("キーを出力")

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
        # 押されたキーを表示し、qが押されたら終了する
        # 出力の詳細については以下を参照してください
        # https://www.pygame.org/docs/ref/key.html
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """画面上の画像を更新し、新しい画面に切り替える"""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    # ゲームのインスタンスを生成して実行する
    kg = KeyGame()
    kg.run_game()
