class Employee:
    """従業員を表すクラス"""

    def __init__(self, f_name, l_name, salary):
        """従業員の初期化"""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=500000):
        """従業員を昇給する"""
        self.salary += amount
