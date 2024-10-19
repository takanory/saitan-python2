import requests


def get_repos_info():
    """GitHub上のPythonリポジトリについての情報を取得する"""
    # API呼び出しを作成してレスポンスを確認する
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)

    print(f"ステータスコード: {r.status_code}")

    return r


def get_response_dict(response):
    """レスポンスのオブジェクトを辞書に変換する"""
    response_dict = response.json()
    return response_dict


def show_repos_info(response_dict):
    """返されたリポジトリについての情報を表示する"""
    print(f"全リポジトリ数: {response_dict['total_count']}")
    print(f"完全な結果: {not response_dict['incomplete_results']}")


def get_repo_dicts(response_dict):
    """1件が各リポジトリを表す辞書のリストを返す"""
    repo_dicts = response_dict['items']
    return repo_dicts


def show_repo_dicts_info(repo_dicts):
    """リポジトリに関する情報を要約する"""
    print(f"情報が返されたリポジトリの数: {len(repo_dicts)}")

    print("\n各リポジトリの選択された情報:")
    for repo_dict in repo_dicts:
        print("\nSelected information about first repository:")
        print(f"名前: {repo_dict['name']}")
        print(f"所有者: {repo_dict['owner']['login']}")
        print(f"スターの数: {repo_dict['stargazers_count']}")
        print(f"リポジトリURL: {repo_dict['html_url']}")
        print(f"作成日: {repo_dict['created_at']}")
        print(f"更新日: {repo_dict['updated_at']}")
        print(f"説明文: {repo_dict['description']}")


response = get_repos_info()
response_dict = get_response_dict(response)
show_repos_info(response_dict)
repo_dicts = get_repo_dicts(response_dict)
show_repo_dicts_info(repo_dicts)
