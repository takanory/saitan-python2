from pathlib import Path
import json


username = input("あなたのお名前は？ ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"戻ってきたときにも名前を覚えていますよ、{username}さん！")