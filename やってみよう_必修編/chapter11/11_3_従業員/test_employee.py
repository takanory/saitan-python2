from employee import Employee


def test_give_default_raise():
    """デフォルトの昇給が正しく動作することをテストする"""
    employee = Employee('takanori', 'suzuki', 6_500_000)
    employee.give_raise()
    assert employee.salary == 7_000_000


def test_give_custom_raise():
    """指定した値での昇給が正しく動作することをテストする"""
    employee = Employee('takanori', 'suzuki', 6_500_000)
    employee.give_raise(1_000_000)
    assert employee.salary == 7_500_000
