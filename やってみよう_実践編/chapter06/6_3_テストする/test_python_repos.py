from python_repos_tested import get_repos_info, get_response_dict, get_repo_dicts


def test_response_status_code():
    """レスポンスのステータスコードが成功かをテストする"""
    r = get_repos_info()
    assert r.status_code == 200


def test_response_dict():
    """リポジトリの数が適切かと、結果が完全であることを確認する"""
    r = get_repos_info()
    response_dict = get_response_dict(r)

    total_count = response_dict['total_count']
    complete_results = not response_dict['incomplete_results']

    assert total_count > 240
    assert complete_results


def test_repo_dicts():
    """repo_dictsの結果が正しいことを確認する"""
    r = get_repos_info()
    response_dict = get_response_dict(r)
    repo_dicts = get_repo_dicts(response_dict)

    assert len(repo_dicts) == 30

    # すべてのリポジトリのスター数が10000以上であることを確認する
    for repo_dict in repo_dicts:
        assert repo_dict['stargazers_count'] > 10_000
