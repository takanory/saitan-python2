favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("以下の言語が投票されました。")
for language in set(favorite_languages.values()):
    print(language.title())
