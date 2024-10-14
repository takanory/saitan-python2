import requests
import json

# API呼び出しを作成してそのレスポンスを格納する
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# データの構造を調べる
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
