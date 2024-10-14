import requests
import plotly.express as px

# API呼び出しを作成してレスポンスを確認する
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

# 全体の結果を処理する
response_dict = r.json()
print(f"完全な結果: {not response_dict['incomplete_results']}")

# リポジトリ情報を処理する
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可視化を作成する
fig = px.bar(x=repo_names, y=stars)
fig.show()
