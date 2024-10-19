from pathlib import Path
import json

path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("好きな数字はなんですか？ ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("ありがとう！この数字を覚えています。")
else:
    number = json.loads(contents)
    print(f"あなたの好きな数字を知っています！それは{number}です。")