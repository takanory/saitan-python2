from name_function import get_formatted_name


def test_first_last_name():
    """'Janis Joplin' のような名前で動作するか？"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'


def test_first_last_middle_name():
    """'Wolfgang Amadeus Mozart' のような名前で正しく動作するか？"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
