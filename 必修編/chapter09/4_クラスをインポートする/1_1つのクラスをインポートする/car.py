"""自動車を表すために使用できるクラス"""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """自動車の特徴となる属性を初期化する"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """フォーマットされた名前を返す"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """自動車の走行距離を出力する"""
        print(f"走行距離は{self.odometer_reading}マイルです。")

    def update_odometer(self, mileage):
        """
        指定された値で走行距離を更新します。
        走行距離を減らそうとする処理は拒否します。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("走行距離は減らせません！")

    def increment_odometer(self, miles):
        """指定された距離を走行距離に追加する"""
        self.odometer_reading += miles
