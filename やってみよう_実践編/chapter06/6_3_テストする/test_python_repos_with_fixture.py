import pytest

from python_repos_tested import get_repos_info, get_response_dict, get_repo_dicts


@pytest.fixture
def response():
    """レスポンスオブジェクトを取得する"""
    r = get_repos_info()
    return r


def test_response_status_code(response):
    """レスポンスのステータスコードが成功かをテストする"""
    assert response.status_code == 200


def test_response_dict(response):
    """リポジトリの数が適切かと、結果が完全であることを確認する"""
    response_dict = get_response_dict(response)

    total_count = response_dict['total_count']
    complete_results = not response_dict['incomplete_results']

    assert total_count > 240
    assert complete_results


def test_repo_dicts(response):
    """repo_dictsの結果が正しいことを確認する"""
    response_dict = get_response_dict(response)
    repo_dicts = get_repo_dicts(response_dict)

    assert len(repo_dicts) == 30

    # すべてのリポジトリのスター数が10000以上であることを確認する
    for repo_dict in repo_dicts:
        assert repo_dict['stargazers_count'] > 10_000
