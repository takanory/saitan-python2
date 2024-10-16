from city_functions import city_country


def test_city_country():
    """シンプルな国と都市の組み合わせで動作するか？"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'
