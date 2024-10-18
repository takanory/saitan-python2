from city_functions_pop_optional import city_country


def test_city_country():
    """シンプルな国と都市の組み合わせで動作するか？"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'


def test_city_country_population():
    """人口の引数を含めることができるか？"""
    santiago_chile = city_country('santiago', 'chile', population=5_000_000)
    assert santiago_chile == 'Santiago, Chile - 人口 5000000'
