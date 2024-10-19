from pathlib import Path
import json


def get_stored_user_info(path):
    """有効なユーザー情報があれば取得"""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """新しいユーザーから情報を取得"""
    username = input("あなたのお名前は？ ")
    game = input("好きなゲームは？ ")
    animal = input("好きな動物は？ ")

    user_dict = {
        'username': username,
        'game': game,
        'animal': animal,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """ユーザー名であいさつし、知っていることを表示する。"""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"おかえりなさい、{user_dict['username']}さん！")
        print(f"最近{user_dict['game']}はどんな調子ですか？")
        print(f"最近{user_dict['animal']}を見かけましたか？")
    else:
        user_dict = get_new_user_info(path)
        msg = f"戻ってきたときにも覚えていますよ、{user_dict['username']}さん！"
        print(msg)

greet_user()