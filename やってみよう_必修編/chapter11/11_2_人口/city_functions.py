"""都市についての関数"""


def city_country(city, country, population):
    """'Santiago, Chile - 人口 5000000'のような文字列を返す"""
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" - 人口 {population}"
    return output_string
