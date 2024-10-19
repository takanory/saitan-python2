import json
from pathlib import Path

class GameStats:
    """エイリアン侵略ゲームの統計情報を記録する"""

    def __init__(self, ai_game):
        """統計情報を初期化する"""
        self.settings = ai_game.settings
        self.reset_stats()

        # ハイスコアはリセットしない
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """ファイルが存在すれば、ハイスコアをファイルから取得する"""
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        """ゲーム中に変更される統計情報を初期化する"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
