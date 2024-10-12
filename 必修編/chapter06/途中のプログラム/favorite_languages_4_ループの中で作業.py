favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"こんにちは{name.title()}。")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}、あなたの好きなプログラミング言語は{language}ですね！")
