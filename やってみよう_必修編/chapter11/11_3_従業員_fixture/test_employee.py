import pytest

from employee import Employee


@pytest.fixture
def employee():
    """すべてのテスト関数で使用できる従業員オブジェクト"""
    employee = Employee('takanori', 'suzuki', 6_500_000)
    return employee


def test_give_default_raise(employee):
    """デフォルトの昇給が正しく動作することをテストする"""
    employee.give_raise()
    assert employee.salary == 7_000_000


def test_give_custom_raise(employee):
    """指定した値での昇給が正しく動作することをテストする"""
    employee.give_raise(1_000_000)
    assert employee.salary == 7_500_000
