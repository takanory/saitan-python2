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
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # ホバーテキストを構築する
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可視化を作成する
title = "GitHubで最も多くのスターがついているPythonプロジェクト"
labels = {'x': 'リポジトリ', 'y': 'スターの数'}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)
fig.show()
