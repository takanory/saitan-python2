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

def get_new_username(path):
    """新たなユーザー名の入力を促す。"""
    username = input("あなたのお名前は？ ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """ユーザー名であいさつする。"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"おかえりなさい、{username}さん！")
    else:
        username = get_new_username(path)
        print(f"戻ってきたときにも名前を覚えていますよ、{username}さん！")

greet_user()