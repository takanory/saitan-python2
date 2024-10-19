class Settings:
    """横向きシューティングゲームの全設定を格納するクラス"""

    def __init__(self):
        """ゲームの設定を初期化"""
        # 画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 宇宙船の設定
        self.ship_speed = 3.0
        self.ship_limit = 3

        # 弾の設定
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # エイリアンの設定
        # alien_frequency によって新しいエイリアンの出現頻度を制御します
        # 値が大きいほどエイリアンの出現頻度が高くなり、最大値は1.0です
        self.alien_frequency = 0.015
        self.alien_speed = 6.0
