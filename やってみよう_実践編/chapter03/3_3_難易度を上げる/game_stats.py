class GameStats:
    """ゲームの統計情報を記録する"""

    def __init__(self, ss_game):
        """統計情報を初期化する"""
        self.settings = ss_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ゲーム中に変更される統計情報を初期化する"""
        self.ships_left = self.settings.ship_limit
        self.num_misses = 0
        self.num_hits = 0
