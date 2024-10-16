from pathlib import Path
import json


path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"おかえりなさい、{username}さん！")
else:
    username = input("あなたのお名前は？ ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"戻ってきたときにも名前を覚えていますよ、{username}さん！")