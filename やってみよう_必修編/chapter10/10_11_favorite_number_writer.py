from pathlib import Path
import json

number = input("好きな数字はなんですか？ ")

path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print("ありがとう！この数字を覚えています。")