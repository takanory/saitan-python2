import requests

# API呼び出しを作成してレスポンスを確認する
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# レスポンスのオブジェクトを辞書に変換する
response_dict = r.json()
print(f"全リポジトリ数: {response_dict['total_count']}")
print(f"完全な結果: {not response_dict['incomplete_results']}")

# リポジトリに関する情報を調べる
repo_dicts = response_dict['items']
print(f"情報が返されたリポジトリの数: {len(repo_dicts)}")

# 1つ目のリポジトリを調査する
repo_dict = repo_dicts[0]
print(f"\nキーの数: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
