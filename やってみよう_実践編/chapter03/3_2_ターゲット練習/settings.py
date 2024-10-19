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

        self.target_speed = 1.5

        # ゲーム全体のダイナミクス
        self.miss_limit = 3
