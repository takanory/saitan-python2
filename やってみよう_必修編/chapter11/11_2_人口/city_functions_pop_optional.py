"""都市についての関数"""


def city_country(city, country, population=0):
    """都市と国の文字列を返す"""
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - 人口 {population}"
    return output_string
