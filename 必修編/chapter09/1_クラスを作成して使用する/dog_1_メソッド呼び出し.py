class Dog:
    """イヌをモデル化したシンプルな実装例"""

    def __init__(self, name, age):
        """名前と年齢の属性を初期化する"""
        self.name = name
        self.age = age

    def sit(self):
        """イヌに「おすわり」の命令を実行する"""
        print(f"{self.name}はおすわりしている。")

    def roll_over(self):
        """イヌに「ごろーん」の命令を実行する"""
        print(f"{self.name}がごろーんした！")


my_dog = Dog('ウィリー', 6)
my_dog.sit()
my_dog.roll_over()
