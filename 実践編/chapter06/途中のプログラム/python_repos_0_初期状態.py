import requests

# API呼び出しを作成してレスポンスを確認する
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# レスポンスのオブジェクトを辞書に変換する
response_dict = r.json()

# 結果を処理する
print(response_dict.keys())
