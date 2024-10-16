from pathlib import Path
import json


def get_stored_username(path):
    """保存されたユーザー名があれば取得する。"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    """ユーザー名であいさつする。"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"おかえりなさい、{username}さん！")
    else:
        username = input("あなたのお名前は？ ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"戻ってきたときにも名前を覚えていますよ、{username}さん！")

greet_user()