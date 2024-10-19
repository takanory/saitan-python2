class Settings:
    """横向きシューティングの全設定を格納するクラス"""

    def __init__(self):
        """ゲームの初期設定"""
        # 画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 宇宙船の設定
        self.ship_limit = 3

        # 弾の設定
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # ターゲットの設定
        self.target_height = 120
        self.target_width = 15
        self.target_color = (180, 60, 10)

        # ゲーム全体のダイナミクス
        self.miss_limit = 3
        self.speedup_scale = 2.1
        # levelup_hits を打ったあとに難易度をレベルアップする
        self.levelup_hits = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ゲーム中に変更される設定値を初期化す"""
        self.ship_speed = 3.0
        self.bullet_speed = 12.0
        self.target_speed = 1.5

    def increase_speed(self):
        """速度の設定値を増やす"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale
