def build_person(first_name, last_name):
    """人についての情報を辞書で返す"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
